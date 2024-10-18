#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

#define LIST_LENGTH 300

typedef struct Grid Grid;

typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;
  int size;
  Vector2 list[LIST_LENGTH];

} Snake;

void initSnake(Snake *snake, Grid *grid);
void drawSnake(Snake *snake);

#endif // SNAKE_H
