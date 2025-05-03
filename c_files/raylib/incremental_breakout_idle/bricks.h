#ifndef BRICKS_H
#define BRICKS_H

#include <raylib.h>
#include "constants.h"

typedef struct Brick
{
  Rectangle rect;
  Color color;
  float thickness;
  bool active;
  int level;

}Brick;

typedef struct Bricks
{
  Brick list[ROWS * COLS];

}Bricks;

void bricks_init(Bricks *bricks, int brick_level);
void bricks_draw(Bricks *bricks);

#endif // BRICKS_H
