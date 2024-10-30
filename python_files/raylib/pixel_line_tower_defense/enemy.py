import pyray as p
import random


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

        self.frames_counter = 0
        self.frames_speed = 8
        self.frame_num = 1
        self.speed = 3

        self.x_window = p.get_screen_width() + self.block_size
        self.y_window1 = 100
        self.y_window2 = 250
        self.y_window3 = 400
        self.y_window4 = 500
        self.list1 = [self.x_window, self.y_window1]
        self.list2 = [self.x_window, self.y_window2]
        self.list3 = [self.x_window, self.y_window3]
        self.list4 = [self.x_window, self.y_window4]
        self.counter = 0

        self.current_enemy1 = self.worm_idle
        self.current_enemy2 = self.worm_idle
        self.current_enemy3 = self.worm_idle
        self.current_enemy4 = self.worm_idle

    def draw(self):
        for enemy in self.list1:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_enemy1[0],
                    self.current_enemy1[1],
                    self.current_enemy1[2],
                    self.current_enemy1[3],
                ),
                (enemy[0], enemy[1], self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list2:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_enemy2[0],
                    self.current_enemy2[1],
                    self.current_enemy2[2],
                    self.current_enemy2[3],
                ),
                (enemy[0], enemy[1], self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list3:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_enemy3[0],
                    self.current_enemy3[1],
                    self.current_enemy3[2],
                    self.current_enemy3[3],
                ),
                (enemy[0], enemy[1], self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list4:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    self.current_enemy4[0],
                    self.current_enemy4[1],
                    self.current_enemy4[2],
                    self.current_enemy4[3],
                ),
                (enemy[0], enemy[1], self.block_size, self.block_size),
                (0, 0),
                0,
                p.WHITE,
            )

    def update(self):
        # set current frame
        match self.frame_num:
            case 1:
                self.current_bee = self.bee_idle
                self.current_fly = self.fly_idle
                self.current_worm = self.worm_idle
            case 2:
                self.current_bee = self.bee_move
                self.current_fly = self.fly_move
                self.current_worm = self.worm_move

        # enemy animation
        self.frames_counter += 1
        if self.frames_counter % self.frames_speed == 0:
            self.frames_counter = 0
            self.frame_num += 1
            if self.frame_num > 2:
                self.frame_num = 1

        # update enemy lists and select current enemy randomly
        self.counter += 1
        if self.counter >= 60:
            self.counter = 0
            self.list1.append([self.x_window, self.y_window1])
            self.current_enemy1 = random.choice(
                self.current_bee, self.current_fly, self.current_worm
            )
            self.list2.append([self.x_window, self.y_window2])
            self.current_enemy2 = random.choice(
                self.current_bee, self.current_fly, self.current_worm
            )
            self.list3.append([self.x_window, self.y_window3])
            self.current_enemy3 = random.choice(
                self.current_bee, self.current_fly, self.current_worm
            )
            self.list4.append([self.x_window, self.y_window4])
            self.current_enemy4 = random.choice(
                self.current_bee, self.current_fly, self.current_worm
            )

        # move enemy and remove offscreen enemy from list
        for enemy in self.list1:
            enemy[0] -= self.speed
            if enemy[0] < -self.block_size:
                self.list1.remove(enemy)
        for enemy in self.list2:
            enemy[0] -= self.speed
            if enemy[0] < -self.block_size:
                self.list2.remove(enemy)
        for enemy in self.list3:
            enemy[0] -= self.speed
            if enemy[0] < -self.block_size:
                self.list3.remove(enemy)
        for enemy in self.list4:
            enemy[0] -= self.speed
            if enemy[0] < -self.block_size:
                self.list4.remove(enemy)
