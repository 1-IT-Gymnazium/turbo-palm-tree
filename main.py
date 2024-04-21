import pygame

from utils.util import utils
from screens.PlaceShipsScreen import PlaceShipsScreen

from screens.MainGame import Game, MainGame
from screens.MainMenu import MainMenu
"""
This script runs a Pygame-based game loop for a battleship game.

Usage:
- Ensure Pygame is installed (`pip install pygame`).
- Run this script to start the game.
- Use the mouse and to interact with the game screen.
"""

utils.currentScreen = PlaceShipsScreen()

while True:
    utils.screen.fill((22, 23, 23), (0, 0, utils.width, utils.height))
    utils.initDeltaTime()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            utils.currentScreen.onKeyDown(event.key)
        if event.type == pygame.KEYUP:
            utils.currentScreen.onKeyUp(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            utils.currentScreen.onMouseDown(event)
            mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            utils.currentScreen.onMouseUp(event)
        if event.type == pygame.MOUSEWHEEL:
            utils.currentScreen.onMouseWheel(event)

    utils.currentScreen.update()
    utils.currentScreen.draw()


    pygame.display.flip()
