from check_moves import check_for_edge_block
from get_knight_moves import check_for_edge


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

    possible_danger = tuple(
        map(
            lambda dir: check_direction_for_danger(
                board, index + movement, dir, team
            ), 
            danger_directions
        )
    )

    possible_knights = check_for_knights(board, index + movement, team)

    if True in (*possible_danger, possible_knights):
        return True

    return False


def check_direction_for_danger(board, index, offset, team, is_first_step=True):
    if is_first_step:
        if check_for_edge_block(index, offset):
            return False

        # Check for pawn and king TODO change pawn algo
        if team == 1:
            l_pos_pawn = board[index - 9]
            l_edge_block = check_for_edge_block(index, -9)
            r_pos_pawn = board[index - 7]
            r_edge_block = check_for_edge_block(index, -7)
            enemy = 2
        elif team == 2:
            l_pos_pawn = board[index + 7]
            l_edge_block = check_for_edge_block(index, 7)
            r_pos_pawn = board[index + 9]
            r_edge_block = check_for_edge_block(index, 9)
            enemy = 1

        # Pawn check
        if (not l_edge_block 
            and l_pos_pawn.occupant_team == enemy 
            and l_pos_pawn.piece == 'p'):
            return True
        if (not r_edge_block 
            and r_pos_pawn.occupant_team == enemy 
            and r_pos_pawn.piece == 'p'):
            return True

        # King check
        def king_check(offset):
            if check_for_edge_block(index, offset):
                return False

            pos_king = board[index + offset]
            if pos_king.occupant_team == enemy and pos_king.piece == 'K':
                return True
            
            return False

        if True in tuple(map(king_check, (-1, -9, -8, -7, 1, 9, 8, 7))):
            return True

        index += offset

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
        board, index + offset, offset, team, False
    )


def check_for_knights(board, index, team):
    # TODO implement later
    # offsets = (-17, -15, -10, -6, 6, 10, 15, 17)

    # def check_offset(board, index, offset):
    #     if check_for_edge(index, offset):
    #         return False

    #     print(check_for_edge(index, offset))
    #     print(index + offset)

    #     if (board[index + offset].occupant_team != team 
    #         and board[index + offset].piece == 'k'):
    #         return True

    # possible_knights = tuple(
    #     map(lambda offset: check_offset(board, index, offset), offsets)
    # )

    # if True in possible_knights:
    #     return True

    return False
