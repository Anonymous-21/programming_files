import pyray as p
from random import uniform

NUMBER_OF_STARS: int = 8
NUMBER_OF_METEORS: int = 2


class Background:
    def __init__(
        self, spritesheet: p.Texture, sprite_dict: dict[str, p.Rectangle]
    ) -> None:
        self.spritesheet: p.Texture = spritesheet
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.stars: dict[str, p.Rectangle] = {
            "tiny": self.sprite_dict["star_tiny.png"],
            "small": self.sprite_dict["star_small.png"],
            "medium": self.sprite_dict["star_medium.png"],
            "large": self.sprite_dict["star_large.png"],
        }
        self.meteors: dict[str, p.Rectangle] = {
            "detailed_large": self.sprite_dict["meteor_detailedLarge.png"],
            "detailed_small": self.sprite_dict["meteor_detailedSmall.png"],
            "large": self.sprite_dict["meteor_large.png"],
            "small": self.sprite_dict["meteor_small.png"],
            "square_detailed_large": self.sprite_dict["meteor_squareDetailedLarge.png"],
            "square_detailed_small": self.sprite_dict["meteor_squareDetailedSmall.png"],
            "square_large": self.sprite_dict["meteor_squareLarge.png"],
            "square_small": self.sprite_dict["meteor_squareSmall.png"],
        }

        self.star_current: p.Rectangle = self.stars["small"]
        self.star_source: p.Rectangle = p.Rectangle(
            self.star_current.x,
            self.star_current.y,
            self.star_current.width,
            self.star_current.height,
        )
        self.star_list: list[p.Vector2] = []
        for i in range(NUMBER_OF_STARS):
            x: float = uniform(0, p.get_screen_width())
            y: float = uniform(0, p.get_screen_height())

            self.star_list.append(p.Vector2(x, y))

        self.star_tint: p.Color = p.WHITE
        self.star_speed: float = 1.0
        
        self.meteor_current: p.Rectangle = self.meteors["square_detailed_large"]
        self.meteor_source: p.Rectangle = p.Rectangle(
            self.meteor_current.x,
            self.meteor_current.y,
            self.meteor_current.width,
            self.meteor_current.height,
        )
        self.meteor_list: list[p.Vector2] = []
        for i in range(NUMBER_OF_METEORS):
            x: float = uniform(0, p.get_screen_width())
            y: float = uniform(0, p.get_screen_height())

            self.meteor_list.append(p.Vector2(x, y))

        self.meteor_tint: p.Color = p.BROWN
        self.meteor_speed: float = 1.0

    def draw(self) -> None:
        for star in self.star_list:
            p.draw_texture_rec(
                self.spritesheet,
                self.star_source,
                p.Vector2(star.x, star.y),
                self.star_tint,
            )
        for meteor in self.meteor_list:
            p.draw_texture_rec(
                self.spritesheet,
                self.meteor_source,
                p.Vector2(meteor.x, meteor.y),
                self.meteor_tint,
            )

    def move(self) -> None:
        for star in self.star_list:
            star.y += self.star_speed

            if star.y > p.get_screen_height() + self.star_current.height:
                star.x = uniform(0, p.get_screen_width())
                star.y = 0
                
        for meteor in self.meteor_list:
            meteor.y += self.meteor_speed

            if meteor.y > p.get_screen_height() + self.meteor_current.height:
                meteor.x = uniform(0, p.get_screen_width())
                meteor.y = 0

    def update(self) -> None:
        self.move()
