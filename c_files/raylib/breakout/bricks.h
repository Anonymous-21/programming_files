#ifndef BRICKS_H
#define BRICKS_H

#include "raylib.h"

#define ROWS 5
#define COLS 10

typedef struct Brick
{
    Vector2 position;
    bool is_active;

} Brick;

typedef struct Bricks
{
    Brick list[ROWS * COLS];
    int size;

} Bricks;

void bricks_initialize(Bricks *bricks);
void bricks_draw(Bricks *bricks);

#endif