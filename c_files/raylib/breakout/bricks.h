#ifndef BRICKS_H
#define BRICKS_H

#include "raylib.h"

#define GRID_MAX_LENGTH 100

typedef struct Bricks {
  int rows;
  int cols;
  int width;
  int height;
  int gap;
  Color color;
  Vector2 grid[GRID_MAX_LENGTH];
  int size;

} Bricks;

void initBricks(Bricks *bricks);
void genGrid(Bricks *bricks);
void drawBricks(Bricks *bricks);

#endif // BRICKS_H
