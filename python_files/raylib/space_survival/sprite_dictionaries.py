import pyray as p


class Ships:
    def __init__(self, sprite_dict: dict[str, p.Rectangle]) -> None:
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.player_ships: dict[str, p.Rectangle] = {
            "blue1": self.sprite_dict["playerShip1_blue.png"],
            "blue2": self.sprite_dict["playerShip2_blue.png"],
            "blue3": self.sprite_dict["playerShip3_blue.png"],
            "green1": self.sprite_dict["playerShip1_green.png"],
            "green2": self.sprite_dict["playerShip2_green.png"],
            "green3": self.sprite_dict["playerShip3_green.png"],
            "orange1": self.sprite_dict["playerShip1_orange.png"],
            "orange2": self.sprite_dict["playerShip2_orange.png"],
            "orange3": self.sprite_dict["playerShip3_orange.png"],
            "red1": self.sprite_dict["playerShip1_red.png"],
            "red2": self.sprite_dict["playerShip2_red.png"],
            "red3": self.sprite_dict["playerShip3_red.png"],
        }

        self.enemy_ships: dict[str, p.Rectangle] = {
            "black1": self.sprite_dict["enemyBlack1.png"],
            "black2": self.sprite_dict["enemyBlack2.png"],
            "black3": self.sprite_dict["enemyBlack3.png"],
            "black4": self.sprite_dict["enemyBlack4.png"],
            "black5": self.sprite_dict["enemyBlack5.png"],
            "blue1": self.sprite_dict["enemyBlue1.png"],
            "blue2": self.sprite_dict["enemyBlue2.png"],
            "blue3": self.sprite_dict["enemyBlue3.png"],
            "blue4": self.sprite_dict["enemyBlue4.png"],
            "blue5": self.sprite_dict["enemyBlue5.png"],
            "green1": self.sprite_dict["enemyGreen1.png"],
            "green2": self.sprite_dict["enemyGreen2.png"],
            "green3": self.sprite_dict["enemyGreen3.png"],
            "green4": self.sprite_dict["enemyGreen4.png"],
            "green5": self.sprite_dict["enemyGreen5.png"],
            "red1": self.sprite_dict["enemyRed1.png"],
            "red2": self.sprite_dict["enemyRed2.png"],
            "red3": self.sprite_dict["enemyRed3.png"],
            "red4": self.sprite_dict["enemyRed4.png"],
            "red5": self.sprite_dict["enemyRed5.png"],
        }


class ShipDamages:
    def __init__(self, sprite_dict: dict) -> None:
        self.sprite_dict: dict[str, p.Rectangle] = sprite_dict

        self.ship_damage: dict[str, p.Rectangle] = {
            "damage1_1": self.sprite_dict["playerShip1_damage1.png"],
            "damage1_2": self.sprite_dict["playerShip1_damage2.png"],
            "damage1_3": self.sprite_dict["playerShip1_damage3.png"],
            "damage2_1": self.sprite_dict["playerShip2_damage1.png"],
            "damage2_2": self.sprite_dict["playerShip2_damage2.png"],
            "damage2_3": self.sprite_dict["playerShip2_damage3.png"],
            "damage3_1": self.sprite_dict["playerShip3_damage1.png"],
            "damage3_2": self.sprite_dict["playerShip3_damage2.png"],
            "damage3_3": self.sprite_dict["playerShip3_damage3.png"],
        }
