import pygame as pg
from ui.base import UIElement


class HeartBar(UIElement):
    """Draws a heart bar on the screen."""

    _full_heart_base = None
    _empty_heart_base = None

    def __init__(
            self,
            position: tuple[int, int],
            max_hearts: int = 5,
            size: int = 32,
            spacing: int = 8
    ):
        super().__init__(position)

        self.max_hearts = max_hearts
        self.current_hearts = max_hearts

        self.size = size
        self.spacing = spacing

        # Load heart images
        if HeartBar._full_heart_base is None:
            HeartBar._full_heart_base = pg.image.load("assets/ui/healthbar/heart_full.png").convert_alpha()
            HeartBar._empty_heart_base = pg.image.load("assets/ui/healthbar/heart_empty.png").convert_alpha()

        # Scale to desired size
        self.full_heart_image = pg.transform.smoothscale(HeartBar._full_heart_base, (self.size, self.size))
        self.empty_heart_image = pg.transform.smoothscale(HeartBar._empty_heart_base, (self.size, self.size))


    def set_position(self, position):
        super().set_position(position)

    def set_hearts(self, hearts: int):
        """Set the current number of hearts."""
        self.current_hearts = max(0, min(self.max_hearts, hearts))

    def draw(self, surface: pg.Surface):
        """Draw the heart bar on the given surface."""
        if not self.visible:
            return
        
        for i in range(self.max_hearts):
            center_x = self.x + i * (self.size + self.spacing) + self.size // 2
            center_y = self.y + self.size // 2

            image =(self.full_heart_image if i < self.current_hearts else self.empty_heart_image)

            rect = image.get_rect(center =(center_x, center_y))
            surface.blit(image,rect)
            