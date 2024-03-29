# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'rna_library'
copyright = '2021, Christopher Jurich'
author = 'Christopher Jurich'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]
extensions.append('autoapi.extension')
extensions.append('sphinx.ext.inheritance_diagram')
extensions.append('sphinx.ext.autodoc.typehints')
extensions.append('sphinx.ext.autodoc')

autodoc_typehints = 'description'

autoapi_modules = {'rna_library': 
                                {
                                    'override': True
                                    },
									'rna_library.core': {'override':True},
									'rna_library.design': {'override':True},
									'rna_library.structure': {'override':True},
									'rna_library.processing': {'override':True},
        }
suppress_warnings = ['autoapi', 'all',
'duplicate.object',
'autosectionlabel.*',
"app.add_node",
"app.add_directive",
"app.add_role",
"app.add_generic_role",
"app.add_source_parser",
"download.not_readable",
"image.not_readable",
"ref.term",
"ref.ref",
"ref.numref",
"ref.keyword",
"ref.option",
"ref.citation",
"ref.footnote",
"ref.doc",
"ref.python",
"misc.highlighting_failure",
"toc.circular",
"toc.secnum",
"epub.unknown_project_files",
"epub.duplicated_toc_entry"]
autoapi_type = 'python'
autoapi_dirs = ['../rna_library/']
autoapi_options = ['members',
        'undoc-members', 'private-members', 'show-inheritance',
        'show-module-summary',
        'special-members', 'imported-members']
autoapi_options.append('members')
autoapi_options.append('show-inheritance-diagram')
autoapi_options.append('show-module-summary')

#autoapi_options = [ 'show-inheritance-diagram']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

