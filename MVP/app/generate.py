from jinja2 import Environment, FileSystemLoader
from json import load
import yaml

template_env = Environment(loader=FileSystemLoader(searchpath='./template'))
template = template_env.get_template('template.txt')

with open('template/config.yaml', 'r') as config_file:
    config = yaml.load(config_file)

with open('output/song.txt', 'w') as output_file:
    output_file.write(
        template.render(
            songTitle=config['songTitle'],
            chords=chordBuilder(config['chords']),
        )
    )