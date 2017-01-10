import random
import math

sentences = [
['bonne', 'chance'],
['bonne', 'annee'],
['quelle', 'chance'],
['annee', 'prochaine'],
['une', 'annee'],
['une', 'chance']
]

def get_word():
    sentence = sentences[random.randint(0,(len(sentences)-1))]
    word = sentence[random.randint(0,(len(sentence)-1))]
    units = math.floor(len(word)/4)
    print word, 'LENGTH: ', len(word), 'UNITS: ', units
    return word, units

def check_if_sentence(block1, block2):
    for sentence in sentences:
        if sentence[0] == block1.word and sentence[1] == block2.word:
            return True
    return False
