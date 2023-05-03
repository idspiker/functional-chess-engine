from enum import Enum, unique


@unique
class TileColor(Enum):
    WHITE = 1
    BLACK = 2


@unique
class Piece(Enum):
    EMPTY = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6


@unique
class Team(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2
