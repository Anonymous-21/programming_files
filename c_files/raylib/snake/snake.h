#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

typedef enum
{
    RIGHT,
    LEFT,
    UP,
    DOWN

} Direction;

typedef struct
{
    Vector2 *list;
    int size;
    int capacity;

} SnakeArray;

typedef struct
{
    int x;
    int y;
    Color color;
    int frames_counter;
    Direction direction;
    SnakeArray snake_array;

} Snake;

void initSnake(Snake *snake);
void drawSnake(Snake *snake);
void updateSnakeList(Snake *snake);
void getDirection(Snake *snake);
void moveSnake(Snake *snake);
void freeSnakeList(Snake *snake);

#endif // SNAKE_H