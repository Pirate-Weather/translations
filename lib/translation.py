import re


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
            if re.search(r"\$\d+", val):
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
            if argcount != 1:
                raise ValueError(
                    f'"{expr}" was used in a value context, '
                    f"but is expected in a template context."
                )
            # Call the function with stack as the context (first argument)
            result = val(stack)

        else:
            raise ValueError(f'"{expr}" is not a valid language template pattern.')

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

            result = re.sub(r"\$\d+", repl, val)

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

            if len(expected_args) == 0:
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
            raise ValueError(f'"{expr[0]}" is not a valid language template pattern.')

        stack.pop()
        return result

    else:
        raise ValueError("Invalid expression.")


class Translation:
    def __init__(self, template):
        self.template = template

    def translate(self, expr):
        return parse(self.template, expr, [])

    def is_supported(self, term):
        return term in self.template
