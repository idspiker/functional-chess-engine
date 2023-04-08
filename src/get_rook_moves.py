from check_directions import check_direction


def get_rook_moves(board, index):
    team = board[index][2]

    return (
        *check_direction(board, index, 'r', team), 
        *check_direction(board, index, 'l', team), 
        *check_direction(board, index, 'u', team), 
        *check_direction(board, index, 'd', team)
    )
