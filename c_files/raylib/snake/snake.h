#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

#define LIST_LENGTH 300

typedef struct Grid Grid;
typedef struct Food Food;

typedef enum {
  RIGHT,
  LEFT,
  UP,
  DOWN

} Direction;

typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;
  int size;
  Direction direction;
  Vector2 list[LIST_LENGTH];
  int frames_counter;

} Snake;

void initSnake(Snake *snake, Grid *grid);
void drawSnake(Snake *snake);
void getSnakeDirection(Snake *snake);
void moveSnake(Snake *snake);
bool snakeCollisionItself(Snake *snake, bool game_over);
bool snakeCollisionWalls(Snake *snake, Grid *grid, bool game_over);

#endif // SNAKE_H
