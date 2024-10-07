#ifndef FOOD_H
#define FOOD_H

#include "raylib.h"
#include "snake.h"

typedef struct Food {
  int rows;
  int cols;
  int block_size;
  int margin_x;
  int margin_y;
  int x;
  int y;
  int width;
  int height;
  Color color;
} Food;

void initFood(Food *food, Snake *snake, int rows, int cols, int block_size, int margin_x,
              int margin_y);
Vector2 genRandomFood(Food *food, Snake *snake);
void drawFood(Food *food);

#endif // FOOD_H
