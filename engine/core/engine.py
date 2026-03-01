import pygame as pg
from typing import Type

from .scene import Scene


class Engine:
    """
    Game Engine class:
        - Window creation
        - Main game loop
        - Scene switching
        - Time
    """

    def __init__(
            self,
            width: int = 800,
            height: int = 600,
            title: str = "pyGame jam",
            fps: int = 60,
    ):
        pg.init()
        
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        
        self.clock = pg.time.Clock()
        self.fps = fps
        self.running = False
        
        self.current_scene: Scene | None = None

    
    def change_scene(self, new_scene: Scene):
        """Switch to new scene"""
        previous = self.current_scene

        if self.current_scene:
            self.current_scene.on_exit()
        
        self.current_scene = new_scene
        self.current_scene.engine = self
        self.current_scene.on_enter(previous)


    def run(self, starting_scene: Scene):
        """Start the main game loop"""
        self.change_scene(starting_scene)
        self.running = True

        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                else:
                    self.current_scene.handle_event(event)

            self.current_scene.update(dt)
            self.current_scene.render(self.screen)         
            
            pg.display.flip()
        
        pg.quit()