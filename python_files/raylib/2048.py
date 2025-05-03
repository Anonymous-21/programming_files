import pyray as p
from dataclasses import dataclass
from math import copysign

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = SCREEN_WIDTH
SCREEN_TITLE: str = "2048"
SCREEN_BACKGROUND: p.Color = p.RAYWHITE

ROWS: int = 4
COLS: int = ROWS
BLOCK_WIDTH: int = SCREEN_WIDTH / COLS
BLOCK_HEIGHT: int = SCREEN_HEIGHT / ROWS


@dataclass
class Block:
    rect: p.Rectangle
    color: p.Color
    thickness: float
    value: int


class Game:
    def __init__(self) -> None:
        self.blocks: list[Block] = []

        initial_blocks: int = 2
        for i in range(initial_blocks):
            random_x: float = p.get_random_value(0, COLS - 1) * BLOCK_WIDTH
            random_y: float = p.get_random_value(0, ROWS - 1) * BLOCK_HEIGHT

            block: Block = Block(
                rect=p.Rectangle(random_x, random_y, BLOCK_WIDTH, BLOCK_HEIGHT),
                color=p.BLACK,
                thickness=5.0,
                value=2,
            )

            self.blocks.append(block)

    def draw(self) -> None:
        for block in self.blocks:
            # center text in block
            text: str = str(block.value)
            font_size: float = 40
            text_width: int = p.measure_text(text, font_size)
            text_color: p.Color = p.BLACK

            p.draw_text(
                text,
                int(block.rect.x + block.rect.width / 2 - text_width / 2),
                int(block.rect.y + block.rect.height / 2 - font_size / 2),
                font_size,
                text_color,
            )

            # draw block
            p.draw_rectangle_lines_ex(block.rect, block.thickness, block.color)

    def update(self) -> None:
        for block in self.blocks:
            # block bounds
            block.rect.x = max(
                0, min(block.rect.x, p.get_screen_width() - block.rect.width)
            )
            block.rect.y = max(
                0, min(block.rect.y, p.get_screen_height() - block.rect.height)
            )

            # get input and move blocks
            if p.is_key_down(p.KeyboardKey.KEY_LEFT):
                block.rect.x -= BLOCK_WIDTH
            if p.is_key_down(p.KeyboardKey.KEY_RIGHT):
                block.rect.x += BLOCK_WIDTH
            if p.is_key_down(p.KeyboardKey.KEY_UP):
                block.rect.y -= BLOCK_WIDTH
            if p.is_key_down(p.KeyboardKey.KEY_DOWN):
                block.rect.y += BLOCK_WIDTH

            # collision and resolution
            for other_block in self.blocks[:]:
                if p.check_collision_recs(block.rect, other_block.rect):
                    if block.value == other_block.value:
                        block.value += other_block.value
                        self.blocks.remove(other_block)
                else:
                    # center of block and other block
                    block_center: p.Vector2 = p.Vector2(
                        block.rect.x + block.rect.width / 2,
                        block.rect.y + block.rect.height / 2,
                    )
                    other_block_center: p.Vector2 = p.Vector2(
                        other_block.rect.x + other_block.rect.width / 2,
                        other_block.rect.y + other_block.rect.height / 2,
                    )

                    # current distance between blocks
                    current_distance: p.Vector2 = p.vector2_subtract(
                        block_center, other_block_center
                    )

                    # min distance to maintain between blocks
                    min_distance: p.Vector2 = p.Vector2(
                        block.rect.width / 2 + other_block.rect.width / 2,
                        block.rect.height / 2 + other_block.rect.height / 2,
                    )

                    #
                    if min_distance.x < min_distance.y:
                        offset: p.Vector2 = p.Vector2(
                            min_distance.x - abs(current_distance.x),
                            min_distance.y - abs(current_distance.y),
                        )
                        block.rect.x += copysign(offset.x, current_distance.x)
                        block.rect.y += copysign(offset.y, current_distance.y)


def main() -> None:
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    game: Game = Game()

    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)

        game.draw()
        game.update()

        p.end_drawing()

    p.close_window()


if __name__ == "__main__":
    main()
