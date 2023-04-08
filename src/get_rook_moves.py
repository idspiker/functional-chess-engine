from check_directions import check_direction


def get_rook_moves(board, index):
    return (
        *check_direction(board, index, 'r', board[index][2]), 
        *check_direction(board, index, 'l', board[index][2]), 
        *check_direction(board, index, 'u', board[index][2]), 
        *check_direction(board, index, 'd', board[index][2])
    )
