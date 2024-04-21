import pygame.draw

from utils.util import utils


class Ship:
    def __init__(self,row,col,size,dir,cells):
        """
        Initialize a Ship object.

        Args:
            row (int): Row position of the ship.
            col (int): Column position of the ship.
            size (int): Size of the ship.
            dir (int): Direction of the ship (1 for horizontal, 0 for vertical).
            cells (dict): Dictionary containing grid cells.
        """
        self.row = row
        self.col = col
        self.size = size
        self.dir = dir
        self.cells = cells

    def getCells(self):
        """
        Get the list of cells occupied by the ship.

        Returns:
            list: List of grid cells occupied by the ship.
        """
        cellsList = []
        if self.dir == 1:
            for i in range(0,self.size):
                nRow = self.row
                nCol = self.col + i
                cellsList.append(self.cells[(nRow,nCol)])
        else:
            for i in range(0,self.size):
                nRow = self.row + i
                nCol = self.col
                cellsList.append(self.cells[(nRow, nCol)])
        return cellsList

    def getRect(self):
        """
        Get the rectangle that bounds the ship.

        Returns:
            pygame.rect.Rect: Rectangle bounding the ship.
        """
        x = self.cells[(self.row, self.col)].pos.x
        y = self.cells[(self.row, self.col)].pos.y
        width = 0
        height = 0
        if self.dir == 1:
            height = self.cells[(self.row, self.col)].getRect().height
            for i in range(0, self.size):
                nRow = self.row
                nCol = self.col + i
                width += self.cells[(nRow, nCol)].getRect().width
        else:
            width = self.cells[(self.row, self.col)].getRect().width
            for i in range(0, self.size):
                nRow = self.row + i
                nCol = self.col
                height += self.cells[(nRow, nCol)].getRect().height
        return pygame.rect.Rect(x,y,width,height)

    def draw(self):
        """
        Draw the ship on the screen.
        """
        if self.dir == 1:
            for i in range(0,self.size):
                nRow = self.row
                nCol = self.col + i
                pygame.draw.rect(utils.screen,(23,23,23),self.cells[(nRow,nCol)].getRect())
        else:
            for i in range(0,self.size):
                nRow = self.row + i
                nCol = self.col
                pygame.draw.rect(utils.screen,(23,23,23),self.cells[(nRow,nCol)].getRect())