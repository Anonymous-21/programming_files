#include "constants.h"
#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include <stdbool.h>
#include <stdio.h>

#define STR_LENGTH 10

int main(void) {
  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  bool game_over = false;
  int score = 0;
  char score_str[STR_LENGTH];

  Snake snake;
  Food food;

  initSnake(&snake);
  initFood(&food, &snake);

  while (!WindowShouldClose()) {
    if (!game_over) {
      // convert score to string
      snprintf(score_str, STR_LENGTH, "Score: %d\n", score);

      updateSnake(&snake, &food, &game_over, &score);

      BeginDrawing();
      ClearBackground(SCREEN_BACKGROUND);

      // draw score
      DrawText(score_str, GetScreenWidth() / 2 - 70, 30, 30, GRAY);

      drawGrid();
      drawSnake(&snake);
      drawFood(&food);

      EndDrawing();
    } else {
      initSnake(&snake);
      initFood(&food, &snake);
      game_over = false;
      score = 0;
    }
  }

  CloseWindow();

  return 0;
}
