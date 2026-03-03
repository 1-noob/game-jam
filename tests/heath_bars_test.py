import pygame as pg
import sys

from ui.progress_bar import ProgressBar
from ui.heart_bar import HeartBar
from ui.manager import UIManager

from engine.core.scene import Scene
from engine.core.engine import Engine


class TestScene(Scene):

    def __init__(self):
        super().__init__()

        # Create a UI manager
        self.ui_manager = UIManager()

        # Progress bars
        self.health_bar = ProgressBar(
            position=(40, 40),
            size = (300, 30),
            fill_color=(220,50,50)
        )

        self.mana_bar = ProgressBar(
            position=(40, 90),  
            size=(300, 30),
            min_value=0,
            max_value=100,
            initial_value=0,
            fill_color=(50, 150, 255),
        )

        self.reverse_bar = ProgressBar(
            position=(500, 80),
            size=(300, 25),
            fill_color=(80, 200, 120),
            reverse=True
        )

        self.bottom_bar = ProgressBar(
            position=(250, 500),
            size=(400, 25),
            fill_color=(200, 180, 50),
        )

        # Heart bar
        self.heart_bar_1 = HeartBar(
            position=(40, 150),
            max_hearts=5,
        )

        self.heart_bar_2 = HeartBar(
            position = (500, 150),
            max_hearts=8,
            size=18,
        )

        # Add to UI manager
        self.ui_manager.add_element(self.health_bar)
        self.ui_manager.add_element(self.mana_bar)
        self.ui_manager.add_element(self.reverse_bar)
        self.ui_manager.add_element(self.bottom_bar)
        self.ui_manager.add_element(self.heart_bar_1)
        self.ui_manager.add_element(self.heart_bar_2)


        # Test values
        self.health = 100
        self.mana = 0
        self.reverse_value = 100
        self.bottom_value = 100
        self.lives = 5

        self.heart_timer = 0

    def handle_event(self, event):
        pass

    def update(self, dt):
        # Simulate health and mana changes

        self.health -= 20 * dt
        if self.health <= 0:
            self.health = 100

        self.mana += 40 * dt
        if self.mana >= 100:
            self.mana = 100

        self.reverse_value -= 30 * dt
        if self.reverse_value <= 0:
            self.reverse_value = 100

        self.bottom_value -= 10 * dt
        if self.bottom_value <= 0:
            self.bottom_value = 100

        # Update bars
        self.health_bar.set_value(self.health)
        self.mana_bar.set_value(self.mana)
        self.reverse_bar.set_value(self.reverse_value)
        self.bottom_bar.set_value(self.bottom_value)

        # Simulate heart loss every 2 seconds
        self.heart_timer += dt
        if self.heart_timer >= 2:
            self.heart_timer = 0
            self.lives -= 1
            if self.lives < 0:
                self.lives = self.heart_bar_1.max_hearts

        self.heart_bar_1.set_hearts(self.lives)

        # Update UI
        self.ui_manager.update(dt)

    # ---------------------------------

    def render(self, screen: pg.Surface):
        screen.fill((25, 25, 35))
        self.ui_manager.draw(screen)




if __name__ == "__main__":
    engine = Engine(
        width=800,
        height=800,
        title="Health Bar Test",
        fps=60
    )

    engine.run(TestScene())
