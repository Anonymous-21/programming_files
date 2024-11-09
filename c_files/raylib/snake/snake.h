#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

#define LIST_LENGTH 400

typedef enum Direction { RIGHT, LEFT, UP, DOWN } Direction;

typedef struct Grid Grid;
typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  Color color;
  Vector2 list[LIST_LENGTH];
  int size;
  int speed;
  int frames_counter;
  Direction direction;

} Snake;

void initSnake(Snake *snake, Grid *grid);
void drawSnake(Snake *snake);
void moveSnake(Snake *snake);
void snakeCollisionWalls(Snake *snake, Grid *grid, bool *game_over);
void snakeCollisionItself(Snake *snake, bool *game_over);

#endif // SNAKE_H
