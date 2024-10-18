import json

from setuptools import setup, find_packages
import python_code_check

with open("README.md", "r", encoding="utf-8") as readme_fp:
    readme = readme_fp.read()

def get_commitizen_config_json():
    with open('.cz.json', encoding="utf-8") as commitizen_config_file:
        return json.load(commitizen_config_file)


commitizen_config_json = get_commitizen_config_json()

__version__ = commitizen_config_json['commitizen']["version"]

# https://klen.github.io/create-python-packages.html
setup(name="python_code_check",
      author="Eva Dugina",
      version=__version__,
      description="Utility for automatic Python-CodeCheck with various tools",
      long_description=readme,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      package_data={'python_code_check': ['checkers/*']},
      entry_points={
            "console_scripts": [
                  "python_code_check = python_code_check.__main__:main"
            ]
      },
      )