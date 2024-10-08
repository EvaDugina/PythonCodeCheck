from setuptools import setup, find_packages
import python_code_check

with open("README.md", "r", encoding="utf-8") as readme_fp:
    readme = readme_fp.read()

# https://klen.github.io/create-python-packages.html
setup(name="python_code_check",
      author="Eva Dugina",
      version=python_code_check.__version__,
      description="Utility for automatic Python-CodeCheck with various tools",
      long_description=readme,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      entry_points={
            "console_scripts": [
                  "python_code_check = python_code_check.main:main"
            ]
      },
      )