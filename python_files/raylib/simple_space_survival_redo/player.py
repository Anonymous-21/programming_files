import pyray as p
from math import degrees, atan2

from bullet_list import BulletList


class Player:
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        background: p.Texture,
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict
        self.background: p.Texture = background

        self.current_sprite: p.Rectangle = self.sprite_dict["ship_A.png"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            background.width / 2,
            background.height / 2,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0
        self.tint: p.Color = p.WHITE
        self.speed: float = 5
        self.health: float = 100

        self.bullets = BulletList()

    def is_alive(self) -> bool:
        return self.health > 0

    def draw(self) -> None:
        self.bullets.draw()

        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, mouse_x: float, mouse_y: float) -> None:
        dx: float = mouse_x - self.dest.x
        dy: float = mouse_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self) -> None:
        if p.is_key_down(p.KeyboardKey.KEY_W):
            self.dest.y -= self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_S):
            self.dest.y += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_A):
            self.dest.x -= self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_D):
            self.dest.x += self.speed

    def bounds(self) -> None:
        self.dest.x = max(
            self.dest.width / 2,
            min(self.dest.x, self.background.width - self.dest.width / 2),
        )
        self.dest.y = max(
            self.dest.height / 2,
            min(self.dest.y, self.background.height - self.dest.height / 2),
        )

    def update(self, mouse_x: float, mouse_y: float) -> None:
        self.rotate(mouse_x, mouse_y)
        self.move()
        self.bounds()  # player movement boundary

        self.bullets.update(
            self.spritesheet,
            self.sprite_dict,
            mouse_x,
            mouse_y,
            self.dest.x,
            self.dest.y,
        )
