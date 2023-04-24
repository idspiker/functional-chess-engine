from math import floor


from specs import TILE_SIZE


def identify_tile_clicked(coords):
    return (
        None 
        if not click_validity_check(coords)
            else coords_to_tile(coords)
    )


def click_validity_check(coords):
    return (
        False
        if invalid_coord_check(coords[0]) or invalid_coord_check(coords[1])
            else True
    )


def invalid_coord_check(coord):
    return coord > TILE_SIZE * 9 or coord < TILE_SIZE


def coords_to_tile(coords):
    return (
        (floor(coords[0] / TILE_SIZE) - 1) 
        + ((floor(coords[1] / TILE_SIZE) - 1) * 8)
    )
