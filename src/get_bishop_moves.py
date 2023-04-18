from check_directions import check_diagonal


def get_bishop_moves(board, index):
    team = board[index].occupant_team

    return (
        *check_diagonal(board, index, -9, team),
        *check_diagonal(board, index, -7, team),
        *check_diagonal(board, index, 7, team),
        *check_diagonal(board, index, 9, team)
    )
    