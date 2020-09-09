from setuptools import setup, find_packages
from pathlib import Path

lines = Path("parttoc_numbering").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="sphinx-parttoc-numbering",
    version=version,
    description="Supporting part in HTML section numbering",
    packages=find_packages(),
    install_requires=[
        "sphinx"
    ]
)

