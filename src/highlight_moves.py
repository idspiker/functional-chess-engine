def highlight_moves(board, moves):
    return tuple(map(lambda x: highlight_tile(*x, moves), enumerate(board)))


def highlight_tile(index, tile, moves):
    if index in moves:
        return tile.change_field('is_highlighted', True)
    else:
        return tile