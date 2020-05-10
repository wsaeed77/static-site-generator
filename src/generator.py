import os
import markdown
from jinja2 import Template

# Load the template
with open('templates/base.html') as f:
    template = Template(f.read())

# Read the markdown content
with open('content/index.md') as f:
    content = markdown.markdown(f.read())

# Generate the final HTML
output = template.render(title="Home", content=content)

# Write the output to a file
with open('output/index.html', 'w') as f:
    f.write(output)
