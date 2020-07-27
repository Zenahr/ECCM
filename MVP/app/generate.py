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

def chordBuilder(chord_stream):
    """
    Splits input into seperate chords and returns numeric chord diagram for each chord. Returns string
    """
    result = ""
    split_stream = chord_stream.spilt()
    result = chordBuilderHelper(split_stream)

def chordBuilderHelper(split_stream):
    result = ""
    for chord in split_stream:
        chord = lookUpChord(chord)
    return split_stream

def lookUpChord(chordName, delimeter="::"):
    lookUpTable = {
        "Am7": "5x555x",
        "D9": "x5455x",
        "Gmaj7": "3x443x",
    }
    if chordName in lookUpTable:
        return chordName + delimeter + lookUpTable[chord]
    else:
        return "N/A"