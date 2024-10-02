import raylib as r


class Player:
    def __init__(self, sprite_dict) -> None:
        self.sprite_dict = sprite_dict
        self.alien_biege = {
            "climb1": "alienBeige_climb1.png",
            "climb2": "alienBeige_climb2.png",
            "duck": "alienBeige_duck.png",
            "front": "alienBeige_front.png",
            "hit": "alienBeige_hit.png",
            "jump": "alienBeige_jump.png",
            "stand": "alienBeige_stand.png",
            "swim1": "alienBeige_swim1.png",
            "swim2": "alienBeige_swim2.png",
            "walk1": "alienBeige_walk1.png",
            "walk2": "alienBeige_walk2.png",
        }
        self.alien_blue = {
            "climb1": "alienBlue_climb1.png",
            "climb2": "alienBlue_climb2.png",
            "duck": "alienBlue_duck.png",
            "front": "alienBlue_front.png",
            "hit": "alienBlue_hit.png",
            "jump": "alienBlue_jump.png",
            "stand": "alienBlue_stand.png",
            "swim1": "alienBlue_swim1.png",
            "swim2": "alienBlue_swim2.png",
            "walk1": "alienBlue_walk1.png",
            "walk2": "alienBlue_walk2.png",
        }
        self.alien_green = {
            "climb1": "alienGreen_climb1.png",
            "climb2": "alienGreen_climb2.png",
            "duck": "alienGreen_duck.png",
            "front": "alienGreen_front.png",
            "hit": "alienGreen_hit.png",
            "jump": "alienGreen_jump.png",
            "stand": "alienGreen_stand.png",
            "swim1": "alienGreen_swim1.png",
            "swim2": "alienGreen_swim2.png",
            "walk1": "alienGreen_walk1.png",
            "walk2": "alienGreen_walk2.png",
        }
        self.alien_pink = {
            "climb1": "alienPink_climb1.png",
            "climb2": "alienPink_climb2.png",
            "duck": "alienPink_duck.png",
            "front": "alienPink_front.png",
            "hit": "alienPink_hit.png",
            "jump": "alienPink_jump.png",
            "stand": "alienPink_stand.png",
            "swim1": "alienPink_swim1.png",
            "swim2": "alienPink_swim2.png",
            "walk1": "alienPink_walk1.png",
            "walk2": "alienPink_walk2.png",
        }
        self.alien_yellow = {
            "climb1": "alienYellow_climb1.png",
            "climb2": "alienYellow_climb2.png",
            "duck": "alienYellow_duck.png",
            "front": "alienYellow_front.png",
            "hit": "alienYellow_hit.png",
            "jump": "alienYellow_jump.png",
            "stand": "alienYellow_stand.png",
            "swim1": "alienYellow_swim1.png",
            "swim2": "alienYellow_swim2.png",
            "walk1": "alienYellow_walk1.png",
            "walk2": "alienYellow_walk2.png",
        }

    def draw(self):
        pass
