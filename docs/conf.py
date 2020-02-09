"""Sphinx configuration."""
project = "ccautils"
author = "Chris Allison"
copyright = f"2020 {author}"

extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
