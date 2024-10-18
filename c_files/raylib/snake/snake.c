#include "snake.h"
#include "food.h"
#include "grid.h"
#include "raylib.h"
#include <stdbool.h>

void initSnake(Snake *snake, Grid *grid) {
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->x = grid->margin;
  snake->y = grid->margin;
  snake->color = BLUE;
  snake->speed = grid->block_size;
  snake->size = 1;
  snake->direction = RIGHT;
  snake->list[0] = (Vector2){snake->x, snake->y};
  snake->frames_counter = 0;
}

void drawSnake(Snake *snake) {
  for (int i = 0; i < snake->size; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->color);
  }
}

void getSnakeDirection(Snake *snake) {
  if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT) {
    snake->direction = RIGHT;
  } else if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT) {
    snake->direction = LEFT;
  } else if (IsKeyPressed(KEY_UP) && snake->direction != DOWN) {
    snake->direction = UP;
  } else if (IsKeyPressed(KEY_DOWN) && snake->direction != UP) {
    snake->direction = DOWN;
  }
}

void moveSnake(Snake *snake) {
  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {
    if (snake->frames_counter > 1000) {
      snake->frames_counter = 0;
    }

    switch (snake->direction) {
    case RIGHT:
      snake->x += snake->speed;
      break;
    case LEFT:
      snake->x -= snake->speed;
      break;
    case UP:
      snake->y -= snake->speed;
      break;
    case DOWN:
      snake->y += snake->speed;
      break;
    }

    for (int i = snake->size - 1; i > 0; i--) {
      snake->list[i] = snake->list[i - 1];
    }

    snake->list[0] = (Vector2){snake->x, snake->y};
  }
}

bool snakeCollisionItself(Snake *snake, bool game_over) {
  for (int i = 1; i < snake->size; i++) {
    if (CheckCollisionRecs((Rectangle){snake->list[0].x, snake->list[0].y,
                                       snake->width, snake->height},
                           (Rectangle){snake->list[i].x, snake->list[i].y,
                                       snake->width, snake->height})) {
      game_over = true;
      break;
    }
  }
  return game_over;
}

bool snakeCollisionWalls(Snake *snake, Grid *grid, bool game_over) {
  if (snake->x < grid->margin ||
      snake->x > GetScreenWidth() - grid->margin - snake->width) {
    game_over = true;
  } else if (snake->y < grid->margin ||
             snake->y > GetScreenHeight() - grid->margin - snake->width) {
    game_over = true;
  }

  return game_over;
}
