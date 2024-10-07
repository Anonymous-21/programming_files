#ifndef FOOD_H
#define FOOD_H

#include "raylib.h"

typedef struct Grid Grid;
typedef struct Snake Snake;

typedef struct Food {
  int x;
  int y;
  int width;
  int height;
  Color color;

} Food;

void initFood(Food *food, Grid *grid, Snake *snake);
Vector2 genRandomFood(Grid *grid, Snake *snake);
void drawFood(Food *food);

#endif // FOOD_H
