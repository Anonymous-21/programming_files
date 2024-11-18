#ifndef COLLISION_HANDLER_H
#define COLLISION_HANDLER_H

#include "snake.h"
#include "food.h"

void snakeCollisionWalls(Snake *snake, bool *game_over);
void snakeCollisionFood(Snake *snake, Food *food);
void snakeCollisionItself(Snake *snake, bool *game_over);

#endif // COLLISION_HANDLER_H
