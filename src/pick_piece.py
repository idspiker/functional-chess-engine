import images
from field_enumerations import Team, Piece


def pick_piece(team: int, piece: str):
    if team is Team.WHITE:
        match piece: 
            case Piece.PAWN:
                return images.LIGHT_PAWN_IMAGE
            case Piece.ROOK:
                return images.LIGHT_ROOK_IMAGE
            case Piece.KNIGHT:
                return images.LIGHT_KNIGHT_IMAGE
            case Piece.BISHOP:
                return images.LIGHT_BISHOP_IMAGE
            case Piece.QUEEN:
                return images.LIGHT_QUEEN_IMAGE
            case Piece.KING:
                return images.LIGHT_KING_IMAGE
    elif team is Team.BLACK:
        match piece: 
            case Piece.PAWN:
                return images.DARK_PAWN_IMAGE
            case Piece.ROOK:
                return images.DARK_ROOK_IMAGE
            case Piece.KNIGHT:
                return images.DARK_KNIGHT_IMAGE
            case Piece.BISHOP:
                return images.DARK_BISHOP_IMAGE
            case Piece.QUEEN:
                return images.DARK_QUEEN_IMAGE
            case Piece.KING:
                return images.DARK_KING_IMAGE
