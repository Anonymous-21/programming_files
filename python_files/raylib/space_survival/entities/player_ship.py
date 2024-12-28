import pyray as p
from math import atan2, degrees

from sprite_dictionaries import Ships


class PlayerShip:
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        speed: float,
        ship_type: int,
        color: str,
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.ships: Ships = Ships(self.sprite_dict)

        self.ship_sprite_loader(ship_type, color)

        self.source: p.Rectangle = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest: p.Rectangle = p.Rectangle(
            p.get_screen_width() / 2,
            p.get_screen_height() / 2,
            self.current_sprite.width / 2,
            self.current_sprite.height / 2,
        )
        self.origin: p.Vector2 = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0
        self.tint: p.Color = p.WHITE

        self.speed: float = speed

    def ship_sprite_loader(self, ship_type: int, color: str) -> None:
        self.current_sprite = self.ships.player_ships[f"{color.lower()}{ship_type}"]

    def draw(self) -> None:
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, target_x: float, target_y: float) -> None:
        """Rotate player sprite towards target (ex: mouse cursor)"""

        dx: float = target_x - self.dest.x
        dy: float = target_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self) -> None:
        if p.is_key_down(p.KeyboardKey.KEY_A) and self.dest.x >= 0:
            self.dest.x -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_D)
            and self.dest.x <= p.get_screen_width() - self.dest.width
        ):
            self.dest.x += self.speed
        elif p.is_key_down(p.KeyboardKey.KEY_W) and self.dest.y >= 0:
            self.dest.y -= self.speed
        elif (
            p.is_key_down(p.KeyboardKey.KEY_S)
            and self.dest.y <= p.get_screen_height() - self.dest.height
        ):
            self.dest.y += self.speed

    def update(self, target_x: float, target_y: float) -> None:
        self.rotate(target_x, target_y)
        self.move()

