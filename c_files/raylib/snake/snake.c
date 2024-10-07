#include "snake.h"
#include "grid.h"
#include "raylib.h"
#include <stdlib.h>
#include <string.h>

void initSnake(Grid *grid, Snake *snake) {
  snake->x = grid->margin_x;
  snake->y = grid->margin_y;
  snake->width = grid->block_size;
  snake->height = grid->block_size;
  snake->color = BLUE;
  snake->speed = grid->block_size;
  snake->frames_counter = 0;
  strcpy(snake->direction, "right");

  // fill list with sentinel value for counting purposes
  snake->sentinel_x = GetScreenWidth() * 10;
  snake->sentinel_y = GetScreenHeight() * 10;

  for (size_t i = 1; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    snake->list[i] = (Vector2){snake->sentinel_x, snake->sentinel_y};
  }

  // snake head
  snake->list[0] = (Vector2){snake->x, snake->y};
}

int arrayLength(Snake *snake) {
  int l = 0; // length of actually used list

  for (size_t i = 0; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    if (snake->list[i].x != snake->sentinel_x &&
        snake->list[i].y != snake->sentinel_y) {
      l++;
    }
  }

  return l;
}

void drawSnake(Snake *snake) {

  int l = arrayLength(snake);

  for (int i = 0; i < l; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->color);
  }
}

void updateSnake(Snake *snake) {
  // get direction from player key press
  if (IsKeyPressed(KEY_RIGHT) && strcmp(snake->direction, "left") != 0) {
    strcpy(snake->direction, "right");
  } else if (IsKeyPressed(KEY_LEFT) && strcmp(snake->direction, "right") != 0) {
    strcpy(snake->direction, "left");
  } else if (IsKeyPressed(KEY_UP) && strcmp(snake->direction, "down") != 0) {
    strcpy(snake->direction, "up");
  } else if (IsKeyPressed(KEY_DOWN) && strcmp(snake->direction, "up") != 0) {
    strcpy(snake->direction, "down");
  }

  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {
    // move snake according to direction
    if (strcmp(snake->direction, "right") == 0) {
      snake->x += snake->speed;
    } else if (strcmp(snake->direction, "left")) {
      snake->x -= snake->speed;
    } else if (strcmp(snake->direction, "up")) {
      snake->y -= snake->speed;
    } else if (strcmp(snake->direction, "down")) {
      snake->y += snake->speed;
    }

    // updaete snake list
    int l = arrayLength(snake);
    Vector2 new_list[400];

    snake->list[0] = (Vector2){snake->x, snake->y};
    for (int i = 0; i < l; i++) {
      new_list[i] = snake->list[i];
      snake->list[i + 1] = new_list[i];
      snake->list[l] = (Vector2){snake->sentinel_x, snake->sentinel_y};
    }
  }
}

// void freeArray(Snake *snake) { free(snake->list); }
