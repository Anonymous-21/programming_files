import pyray as p
from math import sqrt, degrees, atan2


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

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            spawn_x,
            spawn_y,
            self.current_sprite.width - 20,
            self.current_sprite.height - 20,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0
        self.tint: p.Color = p.WHITE
        self.speed: float = 12

        distance_x: float = target_x - spawn_x
        distance_y: float = target_y - spawn_y
        distance: float = sqrt((distance_x**2) + (distance_y**2))
        if distance > 0:
            self.direction_x: float = distance_x / distance
            self.direction_y: float = distance_y / distance

        self.has_rotated: bool = False

        self.damage: float = 1

    def draw(self) -> None:
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
        self.dest.x += self.direction_x * self.speed
        self.dest.y += self.direction_y * self.speed

    def update(self, mouse_x: float, mouse_y: float) -> None:
        if not self.has_rotated:
            self.rotate(mouse_x, mouse_y)
            self.has_rotated = True
            
        self.move()
