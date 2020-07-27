
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
        return chordName + delimeter + lookUpTable[chordName] # Example --> Am7::5x555x
    else:
        return "N/A"


chord = "Am7"
print(lookUpChord(chord))