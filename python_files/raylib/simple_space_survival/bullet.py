import pyray as p
from math import degrees, atan2, sqrt


class Bullet:
    def __init__(self, spritesheet, sprite_dict, owner_x, owner_y, target_x, target_y):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.target_x = target_x
        self.target_y = target_y

        self.current_sprite = self.sprite_dict["effect_yellow.png"]
        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            owner_x,
            owner_y,
            self.current_sprite.width - 20,
            self.current_sprite.height - 20,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE
        self.speed = 12

        distance_x = self.target_x - self.dest.x
        distance_y = self.target_y - self.dest.y
        distance = sqrt((distance_x**2) + (distance_y**2))

        if distance > 0:
            self.direction_x = distance_x / distance
            self.direction_y = distance_y / distance

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def update(self):
        # rotation
        dx = self.target_x - self.dest.x
        dy = self.target_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

        # movement
        self.dest.x += self.direction_x * self.speed
        self.dest.y += self.direction_y * self.speed
