from check_moves import check_moves


def get_bishop_moves(board, index):
    return check_moves(board, index, (-9, -7, 9, 7))
