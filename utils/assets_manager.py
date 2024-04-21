import pygame


class AssetsManager:
    """
    Manages game assets such as images.

    Attributes:
        assets (dict): A dictionary containing asset names as keys and corresponding loaded images as values.
    """
    def __init__(self):
        """
        Initializes the AssetsManager object and loads the game assets.
        """
        self.assets = {
            'button': pygame.image.load("assets/btn.png").convert_alpha(),
            'clickButton': pygame.image.load("assets/clickBtn.png").convert_alpha(),
            'splash': pygame.image.load("assets/splash_screen_image.png").convert_alpha(),
        }

    def get(self, key):
        """
        Retrieves the specified asset.

        Args:
            key (str): The name of the asset to retrieve.

        Returns:
            pygame.Surface: The loaded image asset.
        """
        return self.assets[key]


assetsManager = AssetsManager()
