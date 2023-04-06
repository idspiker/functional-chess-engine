def get_pawn_moves(board, index):
    team = board[index][2]

    moves = tuple()

    # Check for white team
    if team == 1:
        moves = get_white_moves(board, index)

    # Check for black team
    elif team == 2:
        moves = get_black_moves(board, index)

    return moves


def get_white_moves(board, index):
    moves = tuple()

    if index < 8:
        return moves

    # Check forward
    if board[index - 8][2] == 0:
        moves = (*moves, index - 8)

    # Check diagonals
    if index % 8 != 0 and board[index - 9][2] == 2:
        moves = (*moves, index - 9)
    if (index + 1) % 8 != 0 and board[index - 7][2] == 2:
        moves = (*moves, index - 7)

    # Check double forward
    if index - 8 < 8 or board[index - 8][2] != 0 or board[index][4] == True:
        return moves

    if board[index - 16][2] == 0:
        moves = (*moves, index - 16)

    return moves


def get_black_moves(board, index):
    moves = tuple()

    if index > 63:
        return moves

    # Check forward
    if board[index + 8][2] == 0:
        moves = (*moves, index + 8)

    # Check diagonals
    if index % 8 != 0 and board[index + 7][2] == 1:
        moves = (*moves, index + 7)
    if (index + 1) % 8 != 0 and board[index + 9][2] == 1:
        moves = (*moves, index + 9)

    # Check double forward
    if index + 8 > 55 or board[index + 8][2] != 0 or board[index][4] == True:
        return moves

    if board[index + 16][2] == 0:
        moves = (*moves, index + 16)

    return moves