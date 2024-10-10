#ifndef BRICKS_H
#define BRICKS_H

#include "raylib.h"

#define LIST_ROW_LENGTH 5
#define LIST_COL_LENGTH 10

typedef struct Ball Ball;

typedef struct Bricks {
  int rows;
  int cols;
  int width;
  int height;
  int color_num;
  int gap;
  Color color;
  Vector2 grid[LIST_ROW_LENGTH][LIST_COL_LENGTH];

} Bricks;

void initBricks(Bricks *bricks);
void genGrid(Bricks *bricks);
void updateBrickColor(Bricks *bricks);
void drawBricks(Bricks *bricks);
void bricksCollisionBall(Bricks *bricks, Ball *ball);
bool checkWinCondition(Bricks *bricks, bool game_won);

#endif // BRICKS_H
