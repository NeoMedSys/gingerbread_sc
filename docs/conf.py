# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
import toml

sys.path.insert(0, os.path.abspath(".."))

# get version from pyproject.toml
with open("../pyproject.toml") as f:
    pyproject = toml.load(f)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Gingerbread"
copyright = "2023, Martin Soria Røvang"
author = "Martin Soria Røvang"
release = pyproject["tool"]["poetry"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
]

templates_path = ["_templates"]
exclude_patterns = []
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_logo = "63ecff6168e0e.png"

# european time format "%b %d %y at %H:%M"
today_fmt = "%b %d %y at %H:%M"
