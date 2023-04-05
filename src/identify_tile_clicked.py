from math import floor


from specs import TILE_SIZE


def identify_tile_clicked(coords):
    return (
        (floor(coords[0] / TILE_SIZE) - 1) 
        + ((floor(coords[1] / TILE_SIZE) - 1) * 8)
    )