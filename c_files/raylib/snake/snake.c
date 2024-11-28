#include "snake.h"
#include "constants.h"
#include "food.h"
#include "raylib.h"
#include <stdbool.h>

void initSnake(Snake *snake) {
  snake->x = MARGIN;
  snake->y = MARGIN;
  snake->speed = BLOCK_SIZE;
  snake->direction = RIGHT;
  snake->color = BLUE;
  snake->size = 1;
  snake->list[0] = (Vector2){snake->x, snake->y};
  snake->frames_counter = 0;
}

void drawSnake(Snake *snake) {
  for (int i = 0; i < snake->size; i++) {
    DrawRectangleRec(
        (Rectangle){snake->list[i].x, snake->list[i].y, BLOCK_SIZE, BLOCK_SIZE},
        snake->color);
  }
}

void updateSnake(Snake *snake, Food *food, bool *game_over, int *score) {

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

  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {

    if (snake->frames_counter > 1000) {
      snake->frames_counter = 0;
    }

    for (int i = snake->size; i > 0; i--) {
      snake->list[i] = snake->list[i - 1];
    }

    // update snake based on direction
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

    // snake collision walls
    if (snake->x < MARGIN) {
      snake->x = GetScreenWidth() - MARGIN - BLOCK_SIZE;
    } else if (snake->x > GetScreenWidth() - MARGIN - BLOCK_SIZE) {
      snake->x = MARGIN;
    } else if (snake->y < MARGIN) {
      snake->y = GetRenderHeight() - MARGIN - BLOCK_SIZE;
    } else if (snake->y > GetScreenHeight() - MARGIN - BLOCK_SIZE) {
      snake->y = MARGIN;
    }

    snake->list[0] = (Vector2){snake->x, snake->y};
  }

  // snake collision itself
  for (int i = 1; i < snake->size; i++) {
    if (CheckCollisionRecs((Rectangle){snake->list[0].x, snake->list[0].y,
                                       BLOCK_SIZE, BLOCK_SIZE},
                           (Rectangle){snake->list[i].x, snake->list[i].y,
                                       BLOCK_SIZE, BLOCK_SIZE})) {
      *game_over = true;
    }
  }

  // snake collision food
  if (CheckCollisionRecs((Rectangle){food->x, food->y, BLOCK_SIZE, BLOCK_SIZE},
                         (Rectangle){snake->list[0].x, snake->list[0].y,
                                     BLOCK_SIZE, BLOCK_SIZE})) {
    snake->size++;
    *score += 1;
    genRandomFood(food, snake);
  }
}
