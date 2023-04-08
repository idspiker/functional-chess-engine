from check_directions import check_diagonal


def get_bishop_moves(board, index):
    return (
        *check_diagonal(board, index, 'ul', board[index][2]),
        *check_diagonal(board, index, 'ur', board[index][2]),
        *check_diagonal(board, index, 'dl', board[index][2]),
        *check_diagonal(board, index, 'dr', board[index][2])
    )