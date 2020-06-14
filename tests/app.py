dataset = {
    "inputVerification": [
    "",
    " ",
    "&", # stop when non alphanumerical values are read from inputStream
    "  1123josbiosdcio!!! ", # non AlphaNum check should catch again
    "Gmaj7",
    "GM7",
    "G7"
    ],

    "chordIdentification": [
        {
        "GM7": [
            "GM7",
            "Gmaj7",
            "GM",
            "Gmaj",
        ],
        "DM7": [
            # Alias
        ],
        "F#7(b13)": [
            # Alias
        ],
        "C#7(#9)": [
            # Alias
        ],
        
        "A13": [
            # Alias
        ],
        "B7": [
            # Alias
        ],
        "Em9": [
            # Alias
        ],
        "Bm9": [
            # Alias
        ],

        }
    ]
}

""""Assert stuff as follows

chordNotationPairer()
------------------------------------------------------
I -> "Gmaj7"
Assert O to be ->
"('Gmaj7', '355433')
"
------------------------------------------------------

numericNocationBuilder(input):
input = F#7(b13) Em9 Dmaj7(9) C#7(#9) Bm9 A13 B7(9)
Assert O ->

"Gmaj7=355433\n
...
Em9=______\n
...
B7(9)=______
"

"""