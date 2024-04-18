import json
from jinja2 import Template

def open_json_file(file_path):
    """Open a json file and return the data as a dictionary."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def render_to_tex(template_path, data):
    """Render a jinja2 template to a tex string."""
    with open(template_path, 'r') as file:
        template = Template(file.read(),
                            lstrip_blocks=True, 
                            trim_blocks=True)
    return template.render(data)

def save_tex_file(file_path, tex_string):
    """Save a string to a tex file."""
    with open(file_path, 'w') as file:
        file.write(tex_string)
    return

def process_data(file_path, template_path):
    """Open a json file, render it to a tex string, and save it to a tex file."""
    data = open_json_file(file_path)
    output = render_to_tex(template_path, data={'data': data['content']})
    save_tex_file(f'output/{file_path.split("/")[-1].split(".")[0]}.tex', output)

process_data('data/skills.json', 'j2/skills.tex.j2')
process_data('data/experience.json', 'j2/experience.tex.j2')
process_data('data/projects.json', 'j2/software.tex.j2')
process_data('data/education.json', 'j2/education.tex.j2')
process_data('data/writing.json', 'j2/writing.tex.j2')