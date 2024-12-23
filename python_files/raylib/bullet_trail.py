import pyray as p
import math
from collections import deque

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bullet Trail"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Bullet:
    def __init__(self, target_x, target_y):
        self.x = p.get_screen_width() / 2
        self.y = p.get_screen_height() / 2
        self.radius = 4
        self.color = p.RED
        self.speed = 5

        distance_x = target_x - self.x
        distance_y = target_y - self.y
        distance = math.sqrt((distance_x**2) + (distance_y**2))

        self.direction_x = distance_x / distance
        self.direction_y = distance_y / distance

        self.trail_list = deque(maxlen=10)

    def draw(self):
        p.draw_circle_v((self.x, self.y), self.radius, self.color)

        for i in self.trail_list:
            trail_color = p.color_alpha(p.ORANGE, i[2])
            p.draw_circle_v((i[0], i[1]), self.radius, trail_color)

    def update(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

        self.trail_list.append([self.x, self.y, 1])

        for i in range(len(self.trail_list)):
            self.trail_list[i][2] -= 0.1


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    bullet_list = []

    while not p.window_should_close():
        if p.is_mouse_button_pressed(p.MouseButton.MOUSE_BUTTON_LEFT):
            bullet_list.append(Bullet(p.get_mouse_x(), p.get_mouse_y()))

        for bullet in bullet_list:
            bullet.update()

            if bullet.x <= 0 or bullet.x >= p.get_screen_width():
                bullet_list.remove(bullet)
            elif bullet.y <= 0 or bullet.y >= p.get_screen_height():
                bullet_list.remove(bullet)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        for bullet in bullet_list:
            bullet.draw()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
