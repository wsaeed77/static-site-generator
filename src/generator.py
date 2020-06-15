import os
import markdown
from jinja2 import Template

# Load the template
with open('templates/base.html') as f:
    template = Template(f.read())

# Process each markdown file in the content directory
for markdown_file in os.listdir('content'):
    with open(f'content/{markdown_file}') as f:
        content = markdown.markdown(f.read())

    # Generate the final HTML
    title = markdown_file.replace('.md', '').capitalize()
    output = template.render(title=title, content=content)

    # Write the output to a file
    output_file = f'output/{markdown_file.replace(".md", ".html")}'
    with open(output_file, 'w') as f:
        f.write(output)
