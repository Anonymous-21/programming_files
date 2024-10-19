#include "ball.h"
#include "bricks.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

#define LIVES_MAX_LENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Breakout";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  int lives = 5;
  char lives_str[LIVES_MAX_LENGTH];

  Paddle paddle;
  Ball ball;
  Bricks bricks;

  initPaddle(&paddle);
  initBall(&ball);
  initBricks(&bricks);

  while (!WindowShouldClose()) {

    if (!game_over) {

      // game over condition
      if (lives <= 0) {
        game_over = true;
      }

      // convert lives to string
      snprintf(lives_str, LIVES_MAX_LENGTH, "Lives: %d\n", lives);

      movePaddle(&paddle);
      lives = moveBall(&ball, lives);

      // ball collision with paddle
      if (CheckCollisionCircleRec(
              (Vector2){ball.x, ball.y}, ball.radius,
              (Rectangle){paddle.x, paddle.y, paddle.width, paddle.height})) {
        ball.speed_y *= -1;
      }

      // ball collision with bricks
      for (int i = 0; i < bricks.size; i++) {
        if (CheckCollisionCircleRec((Vector2){ball.x, ball.y}, ball.radius,
                                    (Rectangle){bricks.grid[i].x,
                                                bricks.grid[i].y, bricks.width,
                                                bricks.height})) {
          ball.speed_y *= -1;
          bricks.grid[i] = (Vector2){-2, -2};
        }
      }

    } else if (game_over) {

      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        lives = 5;
        initPaddle(&paddle);
        initBall(&ball);
        initBricks(&bricks);
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    if (!game_over) {

      // draw lives
      DrawText(lives_str, 10, GetScreenHeight() - 50, 20, GRAY);

      drawPaddle(&paddle);
      DrawBall(&ball);
      drawBricks(&bricks);

    } else if (game_over) {

      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText("Game Over", GetScreenWidth() / 2 - 80,
               GetScreenHeight() / 2 - 30, 40, GRAY);
      DrawText("Press 'Enter' to restart!", GetScreenWidth() / 2 - 150,
               GetScreenHeight() / 2 + 20, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
