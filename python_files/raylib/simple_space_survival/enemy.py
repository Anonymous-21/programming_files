import pyray as p


class Enemy:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.current_sprite = sprite_dict["enemy_A.png"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            0, 0, self.current_sprite.width, self.current_sprite.height
        )
        self.origin = p.Vector2(self.dest.width/2, self.dest.height/2)
        self.rotation = 0
        self.tint = p.WHITE

    def draw(self):
        p.draw_texture_pro(self.spritesheet, self.source, self.dest, self.origin, self.rotation, self.tint)

    def update(self):
        pass
