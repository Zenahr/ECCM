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
        result += lookUpChord(chord) + "\n\n"
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

chordStream = "Am7 D9 Gmaj7"
chord = "Am7"
# print(lookUpChord(chord))
print(chordBuilder(chordStream))
