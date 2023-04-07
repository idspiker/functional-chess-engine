from math import floor


from specs import TILE_SIZE


def identify_tile_clicked(coords):
    if coords[0] > TILE_SIZE * 9 or coords[0] < TILE_SIZE:
        return None

    if coords[1] < TILE_SIZE or coords[1] > TILE_SIZE * 9:
        return None

    return (
        (floor(coords[0] / TILE_SIZE) - 1) 
        + ((floor(coords[1] / TILE_SIZE) - 1) * 8)
    )