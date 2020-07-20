import os
import markdown
from jinja2 import Template
import sys

def generate_site(content_dir='content', output_dir='output', template_file='templates/base.html'):
    # Load the template
    with open(template_file) as f:
        template = Template(f.read())

    # Process each markdown file in the content directory
    for markdown_file in os.listdir(content_dir):
        with open(f'{content_dir}/{markdown_file}') as f:
            content = markdown.markdown(f.read())

        # Generate the final HTML
        title = markdown_file.replace('.md', '').capitalize()
        output = template.render(title=title, content=content)

        # Write the output to a file
        output_file = f'{output_dir}/{markdown_file.replace(".md", ".html")}'
        with open(output_file, 'w') as f:
            f.write(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        content_dir = sys.argv[1]
    else:
        content_dir = 'content'

    generate_site(content_dir=content_dir)
