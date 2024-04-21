from __future__ import annotations


import sys
import pygame
import webbrowser
from pygame import Vector2

from utils.util import utils

from utils.Button import Button

from screens.Game import Game
from utils.assets_manager import assetsManager
from tkinter.filedialog import askopenfilename


class MainMenu(Game):
    """
    Represents the main menu screen of the game.

    Attributes:
        gameObjects (list): A list of game objects.
        buttons (list): A list of buttons displayed on the main menu screen.
        splashTime (float): The remaining time for displaying the splash screen image (in seconds).
    """
    def __init__(self,splashTime = 0):
        """
        Initializes the MainMenu object.

        Args:
            splashTime (float, optional): The remaining time for displaying the splash screen image (default is 0).
        """
        self.gameObjects = []

        self.buttons = []
        self.buttons.append(Button(0, Vector2(540, 140), "Start", Vector2(3, 2)))
        self.buttons.append(Button(1, Vector2(540, 240), "Load", Vector2(3, 2)))
        self.buttons.append(Button(3, Vector2(540, 440), "Quit", Vector2(3, 2)))

        self.splashTime = splashTime

    def update(self):
        """
        Updates the main menu screen.
        """
        self.splashTime -= utils.deltaTime()

    def draw(self):
        """
        Draws the main menu screen.
        """
        if self.splashTime > 0:
            utils.screen.blit(assetsManager.get("splash"),(0,0))
            return

        utils.screen.fill((233, 233, 233), (0, 0, utils.width, utils.height))
        for button in self.buttons:
            button.draw()

    def onKeyDown(self, key):
        """
        Handles key press events specific to the main menu screen.

        Args:
            key (int): The key code of the pressed key.
        """
        pass

    def onKeyUp(self, key):
        """
        Handles key release events specific to the main menu screen.

        Args:
            key (int): The key code of the released key.
        """
        pass

    def onMouseDown(self, event):
        """
        Handles mouse button press events specific to the main menu screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        if self.splashTime > 0:
            return

        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    from screens.PlaceShipsScreen import PlaceShipsScreen
                    utils.currentScreen = PlaceShipsScreen()
                    break
                if button.id == 3:
                    exit(1)

    def onMouseUp(self, event):
        """
        Handles mouse button release events specific to the main menu screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseUp()

    def onMouseWheel(self, event):
        """
        Handles mouse wheel scroll events specific to the main menu screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        pass


    def load(self):
        """
        Opens a file dialog to load a file.
        """
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(filename)
