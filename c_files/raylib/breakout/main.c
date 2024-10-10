#include "ball.h"
#include "bricks.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>
#include <string.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Breakout";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;
  const int LIVES_LENGTH = 6;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

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
    if (lives <= 0) {
      game_over = true;
    }

    if (!game_over) {
      // update lives and convert to string for display
      snprintf(lives_str, LIVES_LENGTH, "%d\n", lives);

      movePaddle(&paddle);
      lives = moveBall(&ball, lives);
      paddleCollisionBall(&paddle, &ball);
      bricksCollisionBall(&bricks, &ball);
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
      DrawText(lives_str, 10, GetScreenHeight() - 40, 30, GRAY);

      drawPaddle(&paddle);
      drawBall(&ball);
      drawBricks(&bricks);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText("Game Over", GetScreenWidth() / 2 - 85, GetScreenHeight() / 2 - 100,
               40, GRAY);
      DrawText("Press 'Enter' to restart", GetScreenWidth() / 2 - 160,
               GetScreenHeight() / 2, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
