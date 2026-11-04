import inspect
import re

# $n references to an expression's arguments in a template string
_ARG_REF = re.compile(r"\$\d+")

# Translations remembered per language; the API repeats a few hundred distinct
# summaries, so this bound is only a guard against unbounded growth.
_CACHE_SIZE = 4096


def is_variadic(func):
    # True if the function takes *args, e.g. def list_function(stack, *items)
    return bool(func.__code__.co_flags & inspect.CO_VARARGS)


def parse(template, expr, stack):
    # If the expression is a number, just return its string representation
    if isinstance(expr, int):
        return str(expr)

    # If the expression is a string
    if isinstance(expr, str):
        if expr not in template:
            raise ValueError(f'"{expr}" not found in language template.')

        stack.append(expr)

        val = template[expr]

        if isinstance(val, str):
            # If the template value contains $n references, that's invalid in a value context
            if _ARG_REF.search(val):
                raise ValueError(
                    f'"{expr}" was used in a value context, '
                    f"but is expected in a template context."
                )
            result = val

        elif callable(val):
            # If the template function expects arguments (other than `this`), this is invalid
            # in a value context since we're not passing any arguments.
            # We'll check the function's argument count.
            argcount = val.__code__.co_argcount
            # Expecting only the context (stack) as single argument
            if argcount != 1 or is_variadic(val):
                raise ValueError(
                    f'"{expr}" was used in a value context, '
                    f"but is expected in a template context."
                )
            # Call the function with stack as the context (first argument)
            result = val(stack)

        else:
            raise TypeError(f'"{expr}" is not a valid language template pattern.')

        stack.pop()
        return result

    # If the expression is an array-like structure: [term, arg1, arg2, ...]
    elif isinstance(expr, list) and len(expr) > 0 and isinstance(expr[0], str):
        if expr[0] not in template:
            raise ValueError(f'"{expr[0]}" not found in language template.')

        stack.append(expr[0])
        val = template[expr[0]]

        if isinstance(val, str):
            # Here we need to replace occurrences of $n in the template string
            def repl(m):
                index = int(m.group()[1:])
                return parse(template, expr[index], stack)

            result = _ARG_REF.sub(repl, val)

        elif callable(val):
            # In JS code:
            #   if(template[expr[0]].length === 0) ...
            #   if(template[expr[0]].length !== expr.length - 1) ...
            #
            # In Python, we can check the function's argument count via __code__.co_argcount.
            # We'll assume that the function signature includes the stack as the first argument.
            # Thus, if the function is a value context function (no arguments), co_argcount should be 1.
            # If it's a template context (needs arguments), co_argcount should match 1 + (expr.length - 1)
            # because we pass stack plus the arguments.

            argcount = val.__code__.co_argcount
            expected_args = expr[1:]  # all arguments after the first

            if is_variadic(val):
                # Variadic functions (e.g. def f(stack, *items)) accept any number of
                # arguments, as long as the fixed ones are filled and at least one is given.
                if len(expected_args) == 0 or len(expected_args) < argcount - 1:
                    raise ValueError(
                        f'Template "{expr[0]}" did not expect {len(expected_args)} arguments.'
                    )
            elif len(expected_args) == 0:
                # This means expr is used in a template context but no arguments.
                # According to JS code:
                # if(template[expr[0]].length === 0) { throw ... }
                # Here length===0 means no arguments expected for a value context.
                # If we're in a template context (array), we expect at least one argument unless
                # the template pattern is incorrect.
                # Actually, the JS code says:
                # if(template[expr[0]].length === 0) {
                #   throw "\"expr[0]\" was used in a template context, but is expected in a value context."
                # }
                # That means if the function expects no arguments (length=0), it's a value-context function,
                # but we are using it in a template context.
                if argcount == 1:
                    raise ValueError(
                        f'"{expr[0]}" was used in a template context, '
                        f"but is expected in a value context."
                    )
                # If argcount != 1, then it expects arguments, but we gave none.
                # The JS code also checks if(template[expr[0]].length !== expr.length - 1).
                # expr.length - 1 = 0 in this case, so we must raise:
                if argcount != 1 + len(expected_args):
                    raise ValueError(
                        f'Template "{expr[0]}" did not expect {len(expected_args)} arguments.'
                    )
            else:
                # If there are arguments, we must ensure argcount matches:
                # argcount should be 1 (for stack) + len(expected_args)
                if argcount == 1:
                    # The function expects no arguments, but we provided some:
                    raise ValueError(
                        f'"{expr[0]}" was used in a template context, '
                        f"but is expected in a value context."
                    )

                if argcount != 1 + len(expected_args):
                    raise ValueError(
                        f'Template "{expr[0]}" did not expect {len(expected_args)} arguments.'
                    )

            # Parse arguments
            parsed_args = [parse(template, arg, stack) for arg in expected_args]
            # Call the function with stack as the first argument
            result = val(stack, *parsed_args)

        else:
            raise TypeError(f'"{expr[0]}" is not a valid language template pattern.')

        stack.pop()
        return result

    else:
        raise ValueError("Invalid expression.")


def _cache_key(expr):
    """A hashable copy of an expression. Each term is tagged with its type,
    because equal values of different types (1, 1.0, True) parse differently."""
    if isinstance(expr, list):
        return (list, tuple(_cache_key(item) for item in expr))
    return (type(expr), expr)


class Translation:
    def __init__(self, template):
        self.template = template
        self._cache = {}

    def translate(self, expr):
        # Templates are pure functions of the expression (the stack they see is
        # built from the expression itself), so a translated expression can be
        # reused. Callers translate the same few summaries many times per
        # forecast, and parsing them each time dominated the cost.
        try:
            key = _cache_key(expr)
            cached = self._cache.get(key)
        except TypeError:  # an unhashable term; translate without caching
            return parse(self.template, expr, [])
        if cached is not None:
            return cached
        result = parse(self.template, expr, [])
        if len(self._cache) >= _CACHE_SIZE:
            self._cache.clear()
        self._cache[key] = result
        return result

    def is_supported(self, term):
        return term in self.template
