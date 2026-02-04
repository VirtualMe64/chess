from board import Board
from graphics import BoardDrawer

import pygame


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = Board()
boardDrawer = BoardDrawer(board, WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    boardDrawer.drawBoard(screen)

    pygame.display.flip()