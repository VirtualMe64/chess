import os
from board import Board
import pygame

class BoardDrawer:
    def __init__(self, board : Board, width : int, height : int,
                 whiteColor = "bisque", blackColor = "darkolivegreen4",
                 selectedColor = "gold", potentialMoveColor = "blue",
                 piecesPath = "pieces"):
        self.board = board
        self.width = width
        self.height = height
        self.squareWidth = width / 8
        self.squareHeight = height / 8
        self.whiteColor = whiteColor
        self.blackColor = blackColor
        self.selectedColor = selectedColor
        self.potentialMoveColor = potentialMoveColor
        self.piecesPath = piecesPath

    def drawBoard(self, screen):
        for y, row in enumerate(self.board.board):
            for x, piece in enumerate(row):
                rect = (
                    x * self.squareWidth,
                    y * self.squareHeight,
                    self.squareHeight + 1,
                    self.squareHeight + 1
                )
                parity = (y + x) % 2
                color = self.whiteColor if parity else self.blackColor
                if (x, y) == self.board.selectedIdx:
                    color = self.selectedColor 
                if (x, y) in self.board.potentialMoves:
                    color = self.potentialMoveColor
                pygame.draw.rect(screen, color, rect)

                if piece is not None:
                    expectedFile = f"{'white' if piece.color else 'black'}-{piece.piece.name.lower()}.png"
                    expectedPath = os.path.join(self.piecesPath, expectedFile)

                    pieceImage = pygame.image.load(expectedPath).convert_alpha()
                    pieceImage = pygame.transform.scale(pieceImage, (self.squareWidth, self.squareHeight))
                    screen.blit(pieceImage, rect)

    def coordsToIndex(self, x, y):
        xIdx = max(min(int(x / self.squareWidth), 7), 0)
        yIdx = max(min(int(y / self.squareHeight), 7), 0)
        yIdx = yIdx

        return xIdx, yIdx