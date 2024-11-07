import pyray as p
import random
import math


class Enemy:
    def __init__(self, tower) -> None:
        self.tower = tower

        self.small_width = 20
        self.small_height = 20
        self.small_color = p.BLACK
        self.small_health = 2
        self.small_speed = 2
        self.small_damage = 1

        self.medium_width = 40
        self.medium_height = 40
        self.medium_color = p.ORANGE
        self.medium_health = 5
        self.medium_speed = 1
        self.medium_damage = 1

        self.large_width = 60
        self.large_height = 60
        self.large_color = p.RED
        self.large_health = 10
        self.large_speed = 0.5
        self.large_damage = 2

        self.boss_width = 100
        self.boss_height = 100
        self.boss_color = p.PURPLE
        self.boss_health = 100
        self.boss_speed = 0.1
        self.boss_damage = 5

        self.list = []

        self.update_list()

    def draw(self):
        for enemy in self.list:
            p.draw_rectangle_rec((enemy[0], enemy[1], enemy[2], enemy[3]), enemy[4])

    def update_list(self):
        # update enemy list with values
        for i in range(1, 51):
            coordinate1 = random.choice(
                [
                    -self.boss_width,
                    p.get_screen_width(),
                    -self.boss_health,
                    p.get_screen_height(),
                ]
            )
            if coordinate1 == -self.boss_width or coordinate1 == p.get_screen_width():
                coordinate2 = random.randint(0, p.get_screen_height())
            elif (
                coordinate1 == -self.boss_height or coordinate1 == p.get_screen_height()
            ):
                coordinate2 = coordinate1
                coordinate1 = random.randint(0, p.get_screen_width())

            if i % 4 == 0 or i % 8 == 0:
                self.list.append(
                    [
                        coordinate1,
                        coordinate2,
                        self.medium_width,
                        self.medium_height,
                        self.medium_color,
                    ]
                )
            elif i % 10 == 0 and i != 50:
                self.list.append(
                    [
                        coordinate1,
                        coordinate2,
                        self.large_width,
                        self.large_height,
                        self.large_color,
                    ]
                )
            elif i == 50:
                self.list.append(
                    [
                        coordinate1,
                        coordinate2,
                        self.boss_width,
                        self.boss_height,
                        self.boss_color,
                    ]
                )
            else:
                self.list.append(
                    [
                        coordinate1,
                        coordinate2,
                        self.small_width,
                        self.small_height,
                        self.small_color,
                    ]
                )

    def move(self):
        # enemy movement
        for enemy in self.list:
            distance_x = self.tower.x - enemy[0]
            distance_y = self.tower.y - enemy[1]
            distance = math.sqrt(distance_x**2 + distance_y**2)
            
            distance_x /= distance * 2
            distance_y /= distance * 2
            
            enemy[0] += distance_x
            enemy[1] += distance_y
