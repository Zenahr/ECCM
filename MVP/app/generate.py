from jinja2 import Environment, FileSystemLoader
from json import load
import yaml

chordDelimeter = "\r\n"


def chordBuilder(chord_stream):
    """
    Splits input into seperate chords and returns numeric chord diagram for each chord. Returns string
    """
    result = ""
    split_stream = chord_stream.split()
    result = chordBuilderHelper(split_stream)
    return result

def chordBuilderHelper(split_stream):
    result = ""
    for chord in split_stream:
        result += lookUpChord(chord) + chordDelimeter
    return result

def lookUpChord(chordName, delimeter="::"):
    lookUpTable = {
        "Am7": "5x555x",
        "D9": "x5455x",
        "Gmaj7": "3x443x",
    }
    if chordName in lookUpTable:
        return chordName + delimeter + lookUpTable[chordName] # Example --> Am7::5x555x
    else:
        return "N/A"



template_env = Environment(loader=FileSystemLoader(searchpath='./templates'))
template = template_env.get_template('template.txt')

with open('templates/song.yaml', 'r') as song_file:
    song = yaml.load(song_file)

with open('output/' + song['songTitle'] + '.txt', 'w') as output_file:
    output_file.write(
        template.render(
            songTitle=song['songTitle'],
            chords=chordBuilder(song['chords']),
        )
    )

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
