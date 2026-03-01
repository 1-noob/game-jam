import pygame as pg

from engine.core.engine import Engine
from engine.core.scene import Scene

class TestScene(Scene):

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.engine.running = False

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill((0, 128, 255))  


def main():
    engine = Engine(800, 800, "Window Creation Test", 60)
    engine.run(TestScene())

if __name__ == "__main__":
    main()