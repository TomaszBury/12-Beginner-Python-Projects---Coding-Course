import random
import string
from words import words

alpahabet_lowercase = [c for c in string.ascii_lowercase]


def get_valid_word(words):
    word = random.choice(words)
    for char in word:
        if char not in alpahabet_lowercase:
            word = random.choice(words)

    return word.lower()


def hangman():
    word = get_valid_word(words)
    # print(word) <-- for debugging purposes.
    # set of letters
    # Set items are unordered, unchangeable, and do not allow duplicate values.
    word_letters = set(word)
    alpahabet = set(string.ascii_lowercase)
    # what the user has guessed
    used_letters = set()

    lives = len(word)

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left, letters used: ',
              ' '.join(used_letters))

        # what current word is
        word_list = [char if char in used_letters else '_' for char in word]
        print('Current wrod: ', ' '.join(word_list))

        user_letter = input('Guess a tetter: ').lower()
        if user_letter in alpahabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character, try again.')
        else:
            print('Invalid character. Please try again.')

    # when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(f'You have died, sorry not sorry. Thge word was: {word}')
    else:
        print(f'God game! Word: {word}')


# user_input = input('Type something: ')
# print(user_input)
hangman()
