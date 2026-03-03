import pygame as pg
from ui.base import UIElement


class HeartBar(UIElement):
    """Draws a heart bar on the screen."""

    def __init__(
            self,
            position: tuple[int, int],
            max_hearts: int = 5,
            size: int = 32,
            spacing: int = 8,
            full_color: tuple[int, int, int] = (220, 40, 40),
            empty_color: tuple[int, int, int] = (70, 70, 70),
            outline_color: tuple[int, int, int] = (255, 255, 255)
    ):
        super().__init__(position)

        self.max_hearts = max_hearts
        self.current_hearts = max_hearts

        self.size = size
        self.spacing = spacing

        self.full_color = full_color
        self.empty_color = empty_color
        self.outline_color = outline_color

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

            color = self.full_color if i < self.current_hearts else self.empty_color

            # Draw the heart shape (simple circle for demonstration)
            pg.draw.circle(surface, color, (center_x, center_y), self.size // 2)

            # Draw the outline
            pg.draw.circle(surface, self.outline_color, (center_x, center_y), self.size // 2, 2)
            