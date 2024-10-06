import pyray as pr


class Font:
    def __init__(self, spritesheet, sprite_dict):
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.game_over = self.sprite_dict["textGameOver.png"]
        self.game_over_width = self.game_over[2]
        self.game_over_height = self.game_over[3]
        self.get_ready = self.sprite_dict["textGetReady.png"]
        self.get_ready_width = self.get_ready[2]
        self.get_ready_height = self.get_ready[3]

        self.letters = {
            "a": self.sprite_dict["letterA.png"],
            "b": self.sprite_dict["letterB.png"],
            "c": self.sprite_dict["letterC.png"],
            "d": self.sprite_dict["letterD.png"],
            "e": self.sprite_dict["letterE.png"],
            "f": self.sprite_dict["letterF.png"],
            "g": self.sprite_dict["letterG.png"],
            "h": self.sprite_dict["letterH.png"],
            "i": self.sprite_dict["letterI.png"],
            "j": self.sprite_dict["letterJ.png"],
            "k": self.sprite_dict["letterK.png"],
            "l": self.sprite_dict["letterL.png"],
            "m": self.sprite_dict["letterM.png"],
            "n": self.sprite_dict["letterN.png"],
            "o": self.sprite_dict["letterO.png"],
            "p": self.sprite_dict["letterP.png"],
            "q": self.sprite_dict["letterQ.png"],
            "r": self.sprite_dict["letterR.png"],
            "s": self.sprite_dict["letterS.png"],
            "t": self.sprite_dict["letterT.png"],
            "u": self.sprite_dict["letterU.png"],
            "v": self.sprite_dict["letterV.png"],
            "w": self.sprite_dict["letterW.png"],
            "x": self.sprite_dict["letterX.png"],
            "y": self.sprite_dict["letterY.png"],
            "z": self.sprite_dict["letterZ.png"],
        }
        self.letters_width = (self.letters["a"])[2]
        self.letters_height = (self.letters["a"])[3]

        self.numbers = {
            0: self.sprite_dict["number0.png"],
            1: self.sprite_dict["number1.png"],
            2: self.sprite_dict["number2.png"],
            3: self.sprite_dict["number3.png"],
            4: self.sprite_dict["number4.png"],
            5: self.sprite_dict["number5.png"],
            6: self.sprite_dict["number6.png"],
            7: self.sprite_dict["number7.png"],
            8: self.sprite_dict["number8.png"],
            9: self.sprite_dict["number9.png"],
        }
        self.numbers_width = (self.numbers[0])[2]
        self.numbers_height = (self.numbers[0])[3]

    def draw_numbers(self, number, position_vector, tint=pr.WHITE):
        pr.draw_texture_rec(self.spritesheet, self.numbers[number], position_vector, tint)

    def draw_letters(self, letter, position_vector, tint=pr.WHITE):
        pr.draw_texture_rec(
            self.spritesheet, self.letters[str(letter)], position_vector, tint
        )

    def draw_game_over(self):
        pr.draw_texture_rec(
            self.spritesheet,
            self.game_over,
            (
                pr.get_screen_width() / 2 - self.game_over_width / 2,
                pr.get_screen_height() / 2 - self.game_over_height / 2,
            ),
            pr.WHITE,
        )

    def draw_get_ready(self):
        pr.draw_texture_rec(
            self.spritesheet,
            self.get_ready,
            (
                pr.get_screen_width() / 2 - self.get_ready_width / 2,
                pr.get_screen_height() / 2 - self.get_ready_height / 2,
            ),
            pr.WHITE,
        )
