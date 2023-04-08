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


def check_diagonal(board, index, direction, team, movement=0, moves=tuple()):
    if movement == 0:
        movement = get_movement_from_direction(direction)

    if check_for_edge_block(index, movement) == True:
        return moves

    if board[index + movement][2] == team:
        return moves

    if board[index + movement][2] != team and board[index + movement][2] != 0:
        return (*moves, index + movement)

    moves = (*moves, index + movement)

    return check_diagonal(
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
    elif direction == 'ul':
        return -9
    elif direction == 'ur':
        return -7
    elif direction == 'dl':
        return 7
    elif direction == 'dr':
        return 9
    else:
        raise Exception(f'"{direction}" is not a valid direction')


def check_for_edge_block(index, movement):
    """Returns true if edge is blocking movement, else false"""
    left_edge_move = movement == -1 or movement == -9 or movement == 7
    right_edge_move = movement == 1 or movement == -7 or movement == 9
    top_edge_move = movement == -8 or movement == -7 or movement == -9
    bottom_edge_move = movement == 8 or movement == 7 or movement == 9

    if index % 8 == 0 and left_edge_move:
        return True
    elif (index + 1) % 8 == 0 and right_edge_move:
        return True
    elif index < 8 and top_edge_move:
        return True
    elif index > 55 and bottom_edge_move:
        return True

    return False