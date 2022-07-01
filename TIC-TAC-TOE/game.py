from shutil import move


class TicTacToe:
    def __init__(self):
        # single list to represent 3x3 board
        self.board = [' ' for _ in range(9)]
        # keep track of winner
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' .join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (Tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | ' .join(row) + ' |')

    def available_moves(self):
        # returns []
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'x')]
        #     if spot == ' ':
        #         moves.append(i)

        # return moves
