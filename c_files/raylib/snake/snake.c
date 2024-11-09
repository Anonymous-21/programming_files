#include "snake.h"
#include "grid.h"
#include "raylib.h"

void initSnake(Snake *snake, Grid *grid) {
  snake->x = grid->margin;
  snake->y = grid->margin;
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->color = BLUE;
  snake->size = 1;
  snake->direction = RIGHT;
  snake->speed = grid->block_size;
  snake->frames_counter = 0;
  snake->list[0].x = snake->x;
  snake->list[0].y = snake->y;
}

void drawSnake(Snake *snake) {
  for (int i = 0; i < snake->size; i++) {
    DrawRectangle(snake->list[i].x, snake->list[i].y, snake->width,
                  snake->height, snake->color);
  }
}

void moveSnake(Snake *snake) {
  // get direction from player
  if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT) {
    snake->direction = RIGHT;
  } else if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT) {
    snake->direction = LEFT;
  } else if (IsKeyPressed(KEY_UP) && snake->direction != DOWN) {
    snake->direction = UP;
  } else if (IsKeyPressed(KEY_DOWN) && snake->direction != UP) {
    snake->direction = DOWN;
  }

  // move snake
  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {
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
    }

    for (int i = snake->size; i > 0; i--) {
      snake->list[i] = snake->list[i - 1];
    }

    snake->list[0] = (Vector2){snake->x, snake->y};
  }
}

void snakeCollisionWalls(Snake *snake, Grid *grid, bool *game_over) {
  if (snake->list[0].x < grid->margin ||
      snake->list[0].x > GetScreenWidth() - grid->margin - snake->width) {
    *game_over = true;
  } else if (snake->list[0].y < grid->margin ||
             snake->list[0].y >
                 GetScreenHeight() - grid->margin - snake->height) {
    *game_over = true;
  }
}

void snakeCollisionItself(Snake *snake, bool *game_over) {
  for (int i = 1; i < snake->size; i++) {
    if (CheckCollisionRecs((Rectangle){snake->list[0].x, snake->list[0].y,
                                       snake->width, snake->height},
                           (Rectangle){snake->list[i].x, snake->list[i].y,
                                       snake->width, snake->height})) {
      *game_over = true;
    }
  }
}
