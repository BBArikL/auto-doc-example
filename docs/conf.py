import sys
import os
import re
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PROJECT_NAME'
copyright = 'YEAR, AUTHOR#1, ... AUTHOR#N'
author = 'AUTHOR#1, ... AUTHOR#N'
release = 'REL_VER'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'breathe', 'sphinx.ext.autodoc', 'sphinx.ext.mathjax', 'myst_parser']

exclude_patterns = []

source_suffix = {'.rst': 'restructuredtext', '.md': 'restructuredtext', '.xml': 'restructuredtext'}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Breathe config
sys.path.append(Path("./breathe/"))
breathe_projects = {project: Path("./xml-dir/")}
breathe_show_include = False
breathe_default_project = project

# Add all source files to be generated and included by sphinx and breathe
sFiles = []
for f in os.listdir("../"):
    if re.match(".*\\.(cpp|h)", f):
        sFiles.append(Path(f))

breathe_projects_source = {project: ("../", sFiles)}

generated_files_folder = "code-doc"
if not os.path.exists(generated_files_folder):
    os.makedirs(generated_files_folder)

for sFile in sFiles:
    sFile = re.sub("\\.(cpp|h)", "", sFile.name)
    rst_file = f"{generated_files_folder}/{sFile.lower()}.rst"
    if not os.path.exists(rst_file):
        with open(rst_file, "w") as f:
            title = f"{sFile}"
            f.write(f"{title}\n{'='*len(title)}\n\n")

            if os.path.exists(f"../{sFile}.cpp"):
                f.write(f".. autodoxygenfile:: {sFile}.cpp\n   :project: {project}\n")
            f.write(f".. autodoxygenfile:: {sFile}.h\n   :project: {project}\n")