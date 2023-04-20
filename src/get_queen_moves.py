from check_directions import check_direction


def get_queen_moves(board, index):
    team = board[index].occupant_team

    return (
        *check_direction(board, index, -1, team),
        *check_direction(board, index, 1, team),
        *check_direction(board, index, -8, team),
        *check_direction(board, index, 8, team),
        *check_direction(board, index, -9, team),
        *check_direction(board, index, -7, team),
        *check_direction(board, index, 7, team),
        *check_direction(board, index, 9, team),
    )
