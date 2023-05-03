from functools import partial

from utility_funcs import check_conditions, flatten
from field_enumerations import Team



def check_moves(board, index, directions):
    return flatten(
        map(
            partial(check_direction, board, index, board[index].occupant_team),
            directions
        )
    )


def check_direction(board, index, team, movement, moves=tuple()):
    return (
        moves 
        if hard_stop_check(board, index, movement, team)
            else (*moves, index + movement)
            if enemy_check(board, index, movement, team)
                else check_direction(
                    board, index + movement, 
                    team, movement, (*moves, index + movement)
                )
    )


def hard_stop_check(board, index, movement, team):
    return (
        check_for_edge_block(index, movement) 
        or teammate_check(board, index, movement, team)
    )


def teammate_check(board, index, movement, team):
    return board[index + movement].occupant_team is team


def enemy_check(board, index, movement, team):
    return (
        board[index + movement].occupant_team is not team 
        and board[index + movement].occupant_team is not Team.EMPTY
    )


def check_for_edge_block(index, movement):
    """Returns true if edge is blocking movement, else false"""
    return check_conditions(
        (check_left_edge, check_right_edge, check_top_edge, check_bottom_edge), 
        (index, movement)
    )


def check_left_edge(index, movement):
    return index % 8 == 0 and movement in (-1, -9, 7)


def check_right_edge(index, movement):
    return index % 8 == 7 and movement in (1, -7, 9)


def check_top_edge(index, movement):
    return index < 8 and movement in (-8, -7, -9)


def check_bottom_edge(index, movement):
    return index > 55 and movement in (8, 7, 9)
