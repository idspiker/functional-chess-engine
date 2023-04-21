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

    if index < 8:
        return moves

    # Check forward
    if board[index - 8].occupant_team == 0:
        moves = (*moves, index - 8)

    # Check diagonals
    if index % 8 != 0 and board[index - 9].occupant_team == 2:
        moves = (*moves, index - 9)
    if (index + 1) % 8 != 0 and board[index - 7].occupant_team == 2:
        moves = (*moves, index - 7)

    # Check double forward
    if (index - 8 < 8 
        or board[index - 8].occupant_team != 0 
        or board[index].has_moved == True):
        return moves

    if board[index - 16].occupant_team == 0:
        moves = (*moves, index - 16)

    return moves


def get_black_moves(board, index):
    moves = tuple()

    if index > 55:
        return moves

    # Check forward
    if board[index + 8].occupant_team == 0:
        moves = (*moves, index + 8)

    # Check diagonals
    if index % 8 != 0 and board[index + 7].occupant_team == 1:
        moves = (*moves, index + 7)
    if (index + 1) % 8 != 0 and board[index + 9].occupant_team == 1:
        moves = (*moves, index + 9)

    # Check double forward
    if (index + 8 > 55 
        or board[index + 8].occupant_team != 0 
        or board[index].has_moved == True):
        return moves

    if board[index + 16].occupant_team == 0:
        moves = (*moves, index + 16)

    return moves