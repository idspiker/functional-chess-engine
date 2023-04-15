def get_knight_moves(board, index):
    moves = (-17, -15, -10, -6, 6, 10, 15, 17)

    possible_movement = tuple(
        filter(lambda move: check_move(board, index, move), moves)
    )

    return tuple(map(lambda move: index + move, possible_movement))


def check_move(board, index, movement):
    # Return true if valid, false else
    if check_for_edge(index, movement):
        return False

    if board[index + movement].occupant_team == board[index].occupant_team:
        return False

    return True


def check_for_edge(index, movement):
    # Check if move will take the piece over the edge of board
    
    # Check left side
    if index % 8 < 2 and movement in (-17, -10, 6, 15):
        if index % 8 != 1 or movement not in (-17, 15):
            return True

    # Check right side
    if index % 8 > 5 and movement in (-15, -6, 10, 17):
        if index % 8 != 6 or movement not in (-15, 17):
            return True

    # Check top
    if index < 16 and movement in (-10, -17, -15, -6):
        if index <= 7 or movement not in (-10, -6):
            return True

    # Check bottom
    if index > 47 and movement in (6, 15, 17, 10):
        if index >= 56 or movement not in (6, 10):
            return True
    
    return False
