import images


def pick_piece(team: int, piece: str):
    return {
        '1p': images.LIGHT_PAWN_IMAGE,
        '1r': images.LIGHT_ROOK_IMAGE,
        '1k': images.LIGHT_KNIGHT_IMAGE,
        '1b': images.LIGHT_BISHOP_IMAGE,
        '1q': images.LIGHT_QUEEN_IMAGE,
        '1K': images.LIGHT_KING_IMAGE,
        '2p': images.DARK_PAWN_IMAGE,
        '2r': images.DARK_ROOK_IMAGE,
        '2k': images.DARK_KNIGHT_IMAGE,
        '2b': images.DARK_BISHOP_IMAGE,
        '2q': images.DARK_QUEEN_IMAGE,
        '2K': images.DARK_KING_IMAGE,
    }[f'{team}{piece}']
