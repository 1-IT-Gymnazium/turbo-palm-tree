from __future__ import annotations


import sys
import pygame
from pygame import Vector2

from utils.util import utils

from utils.Button import Button

from screens.Game import Game
from utils.assets_manager import assetsManager

class GameOver(Game):
    """
    Represents the game over screen.

    Attributes:
        gameObjects (list): A list of game objects.
        buttons (list): A list of buttons displayed on the game over screen.
    """
    def __init__(self):
        """
        Initializes the GameOver object.
        """
        self.gameObjects = []
        self.buttons = []
        self.buttons.append(Button(0, Vector2(500, 240), "Restart", Vector2(3, 2)))
        self.buttons.append(Button(1, Vector2(500, 340), "Menu", Vector2(3, 2)))
        self.buttons.append(Button(2, Vector2(500, 440), "Quit", Vector2(3, 2)))


    def update(self):
        """
        Updates the game over screen.
        """
        pass


    def draw(self):
        """
        Draws the game over screen.
        """
        utils.screen.fill((233, 233, 233), (0, 0, utils.width, utils.height))

        for button in self.buttons:
            button.draw()

        utils.drawText(Vector2(250, 150), "Game Over!", (233, 23, 23), utils.font24)



    def onKeyDown(self, key):
        """
        Handles key press events specific to the game over screen.

        Args:
            key (int): The key code of the pressed key.
        """
        pass

    def onKeyUp(self, key):
        """
        Handles key release events specific to the game over screen.

        Args:
            key (int): The key code of the released key.
        """
        pass

    def onMouseDown(self, event):
        """
        Handles mouse button press events specific to the game over screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    from screens.PlaceShipsScreen import PlaceShipsScreen
                    utils.currentScreen = PlaceShipsScreen()
                    break
                if button.id == 1:
                    from screens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()
                    break
                if button.id == 2:
                    exit(1)

    def onMouseUp(self, event):
        """
        Handles mouse button release events specific to the game over screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        """
        Handles mouse wheel scroll events specific to the game over screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        pass

