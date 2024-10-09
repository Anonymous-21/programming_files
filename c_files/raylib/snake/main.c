#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HIEGHT = 800;
  const char SCREEN_TITLE[] = "Snake";
  const Color SCREEN_BACKGROUND = RAYWHITE;
  const int GAME_FPS = 60;
  const int SCORE_LENGTH = 20;

  InitWindow(SCREEN_WIDTH, SCREEN_HIEGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  bool game_over = false;
  int score = 0;
  char temp_score_str[SCORE_LENGTH];
  char score_str[SCORE_LENGTH];

  Grid grid;
  Snake snake;
  Food food;

  initGrid(&grid);
  initSnake(&snake, &grid);
  initFood(&food, &grid, &snake);

  while (!WindowShouldClose()) {
    if (!game_over) {
      // update score and convert to string
      strncpy(score_str, "Score: ", SCORE_LENGTH);
      snprintf(temp_score_str, SCORE_LENGTH, "%d\n", score);
      strncat(score_str, temp_score_str, SCORE_LENGTH - strlen(score_str - 1));

      onKeyPress(&snake);
      score = updateSnake(&snake, &food, &grid, score);
      game_over = snakeCollisionWalls(&snake, &grid, game_over);
      game_over = snakeCollisionItself(&snake, game_over);
    } else if (game_over) {
      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        score = 0;
        initGrid(&grid);
        initSnake(&snake, &grid);
        initFood(&food, &grid, &snake);
      }
    }

    BeginDrawing();

    ClearBackground(SCREEN_BACKGROUND);

    if (!game_over) {
      // Draw score
      DrawText(score_str, GetScreenWidth() / 2 - 55, 30, 30, GRAY);

      drawGrid(&grid);
      drawSnake(&snake);
      drawFood(&food);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    SCREEN_BACKGROUND);
      DrawText(score_str, GetScreenWidth() / 2 - 70,
               GetScreenHeight() / 2 - 50, 30, GRAY);
      DrawText("Game Over", GetScreenWidth() / 2 - 70, GetScreenHeight() / 2,
               30, GRAY);
      DrawText("Press 'Enter' to continue", GetScreenWidth() / 2 - 160,
               GetScreenHeight() / 2 + 50, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
