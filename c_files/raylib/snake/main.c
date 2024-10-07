#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include "food.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define SCORE_MAX 20
#define SCORE_MAX_CONCATENATED 40

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 800;
  const char screenTitle[] = "Snake";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  int score = 0;
  char score_str[SCORE_MAX];
  char score_str_concatenated[SCORE_MAX_CONCATENATED];

  int rows = 20;
  int cols = 20;
  int block_size = 30;
  int margin_x = 100;
  int margin_y = 100;

  Grid grid;
  Snake snake;
  Food food;

  initGrid(&grid, rows, cols, block_size, margin_x, margin_y);
  initSnake(&snake, block_size, margin_x, margin_y);
  initFood(&food, &snake, rows, cols, block_size, margin_x, margin_y);

  while (!WindowShouldClose()) {

    if (!game_over) {
      // update score and convert to string for display
      snprintf(score_str, SCORE_MAX, "%d\n", score);
      strncpy(score_str_concatenated, "Score: ", SCORE_MAX_CONCATENATED);
      strncat(score_str_concatenated, score_str,
              SCORE_MAX_CONCATENATED - strlen(score_str_concatenated) - 1);

      // get input from player and move snake
      on_key_press(&snake);
      updateSnake(&snake);
      game_over = collisionWalls(&snake, game_over);
    } else {
      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        score = 0;
        snake.frames_counter = 0;
        initGrid(&grid, rows, cols, block_size, margin_x, margin_y);
        initSnake(&snake, block_size, margin_x, margin_y);
        initFood(&food, &snake, rows, cols, block_size, margin_x, margin_y);
      }
    }
    BeginDrawing();

    ClearBackground(screenBackground);

    if (!game_over) {
      DrawText(score_str_concatenated, GetScreenWidth() / 2 - 70, 35, 30, GRAY);
      drawGrid(&grid);
      drawSnake(&snake);
      drawFood(&food);
    } else {
      DrawRectangleRec((Rectangle){0, 0, GetScreenWidth(), GetScreenHeight()},
                       screenBackground);
      DrawText(score_str_concatenated, GetScreenWidth() / 2 - 70,
               GetScreenHeight() / 2 - 150, 40, GRAY);
      DrawText("Game Over", GetScreenWidth() / 2 - 110, GetScreenHeight() / 2,
               50, GRAY);
      DrawText("Press 'Enter' to continue", GetScreenWidth() / 2 - 165,
               GetScreenHeight() / 2 + 80, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
