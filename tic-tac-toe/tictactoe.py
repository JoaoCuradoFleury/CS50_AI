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
    count_x = 0
    count_o = 0

    # interate over the board and calculate how many x and o are there (i == lines, j == colums)
    for i in board:
        for j in i:
            if j == X:
                count_x += 1
            elif j == O:
                count_o += 1
    
    if count_x <= count_o:
        return X
    
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid action")
     
    y,x = action[0], action[1]

    board_copy = copy.deepcopy(board)
    board_copy[y][x] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check vertical lines
    for i in range(3):
        if((board[0][i] != EMPTY) and (board[0][i] == board[1][i] == board[2][i])):
            return board[0][i]

    # Check Horizontal lines
    for j in range(3):
        if((board[j][0] != EMPTY) and (board[j][0] == board[j][1] == board[j][2])):
            return board[j][0]

    # Check diogonal lines
    if((board[2][2] != EMPTY) and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]))):
        return board[1][1]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    if (EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]):
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

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board,action)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        #loop over the possible actions
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])

        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        plays = []
        #loop over the possible actions
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])

        return sorted(plays, key=lambda x: x[0])[0][1]
