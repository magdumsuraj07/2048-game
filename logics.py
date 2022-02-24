from random import randint


# Constants
ROW_COUNT = 4
COL_COUNT = 4
CONST_VALUE_2 = 2
CONST_VALUE_2048 = 2048
GAME_STATE_WON = "WON"
GAME_STATE_NOTOVER = "GAME NOT OVER"
GAME_STATE_LOST = "LOST"


def start_game():
    """
    Initialize the game with 4x4 matrix. Initially all values will be 0.
    """
    matrix = [[0 for c in range(COL_COUNT)] for r in range(ROW_COUNT)]
    return matrix


def add_new_2(mat):
    """
    Find empty position in matrix and add value '2' at that position.
    """
    row = randint(0, ROW_COUNT-1)
    col = randint(0, COL_COUNT-1)
    while (mat[row][col] != 0):
        row = randint(0, ROW_COUNT-1)
        col = randint(0, COL_COUNT-1)
    mat[row][col] = CONST_VALUE_2


def compress(mat):
    """
    Push all non zero values to left.
    """
    new_mat = [[0 for c in range(COL_COUNT)] for r in range(ROW_COUNT)]

    for r in range(ROW_COUNT):
        pos = 0
        for c in range(COL_COUNT):
            if (mat[r][c] != 0):
                new_mat[r][pos] = mat[r][c]
                pos += 1
    return new_mat


def get_current_state(mat):
    """
    Returns the current state of game. Either WON or NOT_OVER or LOST
    """

    # Check if at any position there is value 2048
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if (mat[r][c] == CONST_VALUE_2048):
                return GAME_STATE_WON
    
    # Check if there are any empty positions
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if (mat[r][c] == 0):
                return GAME_STATE_NOTOVER

    # Empty positions are not there, but check if there is any movement possible.
    # Excluding last row and col as it can lead to out of bound.
    for r in range(ROW_COUNT-1):
        for c in range(COL_COUNT-1):
            if (mat[r][c] == mat[r+1][c] or mat[r][c] == mat[r][c+1]):
                return GAME_STATE_NOTOVER

    # Check for last row
    for c in range(COL_COUNT-1):
        if (mat[ROW_COUNT-1][c] == mat[ROW_COUNT-1][c+1]):
            return GAME_STATE_NOTOVER
    
    # Check for last col
    for r in range(ROW_COUNT-1):
        if (mat[r][COL_COUNT-1] == mat[r+1][COL_COUNT-1]):
            return GAME_STATE_NOTOVER
    
    return GAME_STATE_LOST