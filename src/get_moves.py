from get_pawn_moves import get_pawn_moves
from get_rook_moves import get_rook_moves
from get_bishop_moves import get_bishop_moves
from get_queen_moves import get_queen_moves
from get_knight_moves import get_knight_moves
from get_king_moves import get_king_moves


def get_moves(board, index):
    if board[index].piece == 'p':
        return get_pawn_moves(board, index)
    elif board[index].piece == 'r':
        return get_rook_moves(board, index)
    elif board[index].piece == 'k':
        return get_knight_moves(board, index)
    elif board[index].piece == 'b':
        return get_bishop_moves(board, index)
    elif board[index].piece == 'q':
        return get_queen_moves(board, index)
    elif board[index].piece == 'K':
        return get_king_moves(board, index)
