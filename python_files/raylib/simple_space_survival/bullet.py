import pyray as p


class Bullet:
    def __init__(self, spritesheet, sprite_dict, player):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.player = player

        self.current_sprite = self.sprite_dict["effect_yellow.png"]
        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            player.x, player.y, self.current_sprite.width, self.current_sprite.height
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE

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
        