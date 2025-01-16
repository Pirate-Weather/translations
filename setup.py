"""Set up the Pirate Weather library."""

import os

from setuptools import find_packages, setup

__version__ = "0.0.7"


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")) as f:
    README = f.read()

repo_url = "https://github.com/Pirate-Weather/translations"


setup(
    name="pirateweather-translations",
    version=__version__,
    author="Pirate-Weather",
    description=("Translate Pirate Weather API summaries into any language"),
    license="BSD 2-clause",
    keywords="weather API pirateweather translations",
    url=repo_url,
    download_url=f"{repo_url}/archive/{__version__}.tar.gz",
    packages=find_packages(where="pirateweather_translations"),
    package_dir={"": "pirateweather_translations"},
    include_package_data=True,  # Include package data files
    package_data={
        "pirateweather_translations.lang": ["*.py"],  # Include all .py files in lang/
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
