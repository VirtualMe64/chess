import os
from board import Board
import pygame

class BoardDrawer:
    def __init__(self, board : Board, width : int, height : int, whiteColor = "bisque", blackColor = "darkolivegreen4", piecesPath = "pieces"):
        self.board = board
        self.width = width
        self.height = height
        self.squareWidth = width / 8
        self.squareHeight = height / 8
        self.whiteColor = whiteColor
        self.blackColor = blackColor
        self.piecesPath = piecesPath

    def drawBoard(self, screen):
        for i, row in enumerate(self.board.board):
            for j, piece in enumerate(row):
                rect = (
                    j * self.squareWidth,
                    (7 - i) * self.squareHeight,
                    self.squareHeight + 1,
                    self.squareHeight + 1
                )
                parity = (i + j) % 2
                color = self.whiteColor if parity else self.blackColor
                pygame.draw.rect(screen, color, rect)

                if piece is not None:
                    expectedFile = f"{'black' if piece.isWhite else 'white'}-{piece.piece.name.lower()}.png"
                    expectedPath = os.path.join(self.piecesPath, expectedFile)

                    pieceImage = pygame.image.load(expectedPath).convert_alpha()
                    pieceImage = pygame.transform.scale(pieceImage, (self.squareWidth, self.squareHeight))
                    screen.blit(pieceImage, rect)