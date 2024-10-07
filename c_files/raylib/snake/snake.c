#include "snake.h"
#include "raylib.h"
#include <string.h>

void initSnake(Snake *snake, int block_size, int margin_x, int margin_y) {
  snake->block_size = block_size;
  snake->margin_x = margin_x;
  snake->margin_y = margin_y;
  snake->x = snake->margin_x;
  snake->y = snake->margin_y;
  snake->width = snake->block_size;
  snake->height = snake->block_size;
  snake->color = BLUE;
  snake->speed = snake->block_size;
  strncpy(snake->direction, "right", 6);
  snake->sentinal_x = GetScreenWidth() * 10;
  snake->sentinal_y = GetScreenHeight() * 10;
  snake->frames_counter = 0;

  for (size_t i = 0; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    snake->list[i].x = snake->sentinal_x;
    snake->list[i].y = snake->sentinal_y;
  }

  snake->list[0] = (Vector2){snake->x, snake->y};
}

int arrayLength(Snake *snake) {
  int n = 0;
  for (size_t i = 0; i < sizeof(snake->list) / sizeof(snake->list[0]); i++) {
    if (snake->list[i].x != snake->sentinal_x &&
        snake->list[i].y != snake->sentinal_y) {
      n++;
    }
  }
  return n;
}

void drawSnake(Snake *snake) {
  int list_length = arrayLength(snake);

  for (int i = 0; i < list_length; i++) {
    DrawRectangleRec((Rectangle){snake->list[i].x, snake->list[i].y,
                                 snake->width, snake->height},
                     snake->color);
  }
}

void on_key_press(Snake *snake) {
  if (IsKeyPressed(KEY_RIGHT) && strcmp(snake->direction, "left") != 0) {
    strncpy(snake->direction, "right", 6);
  } else if (IsKeyPressed(KEY_LEFT) && strcmp(snake->direction, "right") != 0) {
    strncpy(snake->direction, "left", 5);
  } else if (IsKeyPressed(KEY_UP) && strcmp(snake->direction, "down") != 0) {
    strncpy(snake->direction, "up", 3);
  } else if (IsKeyPressed(KEY_DOWN) && strcmp(snake->direction, "up") != 0) {
    strncpy(snake->direction, "down", 5);
  }
}

void updateSnake(Snake *snake) {
  // move snake
  snake->frames_counter++;
  if (snake->frames_counter % 5 == 0) {
    if (strncmp(snake->direction, "right", 5) == 0) {
      snake->x += snake->speed;
    } else if (strncmp(snake->direction, "left", 4) == 0) {
      snake->x -= snake->speed;
    } else if (strncmp(snake->direction, "up", 2) == 0) {
      snake->y -= snake->speed;
    } else if (strncmp(snake->direction, "down", 4) == 0) {
      snake->y += snake->speed;
    }

    // update
    //  snake head
    snake->list[0] = (Vector2){snake->x, snake->y};
    // rest of snake list
    int list_length = arrayLength(snake);
    Vector2 new_list[SNAKE_LIST_MAX];
    for (int i = 0; i < list_length; i++) {
      new_list[i] = snake->list[i];
      snake->list[i + 1] = new_list[i];
      snake->list[list_length] =
          (Vector2){snake->sentinal_x, snake->sentinal_y};
    }
  }
}

bool collisionWalls(Snake *snake, bool game_over) {
  if (snake->x < snake->margin_x ||
      snake->x > GetScreenWidth() - snake->margin_x - snake->width) {
    game_over = true;
  } else if (snake->y < snake->margin_y ||
             snake->y > GetScreenHeight() - snake->margin_y - snake->height) {
    game_over = true;
  }

  return game_over;
}
