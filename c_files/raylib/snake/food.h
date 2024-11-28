#ifndef FOOD_H
#define FOOD_H

#include "raylib.h"

typedef struct Snake Snake;

typedef struct Food {
  int x;
  int y;
  Color color;

} Food;

void initFood(Food *food, Snake *snake);
void genRandomFood(Food *food, Snake *snake);
void drawFood(Food *food);
void updateFood(Food *food);

#endif // FOOD_H
