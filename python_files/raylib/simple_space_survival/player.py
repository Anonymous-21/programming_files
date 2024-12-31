import pyray as p
from math import atan2, degrees


class Player:
    def __init__(
        self, spritesheet, sprite_dict, background_width, background_height
    ):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.background_width = background_width
        self.background_height = background_height

        self.current_sprite = self.sprite_dict["ship_A.png"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            self.background_width / 2,
            self.background_height / 2,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE
        self.speed = 5
        self.diagonal_speed = 0.7

    def draw(self):
        p.draw_texture_pro(
            self.spritesheet,
            self.source,
            self.dest,
            self.origin,
            self.rotation,
            self.tint,
        )

    def update(self, mouse_x, mouse_y):
        # rotation towards mouse
        dx = mouse_x - self.dest.x
        dy = mouse_y - self.dest.y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation += 90

        # movement
        
        # diagonal
        if p.is_key_down(p.KeyboardKey.KEY_W) and p.is_key_down(p.KeyboardKey.KEY_A):
            self.dest.x -= self.diagonal_speed
            self.dest.y -= self.diagonal_speed
        if p.is_key_down(p.KeyboardKey.KEY_W) and p.is_key_down(p.KeyboardKey.KEY_D):
            self.dest.x += self.diagonal_speed
            self.dest.y -= self.diagonal_speed
        if p.is_key_down(p.KeyboardKey.KEY_S) and p.is_key_down(p.KeyboardKey.KEY_A):
            self.dest.x -= self.diagonal_speed
            self.dest.y += self.diagonal_speed
        if p.is_key_down(p.KeyboardKey.KEY_S) and p.is_key_down(p.KeyboardKey.KEY_D):
            self.dest.x += self.diagonal_speed
            self.dest.y += self.diagonal_speed

        # rest of the directions
        if p.is_key_down(p.KeyboardKey.KEY_W):
            self.dest.y -= self.speed
        if p.is_key_down(p.KeyboardKey.KEY_S):
            self.dest.y += self.speed
        if p.is_key_down(p.KeyboardKey.KEY_A):
            self.dest.x -= self.speed
        if p.is_key_down(p.KeyboardKey.KEY_D):
            self.dest.x += self.speed

        # player boundary checks
        self.dest.x = max(self.dest.width/2, min(self.dest.x, self.background_width - self.dest.width/2))
        self.dest.y = max(self.dest.height/2, min(self.dest.y, self.background_height - self.dest.height/2))
