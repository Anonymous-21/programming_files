import pyray as p
from math import sqrt, atan2, degrees


class Bullet:
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        spawn_x: float,
        spawn_y: float,
        target_x: float,
        target_y: float,
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.current_sprite: p.Rectangle = self.sprite_dict["effect_yellow.png"]

        self.source: p.Rectangle = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest: p.Rectangle = p.Rectangle(
            spawn_x,
            spawn_y,
            self.current_sprite.width - 20,
            self.current_sprite.height - 20,
        )
        self.origin: p.Vector2 = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotate()

        self.tint: p.Color = p.WHITE

        distance_x: float = target_x - self.dest.x
        distance_y: float = target_y - self.dest.y
        distance: float = sqrt((distance_x**2) + (distance_y**2))

        self.direction_x: float = distance_x / distance
        self.direction_y: float = distance_y / distance

        self.speed: float = 10

    def draw(self) -> None:
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
        self.rotation: float = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self) -> None:
        self.dest.x += self.direction_x * self.speed
        self.dest.y += self.direction_y * self.speed

    def update(self) -> None:
        self.move()
