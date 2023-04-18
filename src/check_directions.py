from functools import reduce


from apply_functions import apply_functions


def check_direction(board, index, movement, team, moves=tuple()):
    if check_for_edge_block(index, movement) == True:
        return moves

    if board[index + movement].occupant_team == team:
        return moves

    if (board[index + movement].occupant_team != team 
        and board[index + movement].occupant_team != 0):
        return (*moves, index + movement)

    moves = (*moves, index + movement)

    return check_direction(
        board, 
        index + movement, 
        movement, 
        team,
        moves
    )


def check_diagonal(board, index, movement, team, moves=tuple()):
    if check_for_edge_block(index, movement) == True:
        return moves

    if board[index + movement].occupant_team == team:
        return moves

    if (board[index + movement].occupant_team != team 
        and board[index + movement].occupant_team != 0):
        return (*moves, index + movement)

    moves = (*moves, index + movement)

    return check_diagonal(
        board, 
        index + movement, 
        movement,
        team,
        moves
    )


def check_for_edge_block(index, movement):
    """Returns true if edge is blocking movement, else false"""
    return reduce(
        lambda x, y: x or y, 
        apply_functions(
            (
                check_left_edge, 
                check_right_edge, 
                check_top_edge, 
                check_bottom_edge
            ), 
            (index, movement)
        )
    )


def check_left_edge(index, movement):
    return index % 8 == 0 and movement in (-1, -9, 7)


def check_right_edge(index, movement):
    return index % 8 == 7 and movement in (1, -7, 9)


def check_top_edge(index, movement):
    return index < 8 and movement in (-8, -7, -9)


def check_bottom_edge(index, movement):
    return index > 55 and movement in (8, 7, 9)
