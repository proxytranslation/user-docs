project = u'Translation Proxy Documentation'
extensions = ["myst_parser"]
copyright = u'2024'
source_suffix = ['.rst', '.md']		
master_doc = 'index'
version = 'latest'
release = 'latest'

# Compare the two
# html_theme = 'proxytheme'
html_theme = 'sphinx_rtd_theme'


htmlhelp_basename = 'easyling-wiki-docs'
html_theme_path = ["."]
latex_documents = [
  ('index', 'easyling-wiki-docs.tex', u'Translation Proxy Online Documentation',
   u'', 'manual'),
]
