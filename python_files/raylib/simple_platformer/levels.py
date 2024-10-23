import pyray as p
import os
import csv

os.chdir(
    "/home/anonymous/Downloads/programming_files/python_files/raylib/simple_platformer"
)


class Levels:
    def __init__(self, spritesheet, sprite_dict) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.rows = 20
        self.cols = 30
        self.block_size = 48

        self.current_level = 1
        self.level = []

        self.level1_pass = False
        self.level1 = []

        with open("levels/level1.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for i in csvreader:
                row = []
                for j in i:
                    row.append(int(j))
                self.level1.append(row)

        # get all one digit numbers from level1
        self.level1_one_digit = []
        for row in self.level1:
            for col in row:
                if col < 10:
                    self.level1_one_digit.append(col)

        self.update()

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.block_size
                y = i * self.block_size

                if self.level[i][j] in self.level1_one_digit:
                    self.sprite = self.sprite_dict[f"tile_000{self.level[i][j]}.png"]
                else:
                    self.sprite = self.sprite_dict[f"tile_00{self.level[i][j]}.png"]

                p.draw_texture_pro(
                    self.spritesheet,
                    (self.sprite[0], self.sprite[1], self.sprite[2], self.sprite[3]),
                    (x, y, self.sprite[2] * 3, self.sprite[3] * 3),
                    (self.sprite[2] / 2, self.sprite[3] / 2),
                    0,
                    p.WHITE,
                )

    def update(self):
        match self.current_level:
            case 1:
                self.level = self.level1
