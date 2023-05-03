from functools import partial

from check_moves import check_moves

get_bishop_moves = partial(check_moves, (-9, -7, 9, 7))
