from piece import Piece, PieceType
from typing import List

DEFAULT_ORDER = [
    PieceType.Rook,
    PieceType.Knight, 
    PieceType.Bishop, 
    PieceType.Queen, 
    PieceType.King, 
    PieceType.Bishop,
    PieceType.Knight,
    PieceType.Rook
]

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.selectedIdx = None

        for i in range(8):
            self.board[0][i] = Piece(DEFAULT_ORDER[i], False)
            self.board[1][i] = Piece(PieceType.Pawn, False)
            self.board[6][i] = Piece(PieceType.Pawn, True)
            self.board[7][i] = Piece(DEFAULT_ORDER[i], True)

    def setSelected(self, xIdx, yIdx):
        if (xIdx, yIdx) == self.selectedIdx:
            self.selectedIdx = None
        else:
            self.selectedIdx = (xIdx, yIdx)