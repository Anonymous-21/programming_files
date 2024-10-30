import pyray as p


class Enemy:
    def __init__(self, spritesheet, sprite_dict, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.block_size = block_size
        
        self.bee_idle = self.sprite_dict["tile_0051.png"]
        self.bee_move = self.sprite_dict["tile_0052.png"]
        self.fly_idle = self.sprite_dict["tile_0053.png"]
        self.fly_move = self.sprite_dict["tile_0054.png"]
        self.worm_idle = self.sprite_dict["tile_0055.png"]
        self.worm_move = self.sprite_dict["tile_0056.png"]
        
        