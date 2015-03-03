# -*- coding: utf-8 -*-
#
# php-opencloud documentation build configuration file, created by
# sphinx-quickstart on Tue Mar  3 12:28:19 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

lexers['php'] = PhpLexer(startinline=True, linenos=1)
lexers['php-annotations'] = PhpLexer(startinline=True, linenos=1)
primary_domain = 'php'

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'php-opencloud'
copyright = u'2015, Jamie Hannaford, Shaunak Kashyap'
version = '1.12'
release = '1.12.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), "_templates"]

html_static_path = ['_static']
html_use_index = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'php-openclouddoc'

latex_documents = [
  ('index', 'php-opencloud.tex', u'php-opencloud Documentation',
   u'Jamie Hannaford, Shaunak Kashyap', 'manual'),
]

man_pages = [
    ('index', 'php-opencloud', u'php-opencloud Documentation',
     [u'Jamie Hannaford, Shaunak Kashyap'], 1)
]

texinfo_documents = [
  ('index', 'php-opencloud', u'php-opencloud Documentation',
   u'Jamie Hannaford, Shaunak Kashyap', 'php-opencloud', 'One line description of project.',
   'Miscellaneous'),
]
