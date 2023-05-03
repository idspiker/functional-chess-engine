from functools import partial

from check_moves import check_moves


get_rook_moves = partial(check_moves, (1, -1, 8, -8))
