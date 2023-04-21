from check_moves import enemy_check


def get_pawn_moves(board, index):
    return (
        get_white_moves(board, index)
        if (team := board[index].occupant_team) == 1
            else get_black_moves(board, index)
            if team == 2
                else tuple()
    )


def get_white_moves(board, index):
    moves = tuple()
    
    if check_forward(board, index, -8, lambda i: i < 8):
        moves = (*moves, index - 8)

    if check_double_forward(board, index, -8, lambda i: i < 8):
        moves = (*moves, index - 16)

    if check_left_diagonal(board, index, -9):
        moves = (*moves, index - 9)
        
    if check_right_diagonal(board, index, -7):
        moves = (*moves, index - 7)

    return moves


def get_black_moves(board, index):
    moves = tuple()

    if check_forward(board, index, 8, lambda i: i > 55):
        moves = (*moves, index + 8)

    if check_double_forward(board, index, 8, lambda i: i > 55):
        moves = (*moves, index + 16)

    if check_left_diagonal(board, index, 7):
        moves = (*moves, index + 7)

    if check_right_diagonal(board, index, 9):
        moves = (*moves, index + 9)

    return moves


def check_forward(board, index, offset, edge_check):
    return not edge_check(index) and board[index + offset].occupant_team == 0


def check_double_forward(board, index, offset, edge_check):
    return (
        not edge_check(index + offset) 
        and board[index].has_moved == False
        and board[index + offset].occupant_team == 0
        and board[index + offset * 2].occupant_team == 0
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

