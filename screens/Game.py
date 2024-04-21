class Game:
    """
    Base class for implementing a game screen.

    This class serves as a template for creating specific game screens.

    Attributes:
        None
    """
    def __init__(self):
        """
        Initializes the Game object.
        """
        pass

    def update(self):
        """
        Updates the game screen state.
        """
        raise NotImplementedError()

    def draw(self):
        """
        Draws the game screen elements on the screen.
        """
        raise NotImplementedError()

    def onKeyDown(self, key):
        """
        Handles key press events specific to the game screen.

        Args:
            key (int): The key code of the pressed key.
        """
        pass

    def onKeyUp(self, key):
        """
        Handles key release events specific to the game screen.

        Args:
            key (int): The key code of the released key.
        """
        pass

    def onMouseDown(self, event):
        """
        Handles mouse button press events specific to the game screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        pass
    """
    Handles mouse button press events specific to the game screen.

    Args:
        event (pygame.event.Event): The mouse event object.
    """

    def onMouseUp(self, event):
        """
        Handles mouse button release events specific to the game screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """

        pass

    def onMouseWheel(self, event):
        """
        Handles mouse wheel scroll events specific to the game screen.

        Args:
            event (pygame.event.Event): The mouse event object.
        """
        pass