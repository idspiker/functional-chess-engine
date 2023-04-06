def identify_previous_tile(board, current_index=0):
    if len(board) == 0:
        return None

    if board[0][1] == True:
        return current_index

    return identify_previous_tile(board[1:], current_index + 1)
