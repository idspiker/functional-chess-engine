from tile import Tile
from field_enumerations import Team, Piece


def move_piece(board, new_index, old_index):
    piece_data = board[old_index]
    
    piece_tile = piece_data.change_field(
        'tile_color', board[new_index].tile_color
    ).change_field(
        'has_moved', True
    ).change_field(
        'is_highlighted', False
    )

    empty_tile = Tile(
        piece_data.tile_color, False, Team.EMPTY, Piece.EMPTY, False, False
    )

    if new_index > old_index:
        board = (
            *board[:old_index], 
            empty_tile, 
            *board[old_index + 1:new_index], 
            piece_tile, 
            *board[new_index + 1:]
        )
    elif new_index < old_index:
        board = (
            *board[:new_index],
            piece_tile,
            *board[new_index + 1:old_index],
            empty_tile,
            *board[old_index + 1:]
        )

    return board
