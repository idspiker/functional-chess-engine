def get_rook_moves(board, index):
    return (
        *check_direction(board, index, 'r', board[index][2]), 
        *check_direction(board, index, 'l', board[index][2]), 
        *check_direction(board, index, 'u', board[index][2]), 
        *check_direction(board, index, 'd', board[index][2])
    )


def check_direction(board, index, direction, team, movement=0, moves=tuple()):
    if movement == 0:
        movement = get_movement_from_direction(direction)

    if check_for_edge_block(index, movement) == True:
        return moves

    if board[index + movement][2] == team:
        return moves

    if board[index + movement][2] != team and board[index + movement][2] != 0:
        return (*moves, index + movement)

    moves = (*moves, index + movement)

    return check_direction(
        board, 
        index + movement, 
        direction, 
        team, 
        movement, 
        moves
    )


def get_movement_from_direction(direction):
    if direction == 'r':
        return 1
    elif direction == 'l':
        return -1
    elif direction == 'u':
        return -8
    elif direction == 'd':
        return 8
    else:
        raise Exception(f'"{direction}" is not a valid direction')


def check_for_edge_block(index, movement):
    """Returns true if edge is blocking movement, else false"""
    if index % 8 == 0 and movement == -1: # Left edge
        return True
    if (index + 1) % 8 == 0 and movement == 1: # Right edge
        return True
    if index < 8 and movement == -8: # Top edge
        return True
    if index > 55 and movement == 8: # Bottom edge
        return True

    return False