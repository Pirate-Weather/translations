import os
import importlib
import pirateweather_translations.lang
from .translation import Translation

def load_translation(language_code):
    try:
        lang_module = importlib.import_module(f"pirateweather_translations.lang.{language_code}")
        return lang_module.template
    except ImportError:
        raise ValueError(f"Language {language_code} not supported.")



def load_all_translations():
    """
    Load all translations from the `lang` directory into a dictionary.
    Keys are language codes, and values are Translation instances.
    """
    translations = {}
    lang_dir = os.path.dirname(pirateweather_translations.lang.__file__)  # Path to the lang directory

    for filename in os.listdir(lang_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            lang_code = filename[:-3]  # Strip ".py" extension
            module_name = f"pirateweather_translations.lang.{lang_code}"

            try:
                # Dynamically import the language module
                lang_module = importlib.import_module(module_name)

                # Check if the module has a `template` attribute
                if hasattr(lang_module, "template"):
                    translations[lang_code] = Translation(lang_module.template)
                else:
                    raise ImportError(f"Module {module_name} does not have a 'template'.")
            except ImportError as e:
                print(f"Failed to load language module {module_name}: {e}")

    return translations