import pygame
from ui.base import UIElement


class UIManager:
    """Manages multiple UI elements and handles their updates and drawing."""

    def __init__(self):
        self.elements: list[UIElement] = []

    def add_element(self, element: UIElement):
        """Add a UI element to the manager."""
        self.elements.append(element)

    def remove_element(self, element: UIElement):
        """Remove a UI element from the manager."""
        if element in self.elements:
            self.elements.remove(element)

    def update(self, dt: float):
        """Update all managed UI elements."""
        for element in self.elements:
            element.update(dt)

    def draw(self, surface: pygame.Surface):
        """Draw all visible UI elements on the given surface."""
        for element in self.elements:
            if element.visible:
                element.draw(surface)