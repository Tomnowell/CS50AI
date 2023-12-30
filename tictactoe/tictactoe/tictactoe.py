"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count, o_count = 0, 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <=  o_count:
        return X
    else:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append([i, j])
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    next_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = next_player
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.

    Checks the 3x3 grid and returns X 
    if there are 3 X's in a row, column, or diagonal. 
    And O if there are 3 O's in a row, column, or diagonal.
    """
    # Check rows:
    for row in board:
        if all([cell == X for cell in row]):
            return X
        elif all([cell == O for cell in row]):
            return O
        else:
            continue

    # Check columns:
    for i in range(3):
        if all([board[j][i] == X for j in range(3)]):
            return X
        elif all([board[j][i] == O for j in range(3)]):
            return O
        else:
            continue
    
    # Check diagonals
    for i in range(3):
        if all([board[i][i] == X for i in range(3)]):
            return X
        elif all([board[i][2-i] == X for i in range(3)]):
            return X
        elif all([board[i][i] == O for i in range(3)]):
            return O
        elif all([board[i][2-i] == O for i in range(3)]):
            return O
        else:
            continue
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not any(EMPTY in row for row in board):
        return True
    elif winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0

def minimax(board):
    """
    Recursively returns the optimal action for the current player on the board.
    """

    # Base case
    if terminal(board):
        return None

    # Recursive case
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            new_v = max(v, min_value(result(board, action)))
            if new_v > v:
                v = new_v
                optimal_action = action

    else:
        v = math.inf
        for action in actions(board):
            new_v = min(v, max_value(result(board, action)))
            if new_v < v:
                v = new_v
                optimal_action = action
    return optimal_action
    
def max_value(board):
    """
    Returns the maximum value of the possible moves.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Returns the minimum value of the possible moves.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
