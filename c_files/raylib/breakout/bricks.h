#ifndef BRICKS_H
#define BRICKS_H

#include "raylib.h"
#include "constants.h"

typedef struct
{
    Vector2 position;
    bool active;
    Color color;

}Brick;

typedef struct
{
    Brick list[ROWS][COLS];

}Bricks;

void initBricks(Bricks *bricks);
void genBricks(Bricks *bricks);
void drawBricks(Bricks *bricks);

#endif // BRICKS_H