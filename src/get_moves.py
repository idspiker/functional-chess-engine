from get_pawn_moves import get_pawn_moves
from get_rook_moves import get_rook_moves
from get_bishop_moves import get_bishop_moves
from get_queen_moves import get_queen_moves
from get_knight_moves import get_knight_moves
from get_king_moves import get_king_moves


def get_moves(board, index):
    if board[index][3] == 'p':
        return get_pawn_moves(board, index)
    elif board[index][3] == 'r':
        return get_rook_moves(board, index)
    elif board[index][3] == 'k':
        return get_knight_moves(board, index)
    elif board[index][3] == 'b':
        return get_bishop_moves(board, index)
    elif board[index][3] == 'q':
        return get_queen_moves(board, index)
    elif board[index][3] == 'K':
        return get_king_moves(board, index)
