import pyray as p
from math import degrees, atan2, sqrt


class Weapon:
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        player_dest: p.Rectangle,
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.current_sprite: p.Rectangle = p.Rectangle(0, 0, 0, 0)

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            player_dest.x,
            player_dest.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0.0
        self.tint: p.Color = p.WHITE
        self.speed: float = 100.0

    def draw(self) -> None:
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, target_pos: p.Vector2) -> None:
        # Calculate the angle between the player and the mouse position
        dx: float = target_pos.x - self.dest.x
        dy: float = target_pos.y - self.dest.y
        angle_rad: float = atan2(dy, dx)
        self.rotation = degrees(angle_rad) + 90

    def move(self, target_pos: p.Vector2) -> None:
        distance_x: float = target_pos.x - self.dest.x
        distance_y: float = target_pos.y - self.dest.y
        distance: float = sqrt(distance_x ** 2 + distance_y ** 2)
        if distance > 0:
            distance_x /= distance
            distance_y /= distance

            self.dest.x += distance_x * self.speed * p.get_frame_time()
            self.dest.y += distance_y * self.speed * p.get_frame_time()

    def update(self, target_pos: p.Vector2) -> None:
        self.rotate(target_pos)
        self.move(target_pos)


class LaserBullet(Weapon):
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        player_dest: p.Rectangle,
    ) -> None:
        super().__init__(spritesheet, sprite_dict, player_dest)
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.current_sprite: p.Rectangle = sprite_dict["effect_yellow.png"]
        