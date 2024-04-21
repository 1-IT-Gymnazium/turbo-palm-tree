import sys

import pygame
from pygame import Vector2

from screens.MainMenu import MainMenu
from utils.Button import Button
from utils.util import utils
import screens
from screens.Game import Game
from screens.GameOver import GameOver
from utils.assets_manager import assetsManager


class MainGame(Game):
    """
    Represents the main game screen.

    Attributes:
        buttons (list): A list of buttons displayed on the main game screen.
        message (str): A message displayed on the main game screen.
        messageColor (tuple): The color of the message text.
    """
    def __init__(self,seed = None,difficult = "easy",loadGrid = None):
        """
        Initializes the MainGame object.

        Args:
            seed (any, optional): The seed for random number generation (default is None).
            difficult (str, optional): The difficulty level of the game (default is "easy").
            loadGrid (any, optional): The grid to load for the game (default is None).
        """
        self.buttons = []
        self.createButtons()
        self.message = ""
        self.messageColor = (23,23,23)
        self.createButtons()

    def createButtons(self):
        """
        Creates buttons for the main game screen.
        """
        self.buttons.append(Button(0, Vector2(utils.width - 150, 10), "Menu", Vector2(2.2, 1.2), utils.font16))


    def update(self):
        """
        Updates the main game screen.
        """
        pass

    def draw(self):
        """
        Draws the main game screen.
        """
        utils.screen.fill((233, 233, 233), (0, 0, utils.width, utils.height))

        for button in self.buttons:
            button.draw()

        messageSizeX,messageSizeY = utils.font24.size(self.message)
        utils.drawText(Vector2(utils.width - messageSizeX - 5,utils.height-messageSizeY - 5),
                       self.message,self.messageColor,utils.font24)

    def onMouseDown(self, event):
        """
        Handles mouse button press events specific to the main game screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    utils.currentScreen = MainMenu()
                    break

        mouseX, mouseY = pygame.mouse.get_pos()

    def onKeyDown(self, key):
        """
        Handles key press events specific to the main game screen.

        Args:
            key (int): The key code of the pressed key.
        """
        pass

    def onMouseUp(self, event):
        """
        Handles mouse button release events specific to the main game screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseUp()


