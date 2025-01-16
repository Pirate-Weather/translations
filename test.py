import pytest
import os
import re
import importlib.util
from pirateweather_translations.translation import Translation


@pytest.fixture
def test_translation():
    return Translation(
        {
            "foo": "bar",
            "bar": "meeple $2",
            "baz": lambda a, b, c: f"meeple {c}",
            "quux": lambda a: "glorple",
        }
    )


def test_return_number_in_string_form(test_translation):
    assert test_translation.translate(42) == "42"


def test_throw_error_for_unrecognized_string(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate("42")


def test_apply_value_conversion(test_translation):
    assert test_translation.translate("foo") == "bar"


def test_throw_error_for_expected_string(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate("bar")


def test_throw_error_for_expected_function(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate("baz")


def test_throw_error_for_empty_array(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate([])


def test_apply_string_template(test_translation):
    assert test_translation.translate(["bar", 10, 20]) == "meeple 20"


def test_fail_to_apply_function_with_wrong_arity(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate(["baz", 10, 20, 30])


def test_apply_function_template(test_translation):
    assert test_translation.translate(["baz", 10, 20]) == "meeple 20"


def test_recursively_apply_function_templates(test_translation):
    assert (
        test_translation.translate(["bar", 10, ["baz", 20, "foo"]])
        == "meeple meeple bar"
    )


def test_throw_error_for_undefined(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate(None)


def test_throw_error_for_null(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate(None)


def test_throw_error_for_object(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate({})


def test_apply_zero_argument_function(test_translation):
    assert test_translation.translate("quux") == "glorple"


def test_fail_to_apply_zero_argument_function_given_arguments(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate(["quux"])


def test_fail_to_apply_function_template_given_value(test_translation):
    with pytest.raises(ValueError):
        test_translation.translate("baz")


def test_provide_context_to_functions():
    test = Translation(
        {
            "foo": lambda a, b, c, d: f"Moop. {b} {c} {d}",
            "bar": "Boop.",
            "baz": lambda a, b: f"Soup. {b}",
            "quux": lambda a: "Floop.",
            "neem": lambda a, b: f"Bloop. {b}",
            "glorp": lambda a, b: "Rope?",
        }
    )

    # Call the translation with nested structure to validate context
    assert (
        test.translate(["foo", "bar", ["baz", "quux"], ["neem", ["glorp", 42]]])
        == "Moop. Boop. Soup. Floop. Bloop. Rope?"
    )


def test_languages(subtests):
    test_dir = os.path.join(os.path.dirname(__file__), "test_cases")
    # Iterate over files in lang directory
    for filename in os.listdir(test_dir):
        with subtests.test(msg="custom message", filename=filename):
            if filename.endswith(".py") and filename != "__init__.py":
                match = re.match(r"^([^.].*)\.py$", filename)
                # Extract the language name (e.g. 'en', 'fr', etc.)
                lang_name = match.group(1)

                # Construct the corresponding Python module path.
                # Here we assume each .js has been replaced by a .py file with the same base name.
                py_module_path = os.path.join(test_dir, lang_name + ".py")

                # Dynamically load the Python module
                spec = importlib.util.spec_from_file_location(lang_name, py_module_path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

                # `template` must be defined inside the Python module
                if not hasattr(mod, "cases"):  # pragma: no cover
                    raise Exception(f"No 'cases' found in {lang_name}.py")

                template = mod.cases

                lang_dir = os.path.join(
                    os.path.dirname(__file__), "pirateweather_translations", "lang"
                )
                # Construct the corresponding Python module path.
                # Here we assume each .js has been replaced by a .py file with the same base name.
                py_module_path = os.path.join(lang_dir, lang_name + ".py")

                # Dynamically load the Python module
                l_spec = importlib.util.spec_from_file_location(
                    lang_name, py_module_path
                )
                l_mod = importlib.util.module_from_spec(l_spec)
                l_spec.loader.exec_module(l_mod)

                l_template = l_mod.template

                # There's no direct equivalent to Object.freeze() in Python,
                # but we trust that we won't modify 'template'.
                for source, expected in template.items():
                    with subtests.test(
                        msg="custom message",
                        l_template=l_template,
                        expected=expected,
                        source=source,
                    ):
                        assert Translation(l_template).translate(expected) == source
