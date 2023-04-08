from check_directions import check_diagonal


def get_bishop_moves(board, index):
    team = board[index][2]

    return (
        *check_diagonal(board, index, 'ul', team),
        *check_diagonal(board, index, 'ur', team),
        *check_diagonal(board, index, 'dl', team),
        *check_diagonal(board, index, 'dr', team)
    )
    