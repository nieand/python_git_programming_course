"""Clear output of certain cells.

How to use: Run all cells (using run below for cells with exceptions), then run
this script and reload the page in the browser.
"""

import nbformat


FILE_NAME = 'slides_session2.ipynb'

with open(FILE_NAME) as f:
    notebook = nbformat.reads(f.read(), as_version=4)

for cell in notebook['cells']:
    metadata = cell['metadata']
    if 'outputs' in cell and 'tags' in metadata and 'clear' in metadata['tags']:
        cell['outputs'] = []

with open(FILE_NAME, 'w') as f:
    nbformat.write(notebook, f)
