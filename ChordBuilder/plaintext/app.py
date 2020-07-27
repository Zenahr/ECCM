"""
Numeric Chord Notation
"""



#   StringToChordChart:: String -> Bool -> String
def StringToChordChart(chordNames, sort):
"""
Scenario:
chordNames ≝ "GM7 F#7b13 Em9 A13 DM9 C#7#9 Bm9 B9"

Return a dict like so:
dict({
    GM7: 'xxxxxx',
    ...
    B9: 'xxxxxx'
})
"""
    pass


def chordNotationPairer(chordName):
    """Finds the right numeric chord notation and returns a tuple of (chordName, notation)

    Args:
        chordName (string): Example: GM7
    
    Return:
        Example:
            I -> Cm9
            O -> ('Cm9', 'x3x133x')
    """

    if (normaliseChordName) == 'Gmaj7'):
        return ('Gmaj7', '355433')

    elif (normaliseChordName) == 'Dmaj7'):
        return ('Dmaj7', 'x57675')

    elif (normaliseChordName) == 'F#7b13'):
        return ('F#7b13', 'x57675')

    elif (normaliseChordName) == 'C#7#9'):
        return ('C#7#9', 'x57675')

    elif (normaliseChordName) == 'A13'):
        return ('A13', 'x57675')

    elif (normaliseChordName) == 'B79'):
        return ('B79', 'x57675')

    elif (normaliseChordName) == 'Em9'):
        return ('Em9', 'x57675')

    elif (normaliseChordName) == 'Bm9'):
        return ('Bm9', 'x57675')

def normaliseChordName(chordName):
    chordName = chordName.replace('(', '')
    chordName = chordName.replace(')', '')
    return chordName

def rowBuilder(tuple):
    chordName = tuple[0]
    chordNotation = tuple[1]
    return chordName + ": " + chordNotation + '\n' # add support for unix-systems later.

def stringBuilder(chordStreamTuples):
    string = ''
    string.join([for (chordName, chordNotation) in chordStream, rowBuilder(chordName, chordNotation)]) # -> [[row], ..., [row]]

def numericNocationBuilder(userInput):
    chordStream = inputDissector(userInput) # Create list of chord names by seperating string into items via " " or "," or ", " delimeter.
    chordStream = chordStreamFeeder(chordStream, chordNotationPairer()) # Callback function mapping every entry of the chordStream list to the callback function.
    chordStream = stringBuilder(chordStream) # chordStream -> [(chordName, chordNotation)] -> String with carriage returns.
    return chordStream

userInput = "GM7 F#7b13 Em9 A13 DM9 C#7#9 Bm9 B9"
print(numericNotationBuilder(userInput))