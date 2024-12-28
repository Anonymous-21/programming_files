import pyray as p
from math import atan2, degrees

from bullet_list import BulletList


class Player:
    def __init__(
        self, spritesheet: p.Texture, sprite_dict: dict[str, p.Rectangle]
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.max_health: int = 100
        self.health: int = self.max_health
        self.damage: int = 1

        self.current_sprite: p.Rectangle = self.sprite_dict["ship_A.png"]

        self.source: p.Rectangle = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest: p.Rectangle = p.Rectangle(
            p.get_screen_width() / 2,
            p.get_screen_height() / 2,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin: p.Vector2 = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0
        self.tint: p.Color = p.WHITE
        self.speed: float = 5

        self.bullet_list: BulletList = BulletList(self.spritesheet, self.sprite_dict)

    def is_alive(self) -> bool:
        return self.health > 0

    def attack(self, target) -> None:
        target.health -= self.damage

    def draw(self) -> None:
        self.bullet_list.draw()
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self) -> None:
        mouse_pos: p.Vector2 = p.get_mouse_position()
        dx: float = mouse_pos.x - self.dest.x
        dy: float = mouse_pos.y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self) -> None:
        if p.is_key_down(p.KeyboardKey.KEY_A) and self.dest.x >= self.dest.width / 2:
            self.dest.x -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_D)
            and self.dest.x <= p.get_screen_width() - self.dest.width / 2
        ):
            self.dest.x += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_W) and self.dest.y >= self.dest.height / 2:
            self.dest.y -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_S)
            and self.dest.y <= p.get_screen_height() - self.dest.height / 2
        ):
            self.dest.y += self.speed

    def update(self):
        self.rotate()
        self.move()

        mouse_pos: p.Vector2 = p.get_mouse_position()
        self.bullet_list.update(self.dest.x, self.dest.y, mouse_pos.x, mouse_pos.y)
