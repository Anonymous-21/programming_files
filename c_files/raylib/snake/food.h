#ifndef FOOD_H
#define FOOD_H

#include "raylib.h"

typedef struct Food
{
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
}Food;

void initFood(Food *food, int rows, int cols, int block_size, int margin_x, int margin_y, Vector2 snake_list[]);
Vector2 genRandomFood(Food *food, Vector2 snake_list[]);
#endif // FOOD_H
