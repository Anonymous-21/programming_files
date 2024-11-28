#include "food.h"
#include "constants.h"
#include "raylib.h"
#include "snake.h"

void initFood(Food *food, Snake *snake) {
  food->color = RED;
  genRandomFood(food, snake);
}

void genRandomFood(Food *food, Snake *snake) {
  while (1) {
    int x = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;
    int y = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;

    for (int i = 0; i < snake->size; i++) {
      if (x != snake->list[i].x && y != snake->list[i].y) {
        food->x = x;
        food->y = y;
        return;
      }
    }
  }
}

void drawFood(Food *food) {
  DrawRectangleRec((Rectangle){food->x, food->y, BLOCK_SIZE, BLOCK_SIZE},
                   food->color);
}
