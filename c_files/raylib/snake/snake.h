#ifndef SNAKE_H
#define SNAKE_H

#include "constants.h"
#include "raylib.h"

#define SNAKE_LIST_LENGTH (ROWS * COLS)

typedef struct Food Food;

typedef enum Direction {
  RIGHT,
  LEFT,
  UP,
  DOWN

} Direction;

typedef struct Snake {
  int x;
  int y;
  Color color;
  Direction direction;
  int speed;
  int size;
  int frames_counter;
  Vector2 list[SNAKE_LIST_LENGTH];

} Snake;

void initSnake(Snake *snake);
void drawSnake(Snake *snake);
void updateSnake(Snake *snake, Food *food, bool *game_over, int *score);

#endif // SNAKE_H
