from piece import Piece, PieceType
from typing import List, Optional

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
        self.board : List[List[Optional[Piece]]] = [[None for i in range(8)] for j in range(8)]
        self.turn = True # white's turn
        self.selectedIdx = None
        self.potentialMoves = []

        for i in range(8):
            self.board[0][i] = Piece(DEFAULT_ORDER[i], False)
            self.board[1][i] = Piece(PieceType.Pawn, False)
            self.board[6][i] = Piece(PieceType.Pawn, True)
            self.board[7][i] = Piece(DEFAULT_ORDER[i], True)

    # todo: replace with more sophisticated move class
    def applyMove(self, start, end):
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = None
        self.turn = not self.turn

    def processClick(self, xIdx, yIdx):
        selectedPiece : Piece = self.board[yIdx][xIdx]

        # deselect via 1. clicking selected square, 2. clicking empty square, 3. clicking opposite color
        if (xIdx, yIdx) in self.potentialMoves:
            self.applyMove(self.selectedIdx, (xIdx, yIdx))
            self.selectedIdx = None
            self.potentialMoves = []
        elif (xIdx, yIdx) == self.selectedIdx or not selectedPiece or selectedPiece.color != self.turn:
            # deselect all
            self.selectedIdx = None
            self.potentialMoves = []
        else:
            self.selectedIdx = (xIdx, yIdx)
            self.potentialMoves = self.getPotentialMoves(xIdx, yIdx)
            print(self.potentialMoves)

    def getPotentialMoves(self, xIdx, yIdx):
        selectedPiece : Piece = self.board[yIdx][xIdx]

        if selectedPiece is None:
            return []
        elif selectedPiece.piece == PieceType.Bishop:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (1, 1), (-1, 1), (-1, -1), (1, -1)
            ])
        elif selectedPiece.piece == PieceType.Rook:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ])
        elif selectedPiece.piece == PieceType.Queen:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)
            ])
        elif selectedPiece.piece == PieceType.Knight:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)
            ], repeated=False)
        elif selectedPiece.piece == PieceType.Pawn:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (0, 1) if not selectedPiece.color else (0, -1)
            ], repeated=False, capturing=False)
        elif selectedPiece.piece == PieceType.King:
            return self.scanForMoves(selectedPiece.color, xIdx, yIdx, [
                (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)
            ], repeated=False)
        else:
            return []

    def scanForMoves(self, color, xIdx, yIdx, dirs, repeated=True, capturing=True):
        out = []
        for dx, dy in dirs:
            for i in range(8 if repeated else 1):
                potentialX = xIdx + dx * (i + 1)
                potentialY = yIdx + dy * (i + 1)

                if potentialX < 0 or potentialX > 7 or potentialY < 0 or potentialY > 7:
                    break

                otherPiece : Piece = self.board[potentialY][potentialX]
                if otherPiece is None:
                    out.append((potentialX, potentialY))
                elif otherPiece.color != color and capturing:
                    out.append((potentialX, potentialY))
                    break
                else:
                    break
        return out