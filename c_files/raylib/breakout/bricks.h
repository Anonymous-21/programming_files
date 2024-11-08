#ifndef BRICKS_H
#define BRICKS_H

#include "raylib.h"

#define ROWS 5
#define COLS 10

typedef struct Bricks {
  int rows;
  int cols;
  int width;
  int height;
  Color color;
  int gap;
  Vector2 list[ROWS][COLS];

} Bricks;

void initBricks(Bricks *bricks);
void genBricks(Bricks *bricks);
void drawBricks(Bricks *Bricks);

#endif // BRICKS_H
