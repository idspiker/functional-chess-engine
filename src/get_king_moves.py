from check_directions import check_for_edge_block

def get_king_moves(board, index):
    moves = (-1, -9, -8, -7, 1, 9, 8, 7)

    possible_movement = tuple(
        filter(lambda move: check_move(board, index, move), moves)
    )

    return tuple(map(lambda move: index + move, possible_movement))


def check_move(board, index, move):
    if check_for_edge(index, move):
        return False

    if board[index + move].occupant_team == board[index].occupant_team:
        return False

    if check_for_danger(board, index, move):
        return False
    
    return True


def check_for_edge(index, movement):
    # Check left
    if index % 8 == 0 and movement in (-1, -9, 7):
        return True

    # Check right
    if index % 8 == 7 and movement in (1, -7, 9):
        return True

    # Check top
    if index < 8 and movement in (-9, -8, -7):
        return True

    # Check bottom
    if index > 55 and movement in (7, 8, 9):
        return True

    return False


def check_for_danger(board, index, movement):
    team = board[index].occupant_team

    danger_directions = (-1, 1, -8, 8, -7, 7, -9, 9)
    knight_offsets = (-17, -15, -10, -6, 6, 10, 15, 17)

    possible_danger = tuple(
        map(
            lambda dir: check_direction_for_danger(
                board, index + movement, dir, team
            ), 
            danger_directions
        )
    )

    possible_knights = tuple(
        map(
            lambda offset: check_for_knight(
                board, index + movement, offset, team
            ),
            knight_offsets
        )
    )

    if True in (*possible_danger, *possible_knights):
        return True

    return False


def check_direction_for_danger(board, index, offset, team, steps=0):
    if steps == 0:
        if check_for_edge_block(index, offset):
            return False

        index += offset

        # Check for king and pawn

    if board[index].occupant_team == team and board[index].piece != 'K':
        return False

    if board[index].occupant_team == (2 if team == 1 else 1):
        if offset in (-1, 1, -8, 8) and board[index].piece in ('q', 'r'):
            return True
        if offset in (-7, 7, -9, 9) and board[index].piece in ('q', 'b'):
            return True
        else:
            return False

    if check_for_edge_block(index, offset):
        return False

    return check_direction_for_danger(
        board, index + offset, offset, team, steps + 1
    )


def check_for_knight(board, index, offset, team):
    return False
