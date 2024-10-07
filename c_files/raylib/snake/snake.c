#include "snake.h"
#include "grid.h"
#include "raylib.h"
#include <string.h>

void initSnake(Snake *snake, Grid *grid) {
  snake->x = grid->margin_x;
  snake->y = grid->margin_y;
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->color = BLUE;
  snake->speed = grid->block_size;
  strncpy(snake->direction, "right", DIRECTION_LENGTH);
  snake->sentinal_x = GetScreenWidth() * 10;
  snake->sentinal_y = GetScreenHeight() * 10;
  snake->frames_counter = 0;

  // initialize every value in list with sentinal values for calculating actual
  // length of array
  for (size_t i = 0; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    snake->list[i] = (Vector2){snake->sentinal_x, snake->sentinal_y};
  }

  snake->list[0] = (Vector2){snake->x, snake->sentinal_y};
}

int arrayLength(Snake *snake) {
  int length = 0;
  for (size_t i = 0; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    if (snake->list[i].x != snake->sentinal_x &&
        snake->list[i].y != snake->sentinal_y) {
      length++;
    }
  }
  return length;
}

void drawSnake(Snake *snake) {
  int length = arrayLength(snake);
  for (int i = 0; i < length; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->color);
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

void updateSnake(Snake *snake) {
  // move snake based on given direction
  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {
    if (strncmp(snake->direction, "right", DIRECTION_LENGTH) == 0) {
      snake->x += snake->speed;
    } else if (strncmp(snake->direction, "left", DIRECTION_LENGTH) == 0) {
      snake->x -= snake->speed;
    } else if (strncmp(snake->direction, "up", DIRECTION_LENGTH) == 0) {
      snake->y -= snake->speed;
    } else if (strncmp(snake->direction, "down", DIRECTION_LENGTH) == 0) {
      snake->y += snake->speed;
    }

    // update snake head
    snake->list[0] = (Vector2){snake->x, snake->y};

    // update rest of the list
    int array_length = arrayLength(snake);
    Vector2 new_list[LIST_LENGTH];

    for (int i = 0; i < array_length; i++) {
      new_list[i] = snake->list[i];
      snake->list[i + 1] = new_list[i];
      snake->list[array_length] =
          (Vector2){snake->sentinal_x, snake->sentinal_y};
    }
  }
}

int collisionWalls(Snake *snake, Grid *grid, bool game_over) {
  if (snake->x < grid->margin_x ||
      snake->x > GetScreenWidth() - snake->width - grid->margin_x) {
    game_over = true;
  } else if (snake->y < grid->margin_y ||
             snake->y > GetScreenHeight() - snake->height - grid->margin_y) {
    game_over = true;
  }

  return game_over;
}
