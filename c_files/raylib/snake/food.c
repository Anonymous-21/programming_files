#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"

void initFood(Food *food, Grid *grid, Snake *snake) {
  Vector2 random_food = genRandomFood(grid, snake);
  food->x = random_food.x;
  food->y = random_food.y;
  food->width = grid->block_size;
  food->height = grid->block_size;
  food->color = RED;
}

Vector2 genRandomFood(Grid *grid, Snake *snake) {
  while (1) {
    int x = GetRandomValue(0, grid->rows - 1) * grid->block_size + grid->margin;
    int y = GetRandomValue(0, grid->cols - 1) * grid->block_size + grid->margin;

    for (int i = 0; i < snake->size; i++) {
      if (x != snake->list[0].x && y != snake->list[0].y) {
        return (Vector2){x, y};
      }
    }
  }
}

void drawFood(Food *food) {
  DrawRectangle(food->x, food->y, food->width, food->height, food->color);
}
