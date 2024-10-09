#include "snake.h"
#include "food.h"
#include "grid.h"
#include "raylib.h"
#include <stdbool.h>
#include <string.h>

void initSnake(Snake *snake, Grid *grid) {
  snake->x = grid->margin;
  snake->y = grid->margin;
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->speed = grid->block_size;
  snake->head_color = BLUE;
  snake->tail_color = SKYBLUE;
  snake->size = 1;
  strncpy(snake->direction, "right", DIRECTION_LENGTH);
  snake->frames_counter = 0;
  snake->sentinal_value = (Vector2){-1, -1};

  for (int i = 0; i < LIST_LENGTH; i++) {
    snake->list[i] = snake->sentinal_value;
  }
  snake->list[0] = (Vector2){snake->x, snake->y};
}

void drawSnake(Snake *snake) {
  // draw head
  DrawRectangleRec((Rectangle){snake->list[0].x, snake->list[0].y, snake->width,
                               snake->height},
                   snake->head_color);
  // draw tail
  for (int i = 1; i < snake->size; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->tail_color);
  }
}

void onKeyPress(Snake *snake) {
  if (IsKeyPressed(KEY_RIGHT) &&
      strncmp(snake->direction, "left", DIRECTION_LENGTH) != 0) {
    strncpy(snake->direction, "right", DIRECTION_LENGTH);
  } else if (IsKeyPressed(KEY_LEFT) &&
             strncmp(snake->direction, "right", DIRECTION_LENGTH) != 0) {
    strncpy(snake->direction, "left", DIRECTION_LENGTH);
  } else if (IsKeyPressed(KEY_UP) &&
             strncmp(snake->direction, "down", DIRECTION_LENGTH) != 0) {
    strncpy(snake->direction, "up", DIRECTION_LENGTH);
  } else if (IsKeyPressed(KEY_DOWN) &&
             strncmp(snake->direction, "up", DIRECTION_LENGTH) != 0) {
    strncpy(snake->direction, "down", DIRECTION_LENGTH);
  }
}

int updateSnake(Snake *snake, Food *food, Grid *grid, int score) {
  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {

    // reset frames counter so that it does not overflow
    if (snake->frames_counter > 1000) {
      snake->frames_counter = 0;
    }

    // add speed to snake head according to user given direction
    if (strncmp(snake->direction, "right", DIRECTION_LENGTH) == 0) {
      snake->x += snake->speed;
    } else if (strncmp(snake->direction, "left", DIRECTION_LENGTH) == 0) {
      snake->x -= snake->speed;
    } else if (strncmp(snake->direction, "up", DIRECTION_LENGTH) == 0) {
      snake->y -= snake->speed;
    } else if (strncmp(snake->direction, "down", DIRECTION_LENGTH) == 0) {
      snake->y += snake->speed;
    }

    if (CheckCollisionRecs(
            (Rectangle){snake->list[0].x, snake->list[0].y, snake->width,
                        snake->height},
            (Rectangle){food->x, food->y, food->width, food->height})) {
      snake->list[snake->size] = snake->list[snake->size - 1];
      snake->size++;
      score++;
      Vector2 random_food = genRandomFood(grid, snake);
      food->x = random_food.x;
      food->y = random_food.y;
    }

    // update list values
    // shift values to the right 1 block
    // insert new value at list[0] and delete last list[size]
    for (int i = snake->size; i > 0; i--) {
      snake->list[i] = snake->list[i - 1];
    }
    snake->list[0] = (Vector2){snake->x, snake->y};
    snake->list[snake->size] = snake->sentinal_value;
  }

  return score;
}

bool snakeCollisionWalls(Snake *snake, Grid *grid, bool game_over) {
  if (snake->x < grid->margin ||
      snake->x > GetScreenWidth() - grid->margin - snake->width) {
    game_over = true;
  } else if (snake->y < grid->margin ||
             snake->y > GetScreenHeight() - grid->margin - snake->height) {
    game_over = true;
  }

  return game_over;
}

bool snakeCollisionItself(Snake *snake, bool game_over) {
  for (int i = 1; i < snake->size; i++) {
    if (CheckCollisionRecs((Rectangle){snake->list[0].x, snake->list[0].y,
                                       snake->width, snake->height},
                           (Rectangle){snake->list[i].x, snake->list[i].y,
                                       snake->width, snake->height})) {
      game_over = true;
    }
  }

  return game_over;
}
