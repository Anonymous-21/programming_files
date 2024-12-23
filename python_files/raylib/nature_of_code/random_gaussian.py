import pyray as p
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Random Guassian"
SCREEN_BACKGROUND = p.BLACK
GAME_FPS = 60

def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)


    while not p.window_should_close():
        mean = SCREEN_WIDTH/2
        sd = 60
        x = random.gauss(mean, sd)

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_circle_v((x, SCREEN_HEIGHT/2), 10, p.fade(p.WHITE, 10))

        p.end_drawing()

    p.close_window()

if __name__ == "__main__":
    main()