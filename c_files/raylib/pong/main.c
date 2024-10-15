#include "paddle.h"
#include "ball.h"
#include "raylib.h"


int main(void)
{
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Pong";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  Paddle paddle_left;
  Paddle paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);
  initBall(&ball);

  while (!WindowShouldClose())
  {
    BeginDrawing();

      ClearBackground(screenBackground);

      drawPaddle(&paddle_left);
      drawPaddle(&paddle_right);
      drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
