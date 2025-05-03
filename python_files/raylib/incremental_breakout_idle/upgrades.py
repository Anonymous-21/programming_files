import pyray as p

from balls import Ball

class Upgrades:
  def __init__(self, ball: Ball, gold: int) -> None:
    self.ball: Ball = ball
    self.gold: int = gold

    
