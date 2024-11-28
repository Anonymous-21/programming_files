#ifndef BRICKS_H
#define BRICKS_H

#include "constants.h"
#include "raylib.h"

typedef struct Brick {
  Vector2 coordinates;
  bool is_active;
} Brick;

typedef struct Bricks {
  Brick list[ROWS * COLS];
  Color color;

} Bricks;

void initBricks(Bricks *bricks);
void drawBricks(Bricks *bricks);

#endif // BRICKS_H
