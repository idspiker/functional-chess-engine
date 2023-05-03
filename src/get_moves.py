from field_enumerations import Piece
from get_pawn_moves import get_pawn_moves
from get_rook_moves import get_rook_moves
from get_bishop_moves import get_bishop_moves
from get_queen_moves import get_queen_moves
from get_knight_moves import get_knight_moves
from get_king_moves import get_king_moves


def get_moves(board, index):
    match board[index].piece:
        case Piece.PAWN:
            return get_pawn_moves(board, index)
        case Piece.ROOK:
            return get_rook_moves(board, index)
        case Piece.KNIGHT:
            return get_knight_moves(board, index)
        case Piece.BISHOP:
            return get_bishop_moves(board, index)
        case Piece.QUEEN:
            return get_queen_moves(board, index)
        case Piece.KING:
            return get_king_moves(board, index)
