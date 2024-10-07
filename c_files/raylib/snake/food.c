#include "food.h"
#include "raylib.h"

void initFood(Food *food, int rows, int cols, int block_size, int margin_x,
              int margin_y, Vector2 snake_list[]) {
  food->rows = rows;
  food->cols = cols;
  food->block_size = block_size;
  food->margin_x = margin_x;
  food->margin_y = margin_y;
  Vector2 random_food = genRandomFood(food, snake_list);
  food->x = random_food.x;
  food->y = random_food.y;
  food->width = food->block_size;
  food->height = food->block_size;
  food->color = RED;
}

Vector2 genRandomFood(Food *food, Vector2 snake_list[]) {
  while (1) {
    int x = (GetRandomValue(0, food->cols - 1) * food->block_size) + food->margin_x;
    int y = (GetRandomValue(0, food->rows - 1) * food->block_size) + food->margin_y;
    for (int i = 0; i < list_length; i++)
    {
      if (x != snake_list[i].x && y != snake_list[i].y) {
        return (Vector2){x, y};
      }
    }
  }
}
