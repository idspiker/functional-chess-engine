from check_moves import check_moves


def get_rook_moves(board, index):
    return check_moves(board, index, (1, -1, 8, -8))
