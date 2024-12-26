import pyray as p
from random import randint


class Background:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.star = self.sprite_dict["star1.png"]

        self.star_list = []
        for i in range(10):
            random_x = randint(0, p.get_screen_width())
            random_y = randint(0, p.get_screen_height())
            self.star_list.append(p.Vector2(random_x, random_y))

        self.star_source = p.Rectangle(
            self.star.x, self.star.y, self.star.width, self.star.height
        )
        self.star_tint = p.WHITE
        self.star_speed = 2

        self.meteors = {
            "brown_big1": self.sprite_dict["meteorBrown_big1.png"],
            "brown_big2": self.sprite_dict["meteorBrown_big2.png"],
            "brown_big3": self.sprite_dict["meteorBrown_big3.png"],
            "brown_big4": self.sprite_dict["meteorBrown_big4.png"],
            "brown_med1": self.sprite_dict["meteorBrown_med1.png"],
            "brown_med2": self.sprite_dict["meteorBrown_med3.png"],
            "brown_small1": self.sprite_dict["meteorBrown_small1.png"],
            "brown_small2": self.sprite_dict["meteorBrown_small2.png"],
            "brown_tiny1": self.sprite_dict["meteorBrown_tiny1.png"],
            "brown_tiny2": self.sprite_dict["meteorBrown_tiny2.png"],
            "grey_big1": self.sprite_dict["meteorGrey_big1.png"],
            "grey_big2": self.sprite_dict["meteorGrey_big2.png"],
            "grey_big3": self.sprite_dict["meteorGrey_big3.png"],
            "grey_big4": self.sprite_dict["meteorGrey_big4.png"],
            "grey_med1": self.sprite_dict["meteorGrey_med1.png"],
            "grey_med2": self.sprite_dict["meteorGrey_med2.png"],
            "grey_small1": self.sprite_dict["meteorGrey_small1.png"],
            "grey_small2": self.sprite_dict["meteorGrey_small2.png"],
            "grey_tiny1": self.sprite_dict["meteorGrey_tiny1.png"],
            "grey_tiny2": self.sprite_dict["meteorGrey_tiny2.png"],
        }

    def draw(self):
        for star in self.star_list:
            p.draw_texture_rec(self.spritesheet, self.star_source, star, self.star_tint)

    def update(self):
        # move and update stars vertically on screen
        for star in self.star_list:
            star.y += self.star_speed

            if star.y > p.get_screen_height():
                x = randint(0, p.get_screen_width())
                y = 0
                index = self.star_list.index(star)

                self.star_list[index] = p.Vector2(x, y)
