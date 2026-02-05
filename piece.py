from dataclasses import dataclass
from enum import Enum

class PieceType(Enum):
    Pawn = 0
    Knight = 1
    Bishop = 2
    Rook = 3
    Queen = 4
    King = 5

@dataclass
class Piece:
    piece: PieceType
    color: bool