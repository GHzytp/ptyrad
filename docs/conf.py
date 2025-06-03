# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'PtyRAD'
copyright = '2025'
author = 'Chia-Hao Lee'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",      
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon", 
    "sphinx.ext.viewcode",
    "sphinx_design", # Allows tab, grid card, drop down and more
    "sphinx_togglebutton", 
    "myst_parser",            
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
    'members': False,
    'inherited-members': False,
    'show-inheritance': False,
}

exclude_patterns = [] # Exclude api could also make the build much faster
autosummary_generate = True # This controls the api autosummary, which is quite slow. Toggle off for faster build while testing other pages.
templates_path = ["_templates"]

# More comprehensive MyST configuration
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Make sure autodoc works with MyST
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/chiahao3/ptyrad",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "show_navbar_depth": 1,
    "show_toc_level": 1, # The 2nd (in content TOC on the right)
    "home_page_in_toc": True,
    "collapse_navigation": True # This collapses all sections by default
}

# Add your _static directory to the static path
html_static_path = ['_static']

html_css_files = ['custom.css'] # To allow table hover effects in `installation.md`

html_js_files = ['custom.js'] # To allow ref switch the tab in `installation.md`