import pyray as p
from random import randint
from math import atan2, degrees, sqrt


class Enemy:
    def __init__(
        self, spritesheet: p.Texture, sprite_dict: dict[str, p.Rectangle]
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict
        
        self.health: int = 50
        self.damage: int = 1

        self.current_sprite: p.Rectangle = self.sprite_dict["enemy_A.png"]

        self.source: p.Rectangle = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest: p.Rectangle = p.Rectangle(
            randint(0, p.get_screen_width()),
            -100,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin: p.Vector2 = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0
        self.tint: p.Color = p.WHITE
        self.speed: float = 2
        
    def is_alive(self) -> bool:
        return self.health > 0
    
    def attack(self, target_x) -> None:
        target_x.health -= self.damage

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
        dx: float = target_x - self.dest.x
        dy: float = target_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self, target_x: float, target_y: float) -> None:
        distance_x: float = target_x - self.dest.x
        distance_y: float = target_y - self.dest.y
        distance: float = sqrt((distance_x**2) + (distance_y**2))

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

            self.dest.x += distance_x * self.speed
            self.dest.y += distance_y * self.speed

    def update(self, target_x: float, target_y: float) -> None:
        self.rotate(target_x, target_y)
        self.move(target_x, target_y)
