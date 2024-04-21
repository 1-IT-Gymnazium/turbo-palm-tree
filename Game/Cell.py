import pygame.draw
from pygame import Vector2

from utils.util import utils


class Cell:
    """
    Represents a cell in a grid.

    Attributes:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        cellType (str): The type of the cell (optional).
        pos (Vector2): The position of the cell on the screen.
    """
    def __init__(self, row, col, pos, cellType=''):
        """
        Initializes the Cell object.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            pos (Vector2): The position of the cell on the screen.
            cellType (str, optional): The type of the cell (default is '').
        """
        self.row = row
        self.col = col
        self.cellType = cellType
        self.pos = pos

    def draw(self):
        """
        Draws the cell on the screen.
        """
        pygame.draw.rect(utils.screen, (23, 23, 23), self.getRect(), 1)

    def getRect(self):
        """
        Returns the rectangle representing the cell's position and size.

        Returns:
            pygame.Rect: The rectangle representing the cell.
        """
        rect = pygame.rect.Rect(self.pos.x, self.pos.y, utils.cellSize, utils.cellSize)
        return rect
