import pyray as p

SCREEN_WIDTH: int = 1000
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Incremental Breakout Idle"
SCREEN_BACKGROUND: p.Color = p.SKYBLUE

ROWS: int = 10
COLS: int = 8
MARGIN: int = 100
BRICK_WIDTH: float = (SCREEN_WIDTH - (MARGIN * 2)) / COLS
BRICK_HEIGHT: float = (SCREEN_HEIGHT - (MARGIN * 2)) / ROWS
BRICK_GAP: int = 3