from random import random


import random


def play():
    user = input(
        'Choose a weapon: (R) for rock, (P) for paper, (S) for scissors.').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Draw'

    if is_win(user_hand=user, computer_hand=computer):
        return 'User has won.'

    return 'Comuter has bested you.'


def is_win(user_hand, computer_hand):
    # returns True if user wins
    # rules
    # r > s, s > p, p >r

    if (user_hand == 'r' and computer_hand == 's') or (user_hand == 's' and computer_hand == 'p') or (user_hand == 'p' and computer_hand == 'r'):
        return True
    else:
        return False


print(play())
