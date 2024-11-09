#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include <stdio.h>

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 800;
  const char SCREEN_TITLE[] = "Snake";
  const Color SCREEN_BACKGROUND = RAYWHITE;
  const int GAME_FPS = 60;

  const int SCORE_LENGTH = 10;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  bool game_win = false;
  bool game_over = false;
  int score = 0;
  char score_str[SCORE_LENGTH];

  Grid grid;
  Snake snake;
  Food food;

  initGrid(&grid);
  initSnake(&snake, &grid);
  initFood(&food, &grid, &snake);

  while (!WindowShouldClose()) {
    // convert score to string
    snprintf(score_str, SCORE_LENGTH, "Score: %d\n", score);

    // game win condition
    if (snake.size >= grid.rows * grid.cols) {
      game_win = true;
    }

    if (!game_over && !game_win) {
      moveSnake(&snake);

      // snake collision food
      if (CheckCollisionRecs(
              (Rectangle){snake.list[0].x, snake.list[0].y, snake.width,
                          snake.height},
              (Rectangle){food.x, food.y, food.width, food.height})) {
        score++;
        snake.size++;
        initFood(&food, &grid, &snake);
      }

      snakeCollisionWalls(&snake, &grid, &game_over);
      snakeCollisionItself(&snake, &game_over);

    } else if (game_win || game_over) {
      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        game_win = false;
        score = 0;
        initGrid(&grid);
        initSnake(&snake, &grid);
        initFood(&food, &grid, &snake);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    if (!game_over && !game_win) {
      // draw score
      DrawText(score_str, GetScreenWidth() / 2 - 60, 35, 30, GRAY);

      drawGrid(&grid);
      drawSnake(&snake);
      drawFood(&food);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), RAYWHITE);
      DrawText(score_str, GetScreenWidth() / 2 - 60,
               GetScreenHeight() / 2 - 100, 30, GRAY);
      DrawText("You lose", GetScreenWidth() / 2 - 60, GetScreenHeight() / 2, 30,
               GRAY);
      DrawText("Press 'enter' to restart!", GetScreenWidth() / 2 - 120,
               GetScreenHeight() / 2 + 50, 20, GRAY);
    } else if (game_win) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), RAYWHITE);
      DrawText(score_str, GetScreenWidth() / 2 - 60,
               GetScreenHeight() / 2 - 100, 30, GRAY);
      DrawText("You win", GetScreenWidth() / 2 - 60, GetScreenHeight() / 2, 30,
               GRAY);
      DrawText("Press 'enter' to restart!", GetScreenWidth() / 2 - 120,
               GetScreenHeight() / 2 + 50, 20, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
