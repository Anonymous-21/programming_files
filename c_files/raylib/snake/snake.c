#include "snake.h"
#include "grid.h"
#include "raylib.h"

void initSnake(Snake *snake, Grid *grid) {
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->x = grid->margin;
  snake->y = grid->margin;
  snake->color = BLUE;
  snake->speed = grid->block_size;
  snake->size = 1;
  snake->list[0] = (Vector2){snake->x, snake->y};
}

void drawSnake(Snake *snake) {
  for (int i = 0; i < snake->size; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->color);
  }
}
