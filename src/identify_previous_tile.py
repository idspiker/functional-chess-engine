from utility_funcs import is_empty


def identify_previous_tile(board, current_index=0):
    return (
        None
        if is_empty(board)
            else current_index
            if board[0].is_selected == True
                else identify_previous_tile(board[1:], current_index + 1)
    )

