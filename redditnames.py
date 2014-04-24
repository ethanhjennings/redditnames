import json
import random
import string
from weighted_choice import weighted_choice

# Constants
# You can play around with these to get different looking usernames
_TWO_WORDS_CHANCE = 0.7
_THREE_WORDS_CHANCE = 0.3
_LETTERS_RANGE = (2,4)
_DIGITS_RANGE = (2,3)
_BINARY_DIGITS_RANGE = (6,16)
_UNDERSCORE_CHANCE = 0.13
_DASH_CHANCE = 0.05
_NO_SEPARATOR_CHANCE = 1.0 - _UNDERSCORE_CHANCE - _DASH_CHANCE
_BEGINNING_SEPARATOR_CHANCE = 0.1
_END_SEPARATOR_CHANCE = 0.1
_CAPITALIZE_FIRST_CHANCE = 0.4
_CAPITALIZE_ALL_CHANCE = 0.05
_CAPITALIZE_NONE_CHANCE = 1.0 - _CAPITALIZE_FIRST_CHANCE - _CAPITALIZE_ALL_CHANCE


words = json.load(open("words.json"))

def _getSeparator():
    return weighted_choice([
            ("_",_UNDERSCORE_CHANCE),
            ("-",_DASH_CHANCE),
            ("",_NO_SEPARATOR_CHANCE)])

def _capitalize(val):
    return weighted_choice([
            (val.title(),_CAPITALIZE_FIRST_CHANCE),
            (val.upper(),_CAPITALIZE_ALL_CHANCE),
            (val.lower(),_CAPITALIZE_NONE_CHANCE)])

def wordUsername():
    separator = _getSeparator()
    numWords = weighted_choice([
                (2,_TWO_WORDS_CHANCE),
                (3,_THREE_WORDS_CHANCE)])

    # choose numWords words, one from each word array, in the same order of the arrays
    wordArrays = [words['prefixAdjectives'],words['middleNouns'],words['suffixAdjectives']]
    chosenWords = [random.choice(wordArrays[index]) for index in sorted(random.sample(range(0,3),numWords))]
    
    username = separator.join(_capitalize(word) for word in chosenWords)
    return username
        
    

def initialsUsername():
    numLetters = random.randint(_LETTERS_RANGE[0],_LETTERS_RANGE[1])
    numDigits = random.randint(_DIGITS_RANGE[0],_DIGITS_RANGE[1])
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(numLetters))
    letters = _capitalize(letters)
    
    numbers = ''.join(random.choice(string.digits) for _ in range(numDigits))
    return letters + _getSeparator() + numbers

def binaryUsername():
    numDigits = random.randint(_BINARY_DIGITS_RANGE[0],_BINARY_DIGITS_RANGE[1])
    return ''.join(random.choice(['0','1']) for _ in range(numDigits))

def generateRandom():
    nameMode = weighted_choice([(initialsUsername,0.18),(wordUsername,0.8),(binaryUsername,0.02)])
    return nameMode()

if __name__ == "__main__":
    print generateRandom()
