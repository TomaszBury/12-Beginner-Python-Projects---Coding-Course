from ast import Return
from logging.config import valid_ident
import math
import random

from numpy import square


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to het their nex move given a game
    def get_move(selft, game):
        pass


class RandomComputerPlayer(Player):
    def __init_(self, letter):
        super().__init_(letter)

    def get_move(selft, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init_(self, letter):
        super().__init_(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            # we're going to check that this is correct value by trying to cast
            # it to an integer, and if it's not. then we say its invalid
            # if that spot is not available on the board, we als say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                # if casting to in is successful we have number.
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
