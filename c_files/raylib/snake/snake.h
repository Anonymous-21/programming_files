#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"
#include "grid.h"

#define MAX 6
#define LMAX 400

typedef struct Snake {

  int x;
  int y;
  int width;
  int height;
  Color color;
  char direction[MAX];
  int speed;
  int frames_counter;
  float sentinel_x;
  float sentinel_y;
  Vector2 list[LMAX];

} Snake;

void initSnake(Grid *grid, Snake *snake);
int arrayLength(Snake *snake);
void drawSnake(Snake *snake);
void updateSnake(Snake *snake);
// void freeArray(Snake *snake);

#endif // SNAKE_H
