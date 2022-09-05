# This Python file uses the following encoding: utf-8
# File generated accordingly to Packaging and distributing projects guide
# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

# ----------------------- #
#  THIS IS A SETUP FILE   #
# ----------------------- #

# Imports
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="otto_FTAF",
    version="0.0.2",
    author="Rodolpho Kades de Oliveira e Silva",
    author_email="rodolpho_kades@hotmail.com",
    keywords="Thermodynamics, Otto, Air-Fuel, Model, Simulation",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["numpy", "scipy", "sympy", "matplotlib"],
    description='Finite Time Air-Fuel Otto Cycles in Python',
)
