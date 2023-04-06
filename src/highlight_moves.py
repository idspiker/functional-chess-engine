def highlight_moves(board, moves):
    return tuple(map(lambda x: highlight_tile(*x, moves), enumerate(board)))


def highlight_tile(index, tile, moves):
    if index in moves:
        return (*tile[:5], True)
    else:
        return tile