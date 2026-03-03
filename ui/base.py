import pygame

class UIElement:
    def __init__(self, position: tuple[int, int]):
        self.x, self.y = position

    def set_position(self, position: tuple[int, int]):
        self.x, self.y = position

    def update(self, dt: float):
        pass

    def draw(self, surface: pygame.Surface):
        raise NotImplementedError("Subclasses must implement the draw method.")