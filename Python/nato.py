import sys

nato_alphabet = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliet',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu'
}

# Ask the user to enter a String



word = str(input("Enter Your Word: "))
print("\n>> Converting Word using NATO Phonetic Alphabet...\n")
print ("\n...")
print ("\n")

for i in word:
    if i.lower() in nato_alphabet.keys(): #lower function pulls up lower case terms that are defined. key() returns a view object.
        print(nato_alphabet[i.lower()])


# for word match the letters to the word and spell them out
