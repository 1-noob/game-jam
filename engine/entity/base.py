import pygame as pg
from typing import Optional


class EntityBase:
    """
    Base class for all game entities.
    """

    def __init__(self, 
                 position: tuple[float, float] = (0, 0),
                 size: Optional[pg.Surface] = None
    ):
        self.position = pg.Vector2(position)
        self.velocity = pg.Vector2(0, 0)

        self.sprite: Optional[pg.Surface] = None
        self.rect: Optional[pg.Rect] = None
    
        if self.sprite:
            self.rect = self.sprite.get_rect(center=self.position)

        # Allows disabling without removing from scene
        self.active = True

    # Core behavior methods

    def update(self, dt: float):
        """
        Update entity logic
        Integrates velocity into position"""
        self.position += self.velocity * dt

        if self.rect:
            self.rect.center = self.position

    def render(self, surface: pg.Surface):
        """Draw entity sprite (if available) to the screen"""
        if self.sprite and self.rect:
            surface.blit(self.sprite, self.rect)

    # Utility methods

    def destroy(self):
        """Mark entity for removal from scene"""
        self.active = False