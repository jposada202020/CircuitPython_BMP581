# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_immaterial",
]

autodoc_preserve_defaults = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "BusDevice": ("https://docs.circuitpython.org/projects/busdevice/en/latest/", None),
    "Register": ("https://docs.circuitpython.org/projects/register/en/latest/", None),
    "CircuitPython": ("https://docs.circuitpython.org/en/latest/", None),
}

autodoc_mock_imports = ["digitalio", "busio", "adafruit_register"]
autoclass_content = "both"
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
# General information about the project.
project = "CircuitPython BMP581 Library"
creation_year = "2023"
current_year = str(datetime.datetime.now().year)
year_duration = (
    current_year
    if current_year == creation_year
    else creation_year + " - " + current_year
)
copyright = year_duration + "Jose D. Montoya"
author = "Jose D. Montoya"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

language = "en"
autoclass_content = "both"
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    "requirements.txt",
]

default_role = "any"
add_function_parentheses = True
pygments_style = "sphinx"
todo_include_todos = False
todo_emit_warnings = False
napoleon_numpy_docstring = False
html_baseurl = "https://circuitpython-bmp581.readthedocs.io/"
rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight
.. default-literal-role:: python
"""
html_theme = "sphinx_immaterial"

html_theme_options = {
    "features": [
        "search.share",
    ],
    # Set the color and the accent color
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/jposada202020/CircuitPython_BMP581/",
    "repo_name": "CircuitPython BMP581",
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/jposada202020/CircuitPython_BMP581",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/circuitpython-bmp581/",
        },
        {
            "name": "CircuitPython Downloads",
            "icon": "octicons/download-24",
            "link": "https://circuitpython.org",
        },
    ],
}
html_favicon = "_static/favicon.ico"

# Output file base name for HTML help builder.
htmlhelp_basename = "CircuitPython_Bmp581_Librarydoc"

sphinx_immaterial_custom_admonitions = [
    {
        "name": "warning",
        "color": (255, 66, 66),
        "icon": "octicons/alert-24",
        "override": True,
    },
    {
        "name": "note",
        "icon": "octicons/pencil-24",
        "override": True,
    },
    {
        "name": "seealso",
        "color": (255, 66, 252),
        "icon": "octicons/eye-24",
        "title": "See Also",
        "override": True,
    },
    {
        "name": "hint",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "tip",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "important",
        "icon": "material/school",
        "override": True,
    },
]
python_type_aliases = {
    "DigitalInOut": "digitalio.DigitalInOut",
}

object_description_options = [
    ("py:.*", dict(generate_synopses="first_sentence")),
]
# Set link name generated in the top bar.
html_title = "CircuitPython BMP581"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["extra_css.css"]
