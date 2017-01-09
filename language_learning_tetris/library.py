import random

sentences = [
['bonne', 'chance'],
['bonne', 'annee']
]

def get_word():
    sentence = sentences[random.randint(0,(len(sentences)-1))]
    word = sentence[random.randint(0,(len(sentence)-1))]
    return word
