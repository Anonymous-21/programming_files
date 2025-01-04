import pyray as p
from math import sqrt, degrees, atan2


class Player:
    def __init__(
        self, spritesheet: p.Texture, sprite_dict: dict[str, p.Rectangle]
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.current_sprite: p.Rectangle = self.sprite_dict["ship_A.png"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            p.get_screen_width() / 2,
            p.get_screen_height() / 2,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0.0
        self.tint: p.Color = p.WHITE
        self.direction: p.Vector2 = p.Vector2(0, 0)
        self.speed: float = 200.0

    def draw(self) -> None:
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, world_mouse_pos: p.Vector2) -> None:
        # update player rotation
        dx: float = world_mouse_pos.x - self.dest.x
        dy: float = world_mouse_pos.y - self.dest.y
        self.rotation = degrees(atan2(dy, dx)) + 90

    def move(self) -> None:
        # update player position
        self.direction.x = int(p.is_key_down(p.KeyboardKey.KEY_D)) - int(
            p.is_key_down(p.KeyboardKey.KEY_A)
        )
        self.direction.y = int(p.is_key_down(p.KeyboardKey.KEY_S)) - int(
            p.is_key_down(p.KeyboardKey.KEY_W)
        )

        # diagonal movement - normalize vector
        direction: float = sqrt(self.direction.x**2 + self.direction.y**2)
        if direction > 0:
            self.direction.x /= direction
            self.direction.y /= direction

        # move player
        dt: float = p.get_frame_time()
        self.dest.x += self.direction.x * self.speed * dt
        self.dest.y += self.direction.y * self.speed * dt

    def check_bounds(self, background: p.Texture) -> None:
        # check bounds
        self.dest.x = max(
            self.dest.width / 2,
            min(self.dest.x, background.width - self.dest.width / 2),
        )
        self.dest.y = max(
            self.dest.height / 2,
            min(self.dest.y, background.height - self.dest.height / 2),
        )

    def update(self, background: p.Texture, world_mouse_pos: p.Vector2) -> None:
        self.rotate(world_mouse_pos)
        self.move()
        self.check_bounds(background)
