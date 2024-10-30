import pyray as p
import csv
import os

os.chdir("/home/anonymous/Downloads/programming_files/python_files/raylib/pixel_line_tower_defense")


class Map:
    def __init__(self, spritesheet, sprite_dict, rows, cols, block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.rows = rows
        self.cols = cols
        self.block_size = block_size
        
        self.map = []
        with open("map.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for i in csv_reader:
                row = []
                for j in i:
                    row.append(int(j))
                self.map.append(row)
                
        self.map_single_digit = []
        for row in self.map:
            for col in row:
                if col < 10:
                    self.map_single_digit.append(col)
                    
    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x_window = col * self.block_size
                y_window = row * self.block_size
                
                if self.map[row][col] in self.map_single_digit:
                    self.current_frame = self.sprite_dict[f"tile_000{self.map[row][col]}.png"]
                else:
                    self.current_frame = self.sprite_dict[f"tile_00{self.map[row][col]}.png"]
                    
                p.draw_texture_pro(self.spritesheet,
                                   (self.current_frame[0], self.current_frame[1], self.current_frame[2], self.current_frame[3]),
                                   (x_window, y_window, self.block_size, self.block_size),
                                   (0, 0),
                                   0,
                                   p.WHITE)
