from identify_tile_clicked import identify_tile_clicked
from identify_previous_tile import identify_previous_tile
from get_moves import get_moves
from move_piece import move_piece


def handle_click(coords, board):
    tile_index = identify_tile_clicked(coords)

    prev_index = identify_previous_tile(board)

    board = tuple(map(deactivate_tile, board))

    if prev_index is None:
        # Handle if tile is unoccupied
        if board[tile_index][2] == 0:
            return board
            
        return (
            *board[:tile_index], 
            (board[tile_index][0], 
            not board[tile_index][1], 
            *board[tile_index][2:]), 
            *board[tile_index + 1:]
        )

    # Get moves of previously selected tile
    moves = get_moves(board, prev_index)

    # Check if current tile is in the moves
    if tile_index in moves:
        board = move_piece(board, tile_index, prev_index)

    return board


def deactivate_tile(tile):
    return (tile[0], False, *tile[2:])