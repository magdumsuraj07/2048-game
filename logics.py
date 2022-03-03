from random import randint
from constants import ROW_COUNT, COL_COUNT, CONST_VALUE_2, CONST_VALUE_2048
from constants import GAME_STATE_WON, GAME_STATE_LOST, GAME_STATE_NOTOVER


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
    grid_changed = False  # Flag to track if grid is changed
    new_mat = [[0 for c in range(COL_COUNT)] for r in range(ROW_COUNT)]

    for r in range(ROW_COUNT):
        pos = 0
        for c in range(COL_COUNT):
            if (mat[r][c] != 0):
                new_mat[r][pos] = mat[r][c]
                if (pos != c):
                    grid_changed = True
                pos += 1
    return new_mat, grid_changed


def merge(mat):
    """
    Merge the adjacent cell's if they have same value
    """
    grid_changed = False  # Flag to track if grid is changed
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT-1):
            if (mat[r][c] == mat[r][c+1] and mat[r][c] != 0):
                mat[r][c] *= 2
                mat[r][c+1] = 0
                grid_changed = True
    return mat, grid_changed


def reverse(mat):
    """
    Reverse a matrix
    """
    for r in range(ROW_COUNT):
        mat[r].reverse()
    return mat


def transpose(mat):
    """
    Transpose a matrix
    """
    new_mat = [[0 for c in range(COL_COUNT)] for r in range(ROW_COUNT)]
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            new_mat[r][c] = mat[c][r]
    return new_mat


def move_left(grid):
    """
    Perform left move operation on grid
    """
    grid, grid_changed_compress = compress(grid)
    grid, grid_changed_merge = merge(grid)
    is_grid_changed = grid_changed_compress or grid_changed_merge
    grid, temp = compress(grid)
    return grid, is_grid_changed


def move_right(grid):
    """
    Perform right move operation on grid
    """
    grid = reverse(grid)
    grid, grid_changed_compress = compress(grid)
    grid, grid_changed_merge = merge(grid)
    is_grid_changed = grid_changed_compress or grid_changed_merge
    grid, temp = compress(grid)
    grid = reverse(grid)
    return grid, is_grid_changed


def move_up(grid):
    """
    Perform up move operation on grid
    """
    grid = transpose(grid)
    grid, grid_changed_compress = compress(grid)
    grid, grid_changed_merge = merge(grid)
    is_grid_changed = grid_changed_compress or grid_changed_merge
    grid, temp = compress(grid)
    grid = transpose(grid)
    return grid, is_grid_changed


def move_down(grid):
    """
    Perform down move operation on grid
    """
    grid = transpose(grid)
    grid = reverse(grid)
    grid, grid_changed_compress = compress(grid)
    grid, grid_changed_merge = merge(grid)
    is_grid_changed = grid_changed_compress or grid_changed_merge
    grid, temp = compress(grid)
    grid = reverse(grid)
    grid = transpose(grid)
    return grid, is_grid_changed


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

    # Empty positions are not there, check if there is any movement possible.
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
