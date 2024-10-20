#include "ball.h"
#include "bricks.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

#define LIVES_LENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Breakout";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_won = false;
  bool game_over = false;
  int lives = 5;
  char lives_str[LIVES_LENGTH];

  Paddle paddle;
  Ball ball;
  Bricks bricks;

  initPaddle(&paddle);
  initBall(&ball);
  initBricks(&bricks);

  while (!WindowShouldClose()) {

    if (!game_over && !game_won) {
      // convert lives to string
      snprintf(lives_str, LIVES_LENGTH, "Lives: %d\n", lives);

      updatePaddle(&paddle);
      updateBall(&ball);

      // game win condition
      bool remaining = false;
      for (int i = 0; i < bricks.rows; i++) {
        for (int j = 0; j < bricks.cols; j++) {
          if (bricks.grid[i][j].x != -2 || bricks.grid[i][j].y != -2) {
            remaining = true;
          }
        }
      }

      if (!remaining) {
        game_won = true;
      }

      // game over condition
      if (lives <= 0) {
        game_over = true;
      }

      // ball collision paddle
      if (CheckCollisionCircleRec(
              (Vector2){ball.x, ball.y}, ball.radius,
              (Rectangle){paddle.x, paddle.y, paddle.width, paddle.height})) {

        ball.speed_y *= -1;
      }

      // ball collision bricks
      for (int i = 0; i < bricks.rows; i++) {
        for (int j = 0; j < bricks.cols; j++) {
          if (CheckCollisionCircleRec(
                  (Vector2){ball.x, ball.y}, ball.radius,
                  (Rectangle){bricks.grid[i][j].x, bricks.grid[i][j].y,
                              bricks.width, bricks.height})) {

            ball.speed_y *= -1;
            bricks.grid[i][j] = (Vector2){-2, -2};
          }
        }
      }

      // ball collision floor and update lives
      if (ball.y >= GetScreenHeight() - ball.radius) {
        lives--;
        ball.active = false;
        resetBall(&ball);
        resetPaddle(&paddle);
      }
    } else if (game_won || game_over) {
      if (IsKeyPressed(KEY_ENTER)) {
        lives = 5;
        game_won = false;
        game_over = false;
        initBricks(&bricks);
        initPaddle(&paddle);
        initBall(&ball);
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    if (!game_over && !game_won) {
      // draw lives
      DrawText(lives_str, 10, GetScreenHeight() - 50, 30, GRAY);

      drawPaddle(&paddle);
      drawBall(&ball);
      drawBricks(&bricks);
    } else if (game_won) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText("You win!", GetScreenWidth() / 2 - 80,
               GetScreenHeight() / 2 - 50, 40, GRAY);
      DrawText("Press 'Enter' to restart!", GetScreenWidth() / 2 - 150,
               GetScreenHeight() / 2 + 20, 30, GRAY);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText("Game Over", GetScreenWidth() / 2 - 80,
               GetScreenHeight() / 2 - 50, 40, GRAY);
      DrawText("Press 'Enter' to restart!", GetScreenWidth() / 2 - 150,
               GetScreenHeight() / 2 + 20, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
