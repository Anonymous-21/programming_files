#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

#define DIRECTION_LENGTH 6
#define LIST_LENGTH 300

typedef struct Grid Grid;
typedef struct Food Food;

typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  int speed;
  Color head_color;
  Color tail_color;
  int size;
  char direction[DIRECTION_LENGTH];
  Vector2 list[LIST_LENGTH];
  int frames_counter;
  Vector2 sentinal_value;
} Snake;

void initSnake(Snake *snake, Grid *grid);
void drawSnake(Snake *snake);
void onKeyPress(Snake *snake);
int updateSnake(Snake *snake, Food *food, Grid *grid, int score);
bool snakeCollisionWalls(Snake *snake, Grid *grid, bool game_over);
bool snakeCollisionItself(Snake *snake, bool game_over);

#endif // SNAKE_H
