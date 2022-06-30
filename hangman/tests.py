from operator import ge
from random import random
import string
import random
from words import words
good_word = True


# print(type(string.ascii_lowercase))
alphabet = [c for c in string.ascii_lowercase]
# print(type(alphabet))


def get_valid_word(word):
    for char in word:
        # print(char)
        if char not in alphabet:
            return False

    return True


for word in words:
    if not get_valid_word(word):
        print(f'Test of: {word} is:{get_valid_word(word)}')
