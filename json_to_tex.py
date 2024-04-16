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

def render_to_tex(template_path, data):
    with open(template_path, 'r') as file:
        template = Template(file.read(),
                            lstrip_blocks=True, 
                            trim_blocks=True)
    return template.render(data)

skills = open_json_file('data/skills.json')
experience = open_json_file('data/experience.json')
software = open_json_file('data/projects.json')
education = open_json_file('data/education.json')
writing = open_json_file('data/writing.json')


skills_output = render_to_tex('j2/skills.tex.j2', data = {'data' : skills['content']})
save_tex_file('output/skills.tex', skills_output)

experience_output = render_to_tex('j2/experience.tex.j2', data = {'data' : experience['content']})
save_tex_file('output/experience.tex', experience_output)

software_output = render_to_tex('j2/software.tex.j2', data = {'data' : software['content']})
save_tex_file('output/projects.tex', software_output)

education_output = render_to_tex('j2/education.tex.j2', data = {'data' : education['content']})
save_tex_file('output/education.tex', education_output)

writing_output = render_to_tex('j2/writing.tex.j2', data = {'data' : writing['content']})
save_tex_file('output/writing.tex', writing_output)