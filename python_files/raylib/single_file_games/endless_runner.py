import pyray as p
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
SCREEN_TITLE = "Runner"
SCREEN_BACKGROUND = p.SKYBLUE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    game_over = False
    score = 0

    rect = p.Rectangle(10, p.get_screen_height() - 30, 20, 30)
    rect_color = p.RED
    gravity = 1
    jump_force = -15
    change_y = 0
    jumping = False

    pillars = []
    pillar_width = 20
    pillar_x = p.get_screen_width()
    pillar_color = p.DARKGREEN
    current_pillar_gap = random.randint(100, 200)

    pillar_speed = 2

    while not p.window_should_close():
        if not game_over:
            if (
                len(pillars) <= 0
                or pillars[-1].x < p.get_screen_width() - current_pillar_gap
            ):
                pillar_height = random.randint(20, 50)
                pillar_y = p.get_screen_height() - pillar_height

                pillars.append(
                    p.Rectangle(pillar_x, pillar_y, pillar_width, pillar_height)
                )

                current_pillar_gap = random.randint(100, 200)

            for pillar in pillars:
                pillar.x -= pillar_speed

                if rect.x == pillar.x + pillar.width:
                    score += 1

                if p.check_collision_recs(rect, pillar):
                    game_over = True

                if pillar.x + pillar.width < 0:
                    pillars.remove(pillar)

            if p.is_key_pressed(p.KeyboardKey.KEY_UP) and not jumping:
                change_y = jump_force
                jumping = True

            if jumping:
                change_y += gravity
                rect.y += change_y

            if rect.y >= p.get_screen_height() - rect.height:
                jumping = False
                change_y = 0
                rect.y = p.get_screen_height() - rect.height

        elif game_over:
            if p.is_key_pressed(p.KeyboardKey.KEY_ENTER):
                score = 0
                game_over = False
                pillars = []

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        # draw score
        p.draw_text(str(score), 20, 10, 40, p.BLACK)

        p.draw_rectangle_rec(rect, rect_color)

        for pillar in pillars:
            p.draw_rectangle_rec(pillar, pillar_color)

        if game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 100,
                p.get_screen_height() // 2,
                40,
                p.BLACK,
            )

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
