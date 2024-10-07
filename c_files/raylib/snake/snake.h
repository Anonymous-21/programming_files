#ifndef SNAKE_H
#define SNAKE_H

#include "grid.h"
#include "raylib.h"

#define DIRECTION_MAX 6
#define SNAKE_LIST_MAX 400

typedef struct Snake {
  int block_size;
  int margin_x;
  int margin_y;
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;
  char direction[DIRECTION_MAX];
  int sentinal_x;
  int sentinal_y;
  int frames_counter;
  Vector2 list[SNAKE_LIST_MAX];
} Snake;

void initSnake(Snake *snake, int block_size, int margin_x, int margin_y);
int arrayLength(Snake *snake);
void drawSnake(Snake *snake);
void on_key_press(Snake *snake);
void updateSnake(Snake *snake);
bool collisionWalls(Snake *snake, bool game_over);

#endif // SNAKE_H
