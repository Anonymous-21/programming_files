import pyray as p
import csv
import os

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/pixel_line_platformer")


class Levels:
    def __init__(self, spritesheet, sprite_dict, rows, cols, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict

        self.rows = rows
        self.cols = cols
        self.block_size = block_size

        self.current_level = 1
        self.level1_pass = False
        self.level1 = []
        with open("levels/level1.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for i in csvreader:
                row = []
                for j in i:
                    row.append(int(j))
                self.level1.append(row)

        self.level1_single_digit = []
        for row in self.level1:
            for col in row:
                if col < 10:
                    self.level1_single_digit.append(col)
                    
        self.update()

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x_window = j * self.block_size
                y_window = i * self.block_size

                if self.level[i][j] in self.level_single_digit:
                    self.current_frame = self.sprite_dict[
                        f"tile_000{self.level1[i][j]}.png"
                    ]
                else:
                    self.current_frame = self.sprite_dict[
                        f"tile_00{self.level1[i][j]}.png"
                    ]

                p.draw_texture_pro(
                    self.spritesheet,
                    (
                        self.current_frame[0],
                        self.current_frame[1],
                        self.current_frame[2],
                        self.current_frame[3],
                    ),
                    (
                        x_window,
                        y_window,
                        self.block_size,
                        self.block_size,
                    ),
                    (self.current_frame[2] / 2, self.current_frame[3] / 2),
                    0,
                    p.WHITE,
                )
                
    def update(self):
        # update current level
        match self.current_level:
            case 1:
                self.level = self.level1
                self.level_single_digit = self.level1_single_digit