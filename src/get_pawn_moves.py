from check_moves import enemy_check
from utility_funcs import combine_on_condition
from field_enumerations import Team


def get_pawn_moves(board, index):
    return (
        get_white_moves(board, index)
        if (team := board[index].occupant_team) is Team.WHITE
            else get_black_moves(board, index)
            if team is Team.BLACK
                else tuple()
    )


def get_white_moves(board, index):
    return combine_on_condition(
        (index - 8, check_forward(board, index, -8, lambda i: i < 8)),
        (index - 16, check_double_forward(board, index, -8, lambda i: i < 8)),
        (index - 9, check_left_diagonal(board, index, -9)),
        (index - 7, check_right_diagonal(board, index, -7))
    )


def get_black_moves(board, index):
    return combine_on_condition(
        (index + 8, check_forward(board, index, 8, lambda i: i > 55)),
        (index + 16, check_double_forward(board, index, 8, lambda i: i > 55)),
        (index + 7, check_left_diagonal(board, index, 7)),
        (index + 9, check_right_diagonal(board, index, 9))
    )


def check_forward(board, index, offset, edge_check):
    return (
        not edge_check(index) 
        and board[index + offset].occupant_team is Team.EMPTY
    )


def check_double_forward(board, index, offset, edge_check):
    return (
        not edge_check(index + offset) 
        and board[index].has_moved == False
        and board[index + offset].occupant_team is Team.EMPTY
        and board[index + offset * 2].occupant_team is Team.EMPTY
    )


def check_left_diagonal(board, index, offset):
    return (
        index % 8 != 0 
        and enemy_check(board, index, offset, board[index].occupant_team)
    )


def check_right_diagonal(board, index, offset):
    return (
        index % 8 != 7
        and enemy_check(board, index, offset, board[index].occupant_team)
    )
