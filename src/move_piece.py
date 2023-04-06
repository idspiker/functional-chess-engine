def move_piece(board, new_index, old_index):
    piece_data = board[old_index]
    piece_tile = (board[new_index][0], *piece_data[1:4], True)
    empty_tile = (piece_data[0], False, 0, '', False)

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