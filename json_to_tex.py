import json
from jinja2 import Template

def open_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_tex_file(file_path, tex_string):
    with open(file_path, 'w') as file:
        file.write(tex_string)
    return

def parse_json(json_string):
    data = json.loads(json_string)
    return data

skills = open_json_file('data/skills.json')
experience = open_json_file('data/experience.json')
software = open_json_file('data/projects.json')

def render_to_tex(template_path, data):
    with open(template_path, 'r') as file:
        template = Template(file.read())
    return template.render(data)

skills_output = render_to_tex('j2/skills.tex.j2', data = {'data' : skills['content']})
save_tex_file('output/skills.tex', skills_output)

experience_output = render_to_tex('j2/experience.tex.j2', data = {'data' : experience['content']})
save_tex_file('output/experience.tex', experience_output)

software_output = render_to_tex('j2/software.tex.j2', data = {'data' : software['content']})
save_tex_file('output/projects.tex', software_output)