from check_directions import check_direction


def get_rook_moves(board, index):
    team = board[index].occupant_team

    return (
        *check_direction(board, index, 1, team), 
        *check_direction(board, index, -1, team), 
        *check_direction(board, index, -8, team), 
        *check_direction(board, index, 8, team)
    )
