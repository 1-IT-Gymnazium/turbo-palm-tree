
import pygame
import math
from pygame.locals import *

from pygame import Vector2, mixer, time



class Utils():
    """
    Utility class for handling game-related functionalities.
    """
    def __init__(self):
        """
        Initializes the Utils object and Pygame.
        """
        pygame.init()

        self.width = 1280
        self.height = 720
        self.cellSize = 40

        self.gameOver = False
        self.currentLevel = 0
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | FULLSCREEN, 16)
        pygame.display.set_caption("Battleship")
        self.dt = 0
        self.clock = pygame.time.Clock()

        self.currentScreen = None

        self.fps = 0
        self.fpsCounter = 0
        self.fpsTimeCount = 0

        self.font8 = pygame.font.Font('assets/helveticaneuebold.ttf', 8)
        self.font12 = pygame.font.Font('assets/helveticaneuebold.ttf', 12)
        self.font16 = pygame.font.Font('assets/helveticaneuebold.ttf', 16)
        self.font18 = pygame.font.Font('assets/helveticaneuebold.ttf', 18)
        self.font24 = pygame.font.Font('assets/helveticaneuebold.ttf', 24)
        self.font32 = pygame.font.Font('assets/helveticaneuebold.ttf', 32)
        self.font48 = pygame.font.Font('assets/helveticaneuebold.ttf', 48)

        self.camera = Vector2(0, 900)
        self.mousePos = Vector2(0,0)

        # world grid, path finding global variables
        self.rows = 100
        self.cols = 50
        self.grid = None
        self.astar = None

    def initDeltaTime(self):  # calculate deltaTime
        """
        Initializes delta time for frame-rate independence.
        """
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        """
        Returns the delta time.

        :return: Delta time value.
        """
        return self.dt

    def drawText(self, pos, text, color, font):  # draw text
        """
        Draws text on the screen.

        :param pos: Position of the text (Vector2).
        :param text: Text to be drawn.
        :param color: Color of the text.
        :param font: Font to be used for the text.
        """
        text = font.render(text, True, color)
        self.screen.blit(text, (pos.x, pos.y))

    def collideRect(self, a, b):  # aabb 2 box collide check
        """
        Checks collision between two rectangular objects.

        :param a: First rectangular object (pygame.Rect).
        :param b: Second rectangular object (pygame.Rect).
        :return: True if collision occurs, False otherwise.
        """
        rect = a
        r = b
        if r.x < rect.x + rect.w and r.x + r.w > rect.x and r.y < rect.y + rect.h and r.h + r.y > rect.y:
            return True
        return False

utils = Utils()  # util is global object
