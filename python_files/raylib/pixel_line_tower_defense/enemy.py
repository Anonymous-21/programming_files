import pyray as p
import random


class Enemy:
    def __init__(self, spritesheet, sprite_dict, character_block_size) -> None:
        self.spritesheet = spritesheet
        self.sprite_dict = sprite_dict
        self.character_block_size = character_block_size

        self.bee_idle = self.sprite_dict["tile_0051.png"]
        self.bee_move = self.sprite_dict["tile_0052.png"]
        self.fly_idle = self.sprite_dict["tile_0053.png"]
        self.fly_move = self.sprite_dict["tile_0054.png"]
        self.worm_idle = self.sprite_dict["tile_0055.png"]
        self.worm_move = self.sprite_dict["tile_0056.png"]
        
        self.current_bee = self.bee_idle
        self.current_fly = self.fly_idle
        self.current_worm = self.worm_idle
        
        self.enemy_list = [self.current_bee, self.current_fly, self.current_worm]

        self.frames_counter = 0
        self.frames_speed = 8
        self.frame_num = 1
        self.speed = 1

        self.x_window = p.get_screen_width()
        self.y_window1 = 80
        self.y_window2 = 240
        self.y_window3 = 400
        self.y_window4 = 560
        
        random_enemy = random.choice(self.enemy_list)
        self.list1 = [[random_enemy, self.x_window, self.y_window1]]
        random_enemy = random.choice(self.enemy_list)
        self.list2 = [[random_enemy, self.x_window, self.y_window2]]
        random_enemy = random.choice(self.enemy_list)
        self.list3 = [[random_enemy, self.x_window, self.y_window3]]
        random_enemy = random.choice(self.enemy_list)
        self.list4 = [[random_enemy, self.x_window, self.y_window4]]
        self.counter = 0

    def draw(self):
        for enemy in self.list1:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    enemy[0][0],
                    enemy[0][1],
                    -enemy[0][2],
                    enemy[0][3],
                ),
                (enemy[1], enemy[2], self.character_block_size, self.character_block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list2:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    enemy[0][0],
                    enemy[0][1],
                    -enemy[0][2],
                    enemy[0][3],
                ),
                (enemy[1], enemy[2], self.character_block_size, self.character_block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list3:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    enemy[0][0],
                    enemy[0][1],
                    -enemy[0][2],
                    enemy[0][3],
                ),
                (enemy[1], enemy[2], self.character_block_size, self.character_block_size),
                (0, 0),
                0,
                p.WHITE,
            )
        for enemy in self.list4:
            p.draw_texture_pro(
                self.spritesheet,
                (
                    enemy[0][0],
                    enemy[0][1],
                    -enemy[0][2],
                    enemy[0][3],
                ),
                (enemy[1], enemy[2], self.character_block_size, self.character_block_size),
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
                
        # update enemy list
        self.enemy_list = [self.current_bee, self.current_fly, self.current_worm]

        # update enemy lists and select current enemy randomly
        self.counter += 1
        if self.counter >= 120:
            self.counter = 0
            random_enemy = random.choice(self.enemy_list)
            self.list1.append([random_enemy, self.x_window, self.y_window1])
            random_enemy = random.choice(self.enemy_list)
            self.list2.append([random_enemy, self.x_window, self.y_window2])
            random_enemy = random.choice(self.enemy_list)
            self.list3.append([random_enemy, self.x_window, self.y_window3])
            random_enemy = random.choice(self.enemy_list)
            self.list4.append([random_enemy, self.x_window, self.y_window4])

        # move enemy and remove offscreen enemy from list
        for enemy in self.list1:
            enemy[1] -= self.speed
            if enemy[1] < -self.character_block_size:
                self.list1.remove(enemy)
        for enemy in self.list2:
            enemy[1] -= self.speed
            if enemy[1] < -self.character_block_size:
                self.list2.remove(enemy)
        for enemy in self.list3:
            enemy[1] -= self.speed
            if enemy[1] < -self.character_block_size:
                self.list3.remove(enemy)
        for enemy in self.list4:
            enemy[1] -= self.speed
            if enemy[1] < -self.character_block_size:
                self.list4.remove(enemy)
