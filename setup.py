from setuptools import setup, find_packages
from pathlib import Path

lines = Path("sphinx_multitoc_numbering").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="sphinx-multitoc-numbering",
    version=version,
    description="Supporting continuous HTML section numbering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    install_requires=["sphinx>=3"],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "testing": [
            "pytest~=5.4",
            "pytest-cov~=2.8",
            "coverage<5.0",
            "pytest-regressions",
            "jupyter-book",
        ],
        "rtd": [
            "sphinx>=3.0",
            "sphinx-book-theme",
            "myst-parser",
        ],
    },
    include_package_data=True,
)
