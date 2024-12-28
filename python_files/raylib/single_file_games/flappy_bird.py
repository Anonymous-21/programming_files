import pyray as p
import random


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Bird"
SCREEN_BACKGROUND = p.SKYBLUE
GAME_FPS = 60


def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)

    score = 0
    game_over = False

    rect = p.Rectangle(20, 20, 30, 30)
    rect_color = p.RED
    gravity = 1
    jump_force = -12
    change_y = 0

    vertical_gap = 150
    horitzontal_gap = 250

    pillar_x = p.get_screen_width()
    pillar_y = 0
    pillar_width = 50

    pillar_speed = 2
    pillar_color = p.DARKGREEN

    pillar_list = []

    while not p.window_should_close():
        if not game_over:
            if (
                len(pillar_list) <= 0
                or pillar_list[-1].x < p.get_screen_width() - horitzontal_gap
            ):
                random_height = random.randint(
                    vertical_gap, p.get_screen_height() - vertical_gap
                )

                pillar = p.Rectangle(pillar_x, pillar_y, pillar_width, random_height)
                pillar_list.append(pillar)

            for pillar in pillar_list:
                pillar.x -= pillar_speed

                # update score
                if rect.x == pillar.x + pillar.width:
                    score += 1

                if pillar.x + pillar.width < 0:
                    pillar_list.remove(pillar)

                # pillar collision rect
                if p.check_collision_recs(rect, pillar):
                    game_over = True
                elif p.check_collision_recs(
                    rect,
                    (
                        pillar.x,
                        pillar.height + vertical_gap,
                        pillar.width,
                        p.get_screen_height() - pillar.height - vertical_gap,
                    ),
                ):
                    game_over = True

            if p.is_key_pressed(p.KeyboardKey.KEY_UP):
                change_y = jump_force

            change_y += gravity
            rect.y += change_y

        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        p.draw_rectangle_rec(rect, rect_color)

        for pillar in pillar_list:
            p.draw_rectangle_rec(
                (pillar.x, pillar.y, pillar.width, pillar.height), pillar_color
            )
            p.draw_rectangle_rec(
                (
                    pillar.x,
                    pillar.height + vertical_gap,
                    pillar.width,
                    p.get_screen_height() - pillar.height - vertical_gap,
                ),
                pillar_color,
            )

        # draw score
        p.draw_text(str(score), 20, 20, 40, p.BLACK)

        if game_over:
            p.draw_text(
                "GAME OVER",
                p.get_screen_width() // 2 - 120,
                p.get_screen_height() // 2,
                40,
                p.BLACK,
            )
        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
