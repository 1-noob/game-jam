# Engine Documentation

---

## engine/core/engine.py

Central runtime controller of the framework.

Responsible for:
- Initializing pygame
- Creating and managing the window
- Running the main game loop
- Handling scene transitions
- Managing time (delta time)
- Dispatching events, update, and render calls

---

### Class: Engine

Main application controller.

---

### `__init__(width: int, height: int, title: str)`

Creates the game window and prepares internal systems.

Parameters:
- `width` — Window width in pixels.
- `height` — Window height in pixels.
- `title` — Window caption.

Initializes:
- pygame
- display surface
- clock
- running state
- current scene (None initially)

---

### `run(starting_scene: Scene)`

Starts the main loop.

Flow:
1. Switches to `starting_scene`
2. Enters loop while `running == True`
3. Each frame:
   - Calculate `dt`
   - Process events
   - Update active scene
   - Render active scene
   - Flip display buffer

`dt` is passed to scene update for framerate-independent logic.

---

### `change_scene(new_scene: Scene)`

Switches the active scene.

Flow:
1. Store previous scene
2. Call `previous_scene.on_exit()`
3. Assign new scene
4. Inject engine reference into new scene
5. Call `new_scene.on_enter(previous_scene)`

---

### `quit()`

Stops the main loop safely.

Sets:
- `running = False`

---

## engine/core/scene.py

Defines the abstract base class for all scenes.

A Scene represents a self-contained state of the game.

Examples:
- Main menu
- Gameplay
- Pause screen
- Game over screen

---

### Class: Scene (Abstract)

Base class for all scenes.

---

### `on_enter(previous_scene: Scene | None)`

Called when the scene becomes active.

Parameters:
- `previous_scene` — Scene that was active before this one.

Use cases:
- Reset state
- Receive data
- Resume gameplay
- Start music

Default behavior: does nothing.

---

### `on_exit()`

Called before the scene is replaced.

Use cases:
- Stop sounds
- Save temporary data
- Clean up references

Default behavior: does nothing.

---

### `handle_event(event: pygame.Event)`

Processes a single pygame event.

Must be implemented.

Typical usage:
- Input handling
- Keyboard / mouse logic
- Scene switching triggers

---

### `update(dt: float)`

Updates game logic.

Parameters:
- `dt` — Delta time in seconds since last frame.

Must be implemented.

Use cases:
- Movement
- Physics
- AI
- Timers

---

### `render(surface: pygame.Surface)`

Draws everything for this scene.

Parameters:
- `surface` — The window surface to draw on.

Must be implemented.

---

## engine/core/entity/base.py

Defines the base entity class.

An Entity represents a game object.

Examples:
- Player
- Enemy
- Projectile
- Collectible
- Static object

This class is intentionally generic.

---

### Class: Entity

Base class for all game objects.

---

### Attributes

Common fields typically included:

- `position: pygame.Vector2`
- `velocity: pygame.Vector2`
- `active: bool`

These are optional depending on implementation.

---

### `update(dt: float)`

Updates the entity state.

Typical behavior:
- Integrates velocity into position:
  
  position += velocity * dt

- Handles movement logic
- Applies physics
- Updates timers

This method can be overridden by subclasses.

---

### `render(surface: pygame.Surface)`

Draws the entity.

Must be implemented in subclasses.

Typical behavior:
- Draw rectangle
- Draw sprite
- Draw shape

---

### `on_destroy()`

Optional cleanup hook.

Called before entity is removed from scene.

Use cases:
- Spawn particles
- Play sound
- Release resources

---

## Architecture Notes

- Engine controls scenes.
- Scenes control entities.
- Entities contain game logic.
- Engine never directly manipulates entities.
- Scenes are responsible for updating and rendering their entities.

Flow per frame:

Engine → Scene → Entities

Event Flow:

Engine → Scene → (optional: Entities)

---

## Time Handling

All movement and physics must use `dt`.

Correct:

    position += velocity * dt

Incorrect:

    position += velocity

This ensures framerate independence.

---

## Responsibility Separation

Engine:
- Window
- Loop
- Scene management

Scene:
- Game state
- Object grouping
- Input interpretation

Entity:
- Object behavior
- Movement
- Rendering

---
