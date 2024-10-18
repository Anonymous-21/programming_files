#include "food.h"
#include "grid.h"
#include "raylib.h"
#include "snake.h"
#include <stdio.h>

#define STR_LENGTH 20

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
  char score_str[STR_LENGTH];

  Grid grid;
  Snake snake;
  Food food;

  initGrid(&grid);
  initSnake(&snake, &grid);
  initFood(&food, &grid, &snake);

  while (!WindowShouldClose()) {

    if (!game_over) {
      // convert score to string
      snprintf(score_str, STR_LENGTH, "Score: %d\n", score);

      getSnakeDirection(&snake);
      moveSnake(&snake);

      // snake collision food
      if (CheckCollisionRecs(
              (Rectangle){snake.list[0].x, snake.list[0].y, snake.width,
                          snake.height},
              (Rectangle){food.x, food.y, food.width, food.height})) {

        score++;
        snake.size++;
        Vector2 random_food = genRandomFood(&grid, &snake);
        food.x = random_food.x;
        food.y = random_food.y;
      }
    } else if (game_over) {
      if (IsKeyPressed(KEY_ENTER)) {
        score = 0;
        initGrid(&grid);
        initSnake(&snake, &grid);
        initFood(&food, &grid, &snake);
        game_over = false;
      }
    }

    game_over = snakeCollisionItself(&snake, game_over);
    game_over = snakeCollisionWalls(&snake, &grid,game_over);

    BeginDrawing();

    ClearBackground(screenBackground);

    if (!game_over) {
      // draw score
      DrawText(score_str, GetScreenWidth() / 2 - 100, 30, 40, GRAY);

      drawGrid(&grid);
      drawSnake(&snake);
      drawFood(&food);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText(score_str, GetScreenWidth() / 2 - 70,
               GetScreenHeight() / 2 - 70, 40, GRAY);
      DrawText("Game Over", GetScreenWidth() / 2 - 70, GetScreenHeight() / 2,
               40, GRAY);
      DrawText("Press 'Enter' to continue!", GetScreenWidth() / 2 - 150,
               GetScreenHeight() / 2 + 70, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
