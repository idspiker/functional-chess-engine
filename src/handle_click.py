from identify_tile_clicked import identify_tile_clicked
from identify_previous_tile import identify_previous_tile
from get_moves import get_moves
from move_piece import move_piece
from highlight_moves import highlight_moves


def handle_click(coords, board):
    tile_index = identify_tile_clicked(coords)

    prev_index = identify_previous_tile(board)

    board = tuple(map(deactivate_tile, board))

    if tile_index is None:
        return board

    if prev_index is None:
        # Handle if tile is unoccupied
        if board[tile_index].occupant_team == 0:
            return board

        board = (
            *board[:tile_index],
            board[tile_index].change_field(
                'is_selected', not board[tile_index].is_selected
            ),
            *board[tile_index + 1:]
        )

        board = highlight_moves(board, get_moves(board, tile_index))

        return board

    # Get moves of previously selected tile
    moves = get_moves(board, prev_index)

    # Check if current tile is in the moves
    if tile_index in moves:
        board = move_piece(board, tile_index, prev_index)

    return board


def deactivate_tile(tile):
    return tile.change_field(
        'is_selected', False
    ).change_field(
        'is_highlighted', False
    )