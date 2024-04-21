from __future__ import annotations

import sys
import pygame
from pygame import Vector2

from Game.Grid import Grid
from Game.Ship import Ship
from utils.util import utils

from utils.Button import Button

from screens.Game import Game
from utils.assets_manager import assetsManager


class PlaceShipsScreen(Game):
    """
    Represents the screen for placing ships before the game starts.

    Attributes:
        gameObjects (list): A list of game objects.
        buttons (list): A list of buttons displayed on the place ships screen.
        seed (any): The seed for random number generation.
        grid1 (Grid): The grid for player 1's ships.
        selectShip1 (Ship): The ship selected for placement or rotation for player 1.
        newShip1 (Ship): The newly created ship for player 1.
        grid2 (Grid): The grid for player 2's ships.
        selectShip2 (Ship): The ship selected for placement or rotation for player 2.
        newShip2 (Ship): The newly created ship for player 2.
    """
    def __init__(self):
        """
        Initializes the PlaceShipsScreen object.
        """
        self.gameObjects = []

        self.buttons = []
        self.buttons.append(Button(0, Vector2(540, 640), "Play", Vector2(3, 2)))

        self.seed = None
        self.grid1 = Grid(Vector2(50,50))
        self.selectShip1 = None
        self.newShip1 = None

        self.grid2 = Grid(Vector2(utils.width/2 + 170, 50))
        self.selectShip2 = None
        self.newShip2 = None

    def update(self):
        """
        Updates the place ships screen.
        """
        self.grid1Update()
        self.grid2Update()

    def grid1Update(self):
        """
        Updates player 1's ship grid.
        """
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.selectShip1 is not None:
            cell = self.grid1.getCellFromPos(Vector2(mouseX,mouseY))
            if cell is not None \
                    and self.grid1.isValidRowCol(cell.row,cell.col,self.selectShip1.size,self.selectShip1.dir):

                prevRow = self.selectShip1.row
                prevCol = self.selectShip1.col
                self.selectShip1.row = cell.row
                self.selectShip1.col = cell.col
                if self.grid1.isCollideOtherShip(self.selectShip1):
                    self.selectShip1.row = prevRow
                    self.selectShip1.col = prevCol
        elif self.newShip1 is not None:
            cell = self.grid1.getCellFromPos(Vector2(mouseX, mouseY))
            if cell is not None:
                dir = 1
                size = 1
                if cell.row > self.newShip1.row:
                    dir = -1
                if dir == 1 and cell.col > self.newShip1.col:
                    size = cell.col - self.newShip1.col + 1
                elif dir == -1 and cell.row > self.newShip1.row:
                    size = cell.row - self.newShip1.row + 1
                self.newShip1.size = size
                self.newShip1.dir = dir
                if self.grid1.isCollideOtherShip(self.newShip1):
                    self.newShip1 = None

    def grid2Update(self):
        """
        Updates player 2's ship grid.
        """
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.selectShip2 is not None:
            cell = self.grid2.getCellFromPos(Vector2(mouseX, mouseY))
            if cell is not None \
                    and self.grid2.isValidRowCol(cell.row, cell.col, self.selectShip2.size, self.selectShip2.dir):

                prevRow = self.selectShip2.row
                prevCol = self.selectShip2.col
                self.selectShip2.row = cell.row
                self.selectShip2.col = cell.col
                if self.grid2.isCollideOtherShip(self.selectShip2):
                    self.selectShip2.row = prevRow
                    self.selectShip2.col = prevCol
        elif self.newShip2 is not None:
            cell = self.grid2.getCellFromPos(Vector2(mouseX, mouseY))
            if cell is not None:
                dir = 1
                size = 1
                if cell.row > self.newShip2.row:
                    dir = -1
                if dir == 1 and cell.col > self.newShip2.col:
                    size = cell.col - self.newShip2.col + 1
                elif dir == -1 and cell.row > self.newShip2.row:
                    size = cell.row - self.newShip2.row + 1
                self.newShip2.size = size
                self.newShip2.dir = dir
                if self.grid2.isCollideOtherShip(self.newShip2):
                    self.newShip2 = None

    def draw(self):
        """
        Draws the place ships screen.
        """
        utils.screen.fill((233, 233, 233), (0, 0, utils.width, utils.height))
        for button in self.buttons:
            button.draw()

        self.grid1.draw()
        if self.newShip1 is not None:
            self.newShip1.draw()

        self.grid2.draw()
        if self.newShip2 is not None:
            self.newShip2.draw()

    def onKeyDown(self, key):
        """
        Handles key press events specific to the place ships screen.

        Args:
            key (int): The key code of the pressed key.
        """
        if key == pygame.K_d:
            if self.selectShip1 is not None:
                self.grid1.ships.remove(self.selectShip1)
                self.selectShip1 = None

            if self.selectShip2 is not None:
                self.grid2.ships.remove(self.selectShip2)
                self.selectShip2 = None

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        """
        Handles mouse button press events specific to the place ships screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 0:
                    from screens.MainGame import MainGame
                    utils.currentScreen = MainGame()
                    break
                if button.id == 3:
                    exit(1)

        if event.button == 1:
            self.selectAndMoveShip()
            if self.selectShip1 is None:
                self.createNewShip1()
            if self.selectShip2 is None:
                self.createNewShip2()
        elif event.button == 3:
            self.selectAndRotateShip()


    def createNewShip1(self):
        """
        Creates a new ship for player 1 based on the current mouse position.
        """
        if self.newShip1 is not None:
            return
        mouseX, mouseY = pygame.mouse.get_pos()
        cell = self.grid1.getCellFromPos(Vector2(mouseX, mouseY))
        if cell is not None:
            self.newShip1 = Ship(cell.row,cell.col,1,1,self.grid1.cells)

    def createNewShip2(self):
        """
        Creates a new ship for player 2 based on the current mouse position.
        """
        if self.newShip2 is not None:
            return
        mouseX, mouseY = pygame.mouse.get_pos()
        cell = self.grid2.getCellFromPos(Vector2(mouseX, mouseY))
        if cell is not None:
            self.newShip2 = Ship(cell.row, cell.col, 1, 1, self.grid2.cells)


    def selectAndRotateShip(self):
        """
        Selects a ship and rotates it when the right mouse button is clicked.
        """
        mouseX, mouseY = pygame.mouse.get_pos()
        for ship1 in self.grid1.ships:
            if ship1.getRect().collidepoint(mouseX, mouseY):
                self.selectShip1 = ship1
                break
        if self.selectShip1 is not None:
            dir = self.selectShip1.dir * -1
            if self.grid1.isValidRowCol(self.selectShip1.row,self.selectShip1.col,self.selectShip1.size,dir):
                prevDir = self.selectShip1.dir
                self.selectShip1.dir = dir
                if self.grid1.isCollideOtherShip(self.selectShip1):
                    self.selectShip1.dir = prevDir
                self.selectShip1 = None

        #########################
        for ship2 in self.grid2.ships:
            if ship2.getRect().collidepoint(mouseX, mouseY):
                self.selectShip2 = ship2
                break
        if self.selectShip2 is not None:
            dir = self.selectShip2.dir * -1
            if self.grid2.isValidRowCol(self.selectShip2.row,self.selectShip2.col,self.selectShip2.size,dir):
                prevDir = self.selectShip2.dir
                self.selectShip2.dir = dir
                if self.grid2.isCollideOtherShip(self.selectShip2):
                    self.selectShip2.dir = prevDir
                self.selectShip2 = None

    def selectAndMoveShip(self):
        """
        Selects a ship and allows it to be moved to a new position on the grid when the left mouse button is clicked.
        """
        mouseX,mouseY = pygame.mouse.get_pos()
        for ship1 in self.grid1.ships:
            if ship1.getRect().collidepoint(mouseX,mouseY):
                self.selectShip1 = ship1
                break
        ##############
        for ship2 in self.grid2.ships:
            if ship2.getRect().collidepoint(mouseX,mouseY):
                self.selectShip2 = ship2
                break

    def onMouseUp(self, event):
        """
        Handles mouse button release events specific to the place ships screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        for button in self.buttons:
            button.onMouseUp()
        self.selectShip1 = None
        if self.newShip1 is not None:
            self.grid1.ships.append(Ship(self.newShip1.row,self.newShip1.col,self.newShip1.size,self.newShip1.dir,self.grid1.cells))
            self.newShip1 = None

        ############
        self.selectShip2 = None
        if self.newShip2 is not None:
            self.grid2.ships.append(
                Ship(self.newShip2.row, self.newShip2.col, self.newShip2.size, self.newShip2.dir, self.grid2.cells))
            self.newShip2 = None

    def onMouseWheel(self, event):
        """
        Handles mouse wheel scroll events specific to the place ships screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        pass
