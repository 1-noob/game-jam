import pygame as pg
from abc import ABC, abstractmethod


class Scene(ABC):
    """
    Base class for all scenes in the game. 
    Each scene should inherit from this class and implement the required methods.
    """
    def __init__(self):
        self.engine = None

    def on_enter(self):
        """Called when scene becomes active."""
        pass

    def on_exit(self):
        """Called when scene is changed or removed."""
        pass

    @abstractmethod
    def handle_event(self, event: pg.event.Event):
        pass

    @abstractmethod
    def update(self, dt: float):
        pass

    @abstractmethod
    def render(self, surface: pg.Surface):
        pass