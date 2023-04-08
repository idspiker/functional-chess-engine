from check_directions import check_direction, check_diagonal


def get_queen_moves(board, index):
    team = board[index][2]

    return (
        *check_direction(board, index, 'l', team),
        *check_direction(board, index, 'r', team),
        *check_direction(board, index, 'u', team),
        *check_direction(board, index, 'd', team),
        *check_diagonal(board, index, 'ul', team),
        *check_diagonal(board, index, 'ur', team),
        *check_diagonal(board, index, 'dl', team),
        *check_diagonal(board, index, 'dr', team),
    )
    