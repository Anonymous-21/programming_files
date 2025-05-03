import pyray as p
from abc import ABC
import random
import math


class Ball(ABC):
    def __init__(self) -> None:
        self.pos: p.Vector2 = p.Vector2(self.radius + 20, self.radius)
        self.direction: p.Vector2 = p.Vector2(1, 1)

    def draw(self) -> None:
        p.draw_circle_v(self.pos, self.radius, self.color)

    def update(self) -> None:
        if abs(self.pos.x) > 0.01 and abs(self.pos.y) > 0.01:
            self.direction = p.vector2_normalize(self.direction)

        # move ball
        self.pos.x += self.direction.x * self.speed * p.get_frame_time()
        self.pos.y += self.direction.y * self.speed * p.get_frame_time()

        # ball bounds
        if self.pos.x < self.radius or self.pos.x > p.get_screen_width() - self.radius:
            self.direction.x *= -1
        if self.pos.y < self.radius or self.pos.y > p.get_screen_height() - self.radius:
            self.direction.y *= -1


class BallNormal(Ball):
    def __init__(self) -> None:
        self.radius: float = 10.0
        self.speed: float = 250.0
        self.color: p.Color = p.RED
        self.damage: int = 1

        super().__init__()
