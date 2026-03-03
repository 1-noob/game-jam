import pygame as pg
from ui.base import UIElement


class ProgressBar(UIElement):
    """Draws a progress bar on the screen."""

    def __init__(
            self,
            position: tuple[int, int],
            size: tuple[int, int],
            min_value: float = 0.0,
            max_value: float = 100.0,
            initial_value: float = 0.0,
            fill_color: tuple[int, int, int] = (0, 255, 0),
            background_color: tuple[int, int, int] = (255, 0, 0),
            border_color: tuple[int, int, int] = (255, 255, 255),
            border_width: int = 2,
            border_radius: int = 8,
            reverse: bool = False,
            smooth_speed: float = 1.0
    ):
        super().__init__(position)

        # Set up the progress bar dimensions 
        self.width, self.height = size
        self.rect = pg.Rect(position, size)

        # Set up the progress bar values
        self.min_value = min_value
        self.max_value = max_value
        
        # Set up the current and target values for smooth animation
        self.current_value = initial_value
        self.target_value = initial_value
        
        # Set up color of the progress bar
        self.fill_color = fill_color
        self.background_color = background_color
        self.border_color = border_color

        # Set up border properties
        self.border_width = border_width
        self.border_radius = border_radius
        
        # Set up reverse and smooth animation 
        self.reverse = reverse
        self.smooth_speed = smooth_speed


    def set_position(self, position):
        super().set_position(position)
        self.rect.topleft = position

    def set_value(self, value: float):
        """Set the target value of the progress bar."""
        self.target_value = max(self.min_value, min(self.max_value, value))

    def get_ratio(self):
        """Get the current progress as a ratio between 0.0 and 1.0."""
        span = self.max_value - self.min_value
        if span == 0:
            return 0.0
        return (self.current_value - self.min_value) / span
    
    def update(self, dt: float):
        """Smoothly update the current value towards the target value."""
        difference = self.target_value - self.current_value
        self.current_value += difference * min(self.smooth_speed * dt, 1.0)

    def draw(self, surface: pg.Surface):
        """Draw the progress bar on the given surface."""
        if not self.visible:
            return
        
        # Shadow
        shadow_rect = self.rect.move(3, 3)
        pg.draw.rect(
            surface,
            (0, 0, 0, 100),  # Semi-transparent black
            shadow_rect,
            border_radius=self.border_radius
        )

        # Background
        pg.draw.rect(
            surface,
            self.background_color,
            self.rect,
            border_radius=self.border_radius
        )

        # Fill
        ratio = self.get_ratio()
        fill_width = int(self.width * ratio)

        if fill_width > 0:
            if self.reverse:
                fill_rect = pg.Rect(
                    self.rect.right - fill_width,
                    self.rect.y,
                    fill_width,
                    self.height
                )
            else:
                fill_rect = pg.Rect(
                    self.rect.x,
                    self.rect.y,
                    fill_width,
                    self.height
                )
            
            pg.draw.rect(
                surface,
                self.fill_color,
                fill_rect,
                border_radius=self.border_radius
            )

        # Border
        pg.draw.rect(
            surface,
            self.border_color,
            self.rect,
            self.border_width,
            border_radius=self.border_radius
        )