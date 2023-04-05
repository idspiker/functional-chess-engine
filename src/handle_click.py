from identify_tile_clicked import identify_tile_clicked


def handle_click(coords, board):
    tile_index = identify_tile_clicked(coords)

    return (
        *board[:tile_index], 
        (board[tile_index][0], 
        not board[tile_index][1], 
        board[tile_index][2], 
        board[tile_index][3]), 
        *board[tile_index + 1:]
    )