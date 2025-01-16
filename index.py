import os
import re
import importlib.util
from pirateweather_translations.translation import Translation

# The directory containing language template files
lang_dir = os.path.join(os.path.dirname(__file__), "pirateweather_translations", "lang")

exports = {}

# Iterate over files in lang directory
for filename in os.listdir(lang_dir):
    # Match files that follow the pattern: name.js (with name not starting with '.')
    match = re.match(r"^([^.].*)\.js$", filename)
    if match:
        # Extract the language name (e.g. 'en', 'fr', etc.)
        lang_name = match.group(1)

        # Construct the corresponding Python module path.
        # Here we assume each .js has been replaced by a .py file with the same base name.
        py_module_path = os.path.join(lang_dir, lang_name + ".py")

        # Dynamically load the Python module
        spec = importlib.util.spec_from_file_location(lang_name, py_module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        # `template` must be defined inside the Python module
        if not hasattr(mod, "template"):
            raise Exception(f"No 'template' found in {lang_name}.py")

        template = mod.template

        # There's no direct equivalent to Object.freeze() in Python,
        # but we trust that we won't modify 'template'.

        # Create a new Translation instance and store it
        exports[lang_name] = Translation(template)

# If you want these translations accessible as top-level variables:
globals().update(exports)

# If you want a controlled list of exported names:
__all__ = list(exports.keys())
