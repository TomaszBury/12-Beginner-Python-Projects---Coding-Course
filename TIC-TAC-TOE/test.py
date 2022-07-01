import random

board = [random.randint(1, 9) for _ in range(9)]

# for row in [self.board[i*3:(i+1)*3] for i in range(3)]:

# for row in [board[i*3:(i+1)*3] for i in range(3)]:
#     print(row)

print('\n')
k = 0
for row in [board[i*3:(i+1)*3] for i in range(3)]:
    print(f'{row[0]} | {row[1]} | {row[2]}')
    if k == 0 or k == 1:
        print('---------')
        k += 1

#board[4] = ' '
used_board = [' ' if k % random.randint(1, 9) == 0 else k for k in board]


def available_moves():
    # returns []
    return [i for i, spot in enumerate(used_board) if spot == ' ']
    # moves = []


print('\n')
print(available_moves())
print('\n')
k = 0
for row in [used_board[i*3:(i+1)*3] for i in range(3)]:
    print(f'{row[0]} | {row[1]} | {row[2]}')
    if k == 0 or k == 1:
        print('---------')
        k += 1
