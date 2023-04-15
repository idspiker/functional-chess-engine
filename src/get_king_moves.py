def get_king_moves(board, index):
    moves = (-1, -9, -8, -7, 1, 9, 8, 7)

    possible_movement = tuple(
        filter(lambda move: check_move(board, index, move), moves)
    )

    return tuple(map(lambda move: index + move, possible_movement))


def check_move(board, index, move):
    if check_for_edge(index, move):
        return False

    if board[index + move][2] == board[index][2]:
        return False

    if check_for_danger(board, index, move):
        return False
    
    return True


def check_for_edge(index, movement):
    # Check left
    if index % 8 == 0 and movement in (-1, -9, 7):
        return True

    # Check right
    if index % 8 == 7 and movement in (1, -7, 9):
        return True

    # Check top
    if index < 8 and movement in (-9, -8, -7):
        return True

    # Check bottom
    if index > 55 and movement in (7, 8, 9):
        return True

    return False


def check_for_danger(board, index, movement):
    return False


def check_direction_for_danger(board, index, offset, team, steps=0):
    pass


def check_for_knight(board, index, movement, offset):
    pass
