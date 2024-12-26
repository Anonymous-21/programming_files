import pyray as p
from math import sqrt, atan2, degrees


class Laser:
    def __init__(self, spritesheet, sprite_dict, spawn_x, spawn_y, target_x, target_y):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.target_x = target_x
        self.target_y = target_y

        # self.lasers = [self.sprite_dict["laserRed06.png"]]
        self.lasers = {
            "blue1": self.sprite_dict["laserBlue01.png"],
            "blue2": self.sprite_dict["laserBlue02.png"],
            "blue3": self.sprite_dict["laserBlue03.png"],
            "blue4": self.sprite_dict["laserBlue04.png"],
            "blue5": self.sprite_dict["laserBlue05.png"],
            "blue6": self.sprite_dict["laserBlue06.png"],
            "blue7": self.sprite_dict["laserBlue07.png"],
            "blue8": self.sprite_dict["laserBlue08.png"],
            "blue9": self.sprite_dict["laserBlue09.png"],
            "blue10": self.sprite_dict["laserBlue10.png"],
            "blue11": self.sprite_dict["laserBlue11.png"],
            "blue12": self.sprite_dict["laserBlue12.png"],
            "blue13": self.sprite_dict["laserBlue13.png"],
            "blue14": self.sprite_dict["laserBlue14.png"],
            "blue15": self.sprite_dict["laserBlue15.png"],
            "blue16": self.sprite_dict["laserBlue16.png"],
            "green1": self.sprite_dict["laserGreen01.png"],
            "green2": self.sprite_dict["laserGreen02.png"],
            "green3": self.sprite_dict["laserGreen03.png"],
            "green4": self.sprite_dict["laserGreen04.png"],
            "green5": self.sprite_dict["laserGreen05.png"],
            "green6": self.sprite_dict["laserGreen06.png"],
            "green7": self.sprite_dict["laserGreen07.png"],
            "green8": self.sprite_dict["laserGreen08.png"],
            "green9": self.sprite_dict["laserGreen09.png"],
            "green10": self.sprite_dict["laserGreen10.png"],
            "green11": self.sprite_dict["laserGreen11.png"],
            "green12": self.sprite_dict["laserGreen12.png"],
            "green13": self.sprite_dict["laserGreen13.png"],
            "green14": self.sprite_dict["laserGreen14.png"],
            "green15": self.sprite_dict["laserGreen15.png"],
            "green16": self.sprite_dict["laserGreen16.png"],
            "red1": self.sprite_dict["laserRed01.png"],
            "red2": self.sprite_dict["laserRed02.png"],
            "red3": self.sprite_dict["laserRed03.png"],
            "red4": self.sprite_dict["laserRed04.png"],
            "red5": self.sprite_dict["laserRed05.png"],
            "red6": self.sprite_dict["laserRed06.png"],
            "red7": self.sprite_dict["laserRed07.png"],
            "red8": self.sprite_dict["laserRed08.png"],
            "red9": self.sprite_dict["laserRed09.png"],
            "red10": self.sprite_dict["laserRed10.png"],
            "red11": self.sprite_dict["laserRed11.png"],
            "red12": self.sprite_dict["laserRed12.png"],
            "red13": self.sprite_dict["laserRed13.png"],
            "red14": self.sprite_dict["laserRed14.png"],
            "red15": self.sprite_dict["laserRed15.png"],
            "red16": self.sprite_dict["laserRed16.png"],
        }
        self.current_sprite = self.lasers["red6"]

        self.source = p.Rectangle(
            self.current_sprite.x,
            self.current_sprite.y,
            self.current_sprite.width,
            self.current_sprite.height,
        )
        self.dest = p.Rectangle(
            spawn_x, spawn_y, self.current_sprite.width, self.current_sprite.height
        )
        self.origin = p.Vector2(self.dest.width / 2, self.dest.height / 2)
        self.rotation = 0
        self.tint = p.WHITE
        self.speed = 12

        distance_x = self.target_x - self.dest.x
        distance_y = self.target_y - self.dest.y
        distance = sqrt((distance_x**2) + (distance_y**2))

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

    def rotate(self):
        dx = self.dest.x - self.target_x
        dy = self.dest.y - self.target_y
        self.rotation = degrees(atan2(dy, dx))
        self.rotation -= 90

    def move(self):
        self.dest.x += self.direction_x * self.speed
        self.dest.y += self.direction_y * self.speed

    def update(self):
        self.rotate()
        self.move()
