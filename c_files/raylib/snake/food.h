#ifndef FOOD_H
#define FOOD_H

#include "raylib.h"
#include "snake.h"

// typedef struct Snake snake;

typedef struct
{
    int x;
    int y;
    Color color;

} Food;

void initFood(Food *food, Snake *snake);
Vector2 genRandomFood(Snake *snake);
void drawFood(Food *food);

#endif // FOOD_H
