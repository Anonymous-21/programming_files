import pyray as p
from math import sqrt
from tower import Tower
from enemy import Enemy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Idle Tower"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.tower = Tower(SCREEN_BACKGROUND)
        self.enemy = Enemy()

    def draw(self):
        self.tower.draw()
        self.enemy.draw()

    def update(self):
        self.enemy.update()
        for enemy in self.enemy.list:
            # enemy distance with tower
            distance_x = self.tower.x - enemy[0]
            distance_y = self.tower.y - enemy[1]
            distance = sqrt(distance_x**2 + distance_y**2)
            # normalize distance vectors
            if distance > 0:
                distance_x /= distance
                distance_y /= distance
            # move enemy
            if enemy[2] == self.enemy.small_width:
                enemy[0] += distance_x * self.enemy.small_speed
                enemy[1] += distance_y * self.enemy.small_speed
            elif enemy[2] == self.enemy.medium_width:
                enemy[0] += distance_x * self.enemy.medium_speed
                enemy[1] += distance_y * self.enemy.medium_speed
            # enemy collision tower
            if p.check_collision_recs(
                (enemy[0], enemy[1], enemy[2], enemy[3]),
                (self.tower.x, self.tower.y, self.tower.width, self.tower.height),
            ):
                if enemy[0] < self.tower.x - enemy[2]:
                    enemy[0] = self.tower.x - enemy[2]
                elif enemy[0] > self.tower.x + self.tower.width:
                    enemy[0] = self.tower.x + self.tower.width
                if enemy[1] < self.tower.y - enemy[3]:
                    enemy[1] = self.tower.y - enemy[3]
                elif enemy[1] > self.tower.y + self.tower.height:
                    enemy[1] = self.tower.y + self.tower.height


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
