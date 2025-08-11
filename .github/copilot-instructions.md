# Pirate Weather Translations

Pirate Weather Translations is a Python library that translates machine-readable weather summaries from the Pirate Weather API into human-readable text in 50+ languages.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Dependencies
- Install Python dependencies: `python -m pip install -r requirements.txt`
  - Takes ~5 seconds to complete
  - Installs ruff, pytest, pytest-subtests, coverage, pytest-cov
  - No additional system dependencies required

### Testing
- Run the complete test suite: `pytest test.py`
  - Takes ~8 seconds to complete
  - Runs 18 tests with 3634 subtests (validates all language translations)
  - **Always run tests after making changes to translation files**
- Run tests with verbose output: `pytest test.py -v`
- Run tests with coverage: `pytest test.py --cov`

### Linting and Formatting
- Check code style: `ruff check --output-format=github . --fix`
  - Takes <1 second to complete
  - Automatically fixes most issues
- Format code: `ruff format .`
  - Takes <1 second to complete
  - **Always run both commands before committing changes**

### Core Functionality Testing
- Test translation directly:
  ```python
  from pirateweather_translations.translation import Translation
  from pirateweather_translations.lang.en import template
  t = Translation(template)
  result = t.translate(['title', 'heavy-rain'])  # Returns "Heavy Rain"
  ```
- Test dynamic loading:
  ```python
  from pirateweather_translations.dynamic_loader import load_translation
  from pirateweather_translations.translation import Translation
  template = load_translation('en')
  t = Translation(template)
  result = t.translate(['title', 'clear'])  # Returns "Clear"
  ```

## Validation

### Manual Validation Requirements
- **Always run the full test suite** after making any changes to translation files
- Test at least 3-5 different translation expressions manually when adding/modifying languages
- Verify that new language files follow the same structure as existing ones (have a `template` dict)
- **Always run linting and formatting** - the CI will fail without proper code style

### Complete End-to-End Validation Scenario
1. Install dependencies: `python -m pip install -r requirements.txt`
2. Run full test suite: `pytest test.py`
3. Test manual translation: Use the code examples above to test specific translations
4. Run linting: `ruff check --output-format=github . --fix`
5. Run formatting: `ruff format .`
6. Verify specific language works: `python -c "from pirateweather_translations.dynamic_loader import load_translation; from pirateweather_translations.translation import Translation; t = Translation(load_translation('fr')); print(t.translate(['title', 'clear']))"`

## Repository Structure

### Key Directories and Files
```
pirateweather_translations/        # Main package
├── translation.py                 # Core translation engine
├── dynamic_loader.py              # Dynamic language loading utilities  
└── lang/                          # Language translation modules
    ├── en.py                      # English (reference implementation)
    ├── fr.py, de.py, es.py...     # 50+ language translations
    └── x-pig-latin.py             # Example/test language

test_cases/                        # Test cases for each language
├── en.py                          # English test cases (reference)
├── fr.py, de.py, es.py...        # Test cases for each language
└── ...

test.py                            # Main test runner
requirements.txt                   # Python dependencies
setup.py                          # Package setup
.ruff.toml                        # Ruff linting configuration
pytest.ini                        # Pytest configuration
```

### Language File Structure
Each language file in `pirateweather_translations/lang/` must have:
- A `template` dictionary mapping weather conditions to translations
- Functions for complex translations (optional)
- Support for both string templates (`"$1 and $2"`) and Python functions

### Test Case Structure  
Each test file in `test_cases/` must have:
- A `cases` dictionary mapping expected output to input expressions
- Complete coverage of all weather conditions for that language

## Common Tasks

### Adding a New Language Translation
1. Create `pirateweather_translations/lang/[lang-code].py` with a `template` dict
2. Create `test_cases/[lang-code].py` with a `cases` dict  
3. Use `pirateweather_translations/lang/en.py` and `test_cases/en.py` as references
4. Run tests to validate: `pytest test.py`
5. Check that your language appears in test output

### Modifying Existing Translations
1. Edit the appropriate file in `pirateweather_translations/lang/`
2. Update corresponding test cases in `test_cases/` if needed
3. **Always run the full test suite**: `pytest test.py`
4. Manually test your changes with the validation commands above

### Working with Translation Templates
- Simple string templates: `"heavy-rain": "Heavy Rain"`  
- Parameterized templates: `"minutes": "$1 minutes"`
- Complex functions: `"and": lambda stack, a, b: f"{a} and {b}"`
- Reference `pirateweather_translations/lang/en.py` for comprehensive examples

## GitHub Actions Integration

### CI Workflows (.github/workflows/)
- `test.yml`: Runs `pytest test.py` on every push/PR  
- `lint.yml`: Runs `ruff format .` and `ruff check` with auto-commit
- `release.yml`: Handles package releases
- `codeql.yml`: Security scanning

### Pre-commit Checklist  
- [ ] Run `pytest test.py` - all tests must pass
- [ ] Run `ruff format .` - code must be formatted
- [ ] Run `ruff check --output-format=github . --fix` - no linting errors
- [ ] Manually test translation functionality if you modified translation files

## Translation Format Reference

The library processes machine-readable weather expressions like:
- `"heavy-rain"` → `"Heavy Rain"`
- `["title", "clear"]` → `"Clear"`  
- `["and", "light-wind", "light-clouds"]` → `"Breezy and Partly Cloudy"`
- `["starting-in", "very-light-rain", ["minutes", 15]]` → `"Drizzle starting in 15 minutes"`

See README.md Appendix A for complete format specification.

## Troubleshooting

### Common Issues
- **Import errors**: Ensure you're in the repository root directory
- **Missing dependencies**: Run `python -m pip install -r requirements.txt`
- **Test failures**: Check that your `template` dict in lang files matches expected test cases
- **Linting errors**: Run `ruff format .` then `ruff check --fix` to auto-fix most issues

### Debug Commands  
```bash
# Test specific language loading
python -c "from pirateweather_translations.dynamic_loader import load_all_translations; print(list(load_all_translations().keys()))"

# Test translation step by step  
python -c "from pirateweather_translations.translation import Translation; print(Translation({'foo': 'bar'}).translate('foo'))"
```