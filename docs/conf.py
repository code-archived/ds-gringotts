# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# ? insert the project paths to let sphinx recognize/find packages
sys.path.append(os.path.abspath(os.path.join("..", "modules", "dt_utils")))
sys.path.append(os.path.abspath(os.path.join("..", "modules", "prettify")))
sys.path.append(os.path.abspath(os.path.join("..", "modules", "sqlparser")))
sys.path.append(os.path.abspath(os.path.join("..", "modules", "wrappers")))

project = 'ds-gringotts'
copyright = '2024, Debmalya Pramanik'
author = 'Debmalya Pramanik'
release = open(os.path.abspath(os.path.join("..", "VERSION")), "r").read()

# WIP import all modules, house-keeping
import datetime_ # noqa: F401, F403 # pyright: ignore[reportMissingImports]
import prettify # noqa: F401, F403 # pyright: ignore[reportMissingImports]
import sqlparser # noqa: F401, F403 # pyright: ignore[reportMissingImports]
import timer_decorator # noqa: F401, F403 # pyright: ignore[reportMissingImports]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
