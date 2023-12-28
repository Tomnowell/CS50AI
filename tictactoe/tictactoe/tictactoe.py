"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    turn_count = x_count + o_count
    if turn_count == 0 or turn_count % 2 == 0:
        return X
    else:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    for i, j in enumerate(board):
        for k, l in enumerate(j):
            if l == EMPTY:
                yield i, k
            else:
                continue

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    next_player = player(board)
    i, j = action
    board[i][j] = next_player
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = utility(board)
    if winner == 1:
        return X
    elif winner == -1:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not any(EMPTY in row for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if any([all([cell == 'X' for cell in row]) for row in board]):
        return 1
    elif any([all([cell == 'O' for cell in row]) for row in board]):
        return -1
    else: 
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
