import pyray as p
from math import degrees, atan2, sqrt


class Enemy:
    def __init__(
        self,
        spritesheet: p.Texture,
        sprite_dict: dict[str, p.Rectangle],
        spawn_x: float,
        spawn_y: float,
        enemy_type: str = "basic",
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.enemy_type: str = enemy_type
        match self.enemy_type:
            case "basic":
                self.current_sprite: p.Rectangle = self.sprite_dict["enemy_A.png"]
                self.speed: float = 3
                self.health: float = 20
                self.damage: float = 1
                self.tint: p.Color = p.GRAY
            case "fast":
                self.current_sprite: p.Rectangle = self.sprite_dict["enemy_B.png"]
                self.speed: float = 5
                self.health: float = 10
                self.damage: float = 1
                self.tint: p.Color = p.YELLOW
            case "strong":
                self.current_sprite: p.Rectangle = self.sprite_dict["enemy_C.png"]
                self.speed: float = 2
                self.health: float = 40
                self.damage: float = 3
                self.tint: p.Color = p.GREEN
            case "tank":
                self.current_sprite: p.Rectangle = self.sprite_dict["enemy_D.png"]
                self.speed: float = 1
                self.health: float = 100
                self.damage: float = 5
                self.tint: p.Color = p.BLUE
            case "boss":
                self.current_sprite: p.Rectangle = self.sprite_dict["enemy_E.png"]
                self.speed: float = 1
                self.health: float = 200
                self.damage: float = 10
                self.tint: p.Color = p.RED

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            spawn_x,
            spawn_y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation: float = 0

    def is_alive(self) -> bool:
        return self.health > 0

    def draw(self) -> None:
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def rotate(self, player_dest_x: float, player_dest_y: float) -> None:
        dx: float = player_dest_x - self.dest.x
        dy: float = player_dest_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

    def move(self, player_dest_x: float, player_dest_y: float) -> None:
        distance_x: float = player_dest_x - self.dest.x
        distance_y: float = player_dest_y - self.dest.y
        distance: float = sqrt((distance_x**2) + (distance_y**2))
        if distance > 0:
            distance_x /= distance
            distance_y /= distance

            self.dest.x += distance_x * self.speed
            self.dest.y += distance_y * self.speed

    def update(self, player_dest_x: float, player_dest_y: float) -> None:
        self.rotate(player_dest_x, player_dest_y)
        self.move(player_dest_x, player_dest_y)
