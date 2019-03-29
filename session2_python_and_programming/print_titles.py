import re
import nbformat


header_pattern = r'^\s*#\s+(.+)'

with open('slides_session2.ipynb') as f:
    notebook = nbformat.reads(f.read(), as_version=4)

for cell in notebook['cells']:
    if not cell['cell_type'] == 'markdown':
        continue
    headlines = re.findall(header_pattern, cell['source'], re.MULTILINE)
    if headlines:
        print("\n".join([headline.strip() for headline in headlines]))
