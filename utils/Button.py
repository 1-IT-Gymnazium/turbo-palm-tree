import pygame

from utils.assets_manager import assetsManager
from utils.util import utils


class Button:
    """
    Represents a clickable button in the game.

    Attributes:
        id (int): The unique identifier of the button.
        pos (pygame.Vector2): The position of the button.
        text (str): The text displayed on the button.
        scale (pygame.Vector2): The scaling factor for the button image.
        font (pygame.font.Font): The font used for the button text (default is utils.font32).
        img (pygame.Surface): The image of the button.
        clickImg (pygame.Surface): The image of the button when clicked.
        drawImg (pygame.Surface): The current image of the button.
        rect (pygame.Rect): The rectangular area occupied by the button.
        clicked (bool): Flag indicating whether the button is currently clicked.
    """
    def __init__(self,id, pos,text, scale,font = utils.font32):
        """
        Initializes a Button object.

        Args:
            id (int): The unique identifier of the button.
            pos (pygame.Vector2): The position of the button.
            text (str): The text displayed on the button.
            scale (pygame.Vector2): The scaling factor for the button image.
            font (pygame.font.Font, optional): The font used for the button text (default is utils.font32).
        """
        self.id = id
        self.text = text

        self.img = assetsManager.get("button")
        self.clickImg = assetsManager.get("clickButton")
        self.drawImg = self.img
        self.pos = pos


        width = self.img.get_width()
        height = self.img.get_height()

        self.img = pygame.transform.scale(self.img, (int(width * scale.x), int(height * scale.y)))
        self.clickImg = pygame.transform.scale(self.clickImg, (int(width * scale.x), int(height * scale.y)))

        self.drawImg = self.img
        self.rect = self.drawImg.get_rect()
        self.rect.topleft = (pos.x,pos.y)
        self.clicked = False

    def onMouseDown(self):
        """
        Handles the button's behavior when the mouse button is pressed down.
        """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.drawImg = self.clickImg

    def onMouseUp(self):
        """
        Handles the button's behavior when the mouse button is released.
        """
        self.clicked = False
        self.drawImg = self.img

    def draw(self):
        """
        Draws the button on the screen.
        """
        action = False
        # get mouse position

        # check mouseover and clicked conditions
        #self.clicked = False

        # draw button on screen
        utils.screen.blit(self.drawImg, self.rect)

        if self.text != "":
            color = (233,233,233)
            textT = utils.font18.render(self.text, True, color)
            text_rect = textT.get_rect(center=(self.pos.x + self.drawImg.get_width() / 2, self.pos.y + self.drawImg.get_height() / 2))
            if self.clicked:
                text_rect.y += 4
            utils.screen.blit(textT, text_rect)

        return
