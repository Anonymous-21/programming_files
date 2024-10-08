#ifndef SNAKE_H
#define SNAKE_H

#include "raylib.h"

#define DIRECTION_LENGTH 7
#define LIST_LENGTH 400

typedef struct Grid Grid;
typedef struct Food Food;

typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;
  char direction[DIRECTION_LENGTH];
  int sentinal_x;
  int sentinal_y;
  int frames_counter;
  int size;
  Vector2 list[LIST_LENGTH];

} Snake;

void initSnake(Snake *snake, Grid *grid);
int arrayLength(Snake *snake);
void drawSnake(Snake *snake);
void onKeyPress(Snake *snake);
int updateSnake(Snake *snake, Food *food, Grid *grid, int score);
int collisionWalls(Snake *snake, Grid *grid, bool game_over);

#endif // SNAKE_H
