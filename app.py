"""
Custom Datatypes: Row, Chord

Row ≔ Object with components ⟹ stringName(E,A,D,G,B,e or 1,2,3,4,5,6), Style(symbol, delimeter), State(neutral, open, closed), Note(fretNumber, fingerNumber)

"""

def rowBuilder(stringName, Style, Note, state):
    """Creates a tablature row
    E ───|─X─|───|───|───|─── ⦿/〇/✕
    Args:
        stringName ([type]): [description]
        Note ([type]): [description]
        state ([type]): [description]

e ───|─X─|───|───|───|───
B ───|─X─|───|───|───|───
G ───|───|─X─|───|───|───
D ───|───|───|─X─|───|───
A ───|───|───|─X─|───|───
E ───|─X─|───|───|───|───

e ───|─1─|───|───|───|─── 〇
B ───|─1─|───|───|───|─── 〇
G ───|───|─2─|───|───|─── 〇
D ───|───|───|─4─|───|─── 〇
A ───|───|───|─3─|───|─── 〇
E ───|─1─|───|───|───|─── ⨀
    """
    pass