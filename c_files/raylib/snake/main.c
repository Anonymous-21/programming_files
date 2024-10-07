#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define SCORE_LENGTH 20
#define SCORE_LENGTH_CONCATENATED 40

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
  char score_str[SCORE_LENGTH];
  char score_str_concatenated[SCORE_LENGTH_CONCATENATED];

  Grid grid;
  Snake snake;
  Food food;

  initGrid(&grid);
  initSnake(&snake, &grid);
  initFood(&food, &grid, &snake);

  while (!WindowShouldClose()) {

    if (!game_over) {
      // update score and convert to string for display
      snprintf(score_str, SCORE_LENGTH, "%d\n", score);
      strncpy(score_str_concatenated, "Score: ", SCORE_LENGTH_CONCATENATED);
      strncat(score_str_concatenated, score_str,
              SCORE_LENGTH_CONCATENATED - (strlen(score_str_concatenated) - 1));

      onKeyPress(&snake);
      updateSnake(&snake);
      game_over = collisionWalls(&snake, &grid, game_over);
    } else {
      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        score = 0;
        snake.frames_counter = 0;
        initGrid(&grid);
        initSnake(&snake, &grid);
        initFood(&food, &grid, &snake);
      }
    }

    BeginDrawing();

    ClearBackground(screenBackground);

    if (!game_over) {
      // draw score
      DrawText(score_str_concatenated, GetScreenWidth() / 2 - 70, 30, 40, GRAY);

      drawGrid(&grid);
      drawSnake(&snake);
      drawFood(&food);
    } else {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText(score_str_concatenated, GetScreenWidth() / 2 - 80,
               GetScreenHeight() / 2 - 100, 40, GRAY);
      DrawText("Game Over", GetScreenWidth() / 2 - 90, GetScreenHeight() / 2,
               40, GRAY);
      DrawText("Press 'Enter' to continue!", GetScreenWidth() / 2 - 170,
               GetScreenHeight() / 2 + 100, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
