import numpy as np
import pygame
from pygame import Vector2

from Game.Cell import Cell
from Game.Ship import Ship
from utils.util import utils


class Grid:
    """
    Represents a grid of cells for placing ships.

    Attributes:
        pos (Vector2): The position of the grid on the screen.
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.
        cellSize (int): The size of each cell in pixels.
        cells (dict): A dictionary containing all the cells in the grid.
        ships (list): A list of ships placed on the grid.
    """
    def __init__(self,pos):
        """
        Initializes the Grid object.

        Args:
            pos (Vector2): The position of the grid on the screen.
        """
        self.pos = pos
        self.rows = 10
        self.cols = 10
        self.cellSize = 32
        # self.data = np.zeros((self.rows, self.cols), dtype=int)
        self.cells = {}
        self.createCells()
        self.ships = []
        self.placeShips()

    def createCells(self):
        """
        Creates all the cells in the grid and stores them in a dictionary.
        """
        offset = 1
        x = self.pos.x
        y = self.pos.y
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                cell = Cell(row, col, Vector2(x, y))
                self.cells[(row,col)] = cell
                x += utils.cellSize + offset

            y += utils.cellSize + offset
            x = self.pos.x

    def placeShips(self):
        """
        Places ships on the grid.
        """
        ship = Ship(0,0,5,1,self.cells)
        # self.ships.append(ship)

    def isValidRowCol(self,row,col,size,dir):
        """
        Checks if a ship with given size and direction can be placed at the specified row and column.

        Args:
            row (int): The row index.
            col (int): The column index.
            size (int): The size of the ship.
            dir (int): The direction of the ship (1 for horizontal, -1 for vertical).

        Returns:
            bool: True if the ship can be placed at the specified position, False otherwise.
        """
        if dir == 1:
            if row > self.rows - 1 or col + size > self.cols  or row < 0 or col < 0:
                return False
        else:
            if row + size > self.rows or col > self.cols - 1 or row < 0 or col < 0:
                return False
        return True


    def draw(self):
        """
        Draws the grid and ships on the screen.
        """
       for cell in self.cells.values():
           cell.draw()
       for ship in self.ships:
           ship.draw()

    def isCollideOtherShip(self,checkShip):
        """
        Checks if a ship collides with any other ship on the grid.

        Args:
            checkShip (Ship): The ship to check for collision.

        Returns:
            bool: True if the ship collides with any other ship, False otherwise.
        """
        for ship in self.ships:
            if ship == checkShip:
                continue
            if utils.collideRect(ship.getRect(),checkShip.getRect()):
                return True
        return False

    def getCellFromPos(self,pos):
        """
        Returns the cell at the specified position.

        Args:
            pos (Vector2): The position on the screen.

        Returns:
            Cell: The cell at the specified position, or None if not found.
        """
        for cell in self.cells.values():
            if cell.getRect().collidepoint(pos):
                return cell
        return None