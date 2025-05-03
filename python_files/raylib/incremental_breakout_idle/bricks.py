import pyray as p
from dataclasses import dataclass

from constants import ROWS, COLS, BRICK_WIDTH, BRICK_HEIGHT, BRICK_GAP, MARGIN


@dataclass
class Brick:
    rect: p.Rectangle
    color: p.Color
    thickness: float
    font_size: int
    level: int


class Bricks:
    def __init__(self, level: int) -> None:
        self.list: list[Brick] = []

        for i in range(ROWS):
            for j in range(COLS):
                x: int = j * (BRICK_WIDTH + BRICK_GAP) + MARGIN
                y: int = i * (BRICK_HEIGHT + BRICK_GAP) + MARGIN

                brick: Brick = Brick(
                    rect=p.Rectangle(x, y, BRICK_WIDTH, BRICK_HEIGHT),
                    color=p.BLACK,
                    thickness=5.0,
                    font_size=30,
                    level=level,
                )

                self.list.append(brick)

    def draw(self) -> None:
        for brick in self.list:
            p.draw_rectangle_lines_ex(brick.rect, brick.thickness, brick.color)
            # draw brick level
            text: str = str(brick.level)
            text_width: float = p.measure_text(text, brick.font_size)
            x: int = int(brick.rect.x + brick.rect.width / 2 - text_width/2)
            y: int = int(brick.rect.y + brick.rect.height/2 - brick.font_size/2)

            p.draw_text(text, x, y, brick.font_size, p.BLACK)
