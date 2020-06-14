"""
Numeric Chord Notation
"""

def util_StringBuilder(chordChartRowList):


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


def notationFinder(chordName):
    """Finds the right numeric chord notation and returns a string

    Args:
        chordName (string): Example: GM7
    
    Return:
        Example:
            I -> Cm9
            O -> x3x133x
    """

    if (chordName == "")