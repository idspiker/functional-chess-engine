def highlight_moves(board, moves):
    return tuple(map(lambda x: highlight_tile(*x, moves), enumerate(board)))


def highlight_tile(index, tile, moves):
    return (
        tile.change_field('is_highlighted', True) 
        if index in moves 
            else tile
    )