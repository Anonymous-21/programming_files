#include "ball.h"
#include "paddle.h"
#include "raylib.h"

#include <stdio.h>

#define SCOREMAXLENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Pong";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_paused = false;
  int left_score = 0;
  int right_score = 0;
  char left_score_str[SCOREMAXLENGTH];
  char right_score_str[SCOREMAXLENGTH];

  Paddle paddle_left;
  Paddle paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);
  initBall(&ball);

  while (!WindowShouldClose()) {

    // convert score to string
    snprintf(left_score_str, SCOREMAXLENGTH, "%d\n", left_score);
    snprintf(right_score_str, SCOREMAXLENGTH, "%d\n", right_score);

    // game pause/unpause with space key
    if (IsKeyPressed(KEY_SPACE) && game_paused) {
      game_paused = false;
    } else if (IsKeyPressed(KEY_SPACE) && !game_paused) {
      game_paused = true;
    }

    if (!game_paused) {
      movePaddle(&paddle_left, KEY_W, KEY_S);
      movePaddle(&paddle_right, KEY_UP, KEY_DOWN);
      moveBall(&ball);
      collisionPaddleBall(&paddle_left, &ball);
      collisionPaddleBall(&paddle_right, &ball);
      ballCollisionVerticalWalls(&ball);

      // ball collision with horizontal walls
      // update score and reset ball/paddle
      if (ball.x <= ball.radius) {
        right_score++;
        paddleReset(&paddle_left);
        paddleReset(&paddle_right);
        ballReset(&ball);
      } else if (ball.x >= GetScreenWidth() - ball.radius) {
        left_score++;
        paddleReset(&paddle_left);
        paddleReset(&paddle_right);
        ballReset(&ball);
      }
    } else if (game_paused) {
      DrawText("PAUSED", GetScreenWidth() - 150, 20, 30, GRAY);
    }

    BeginDrawing();

    ClearBackground(screenBackground);

    // draw score
    DrawText(left_score_str, GetScreenWidth() / 2 - 70, 10, 30, GRAY);
    DrawText(right_score_str, GetScreenWidth() / 2 + 50, 10, 30, GRAY);

    // draw screen divider
    DrawLineEx((Vector2){(float)GetScreenWidth() / 2, 0},
               (Vector2){(float)GetScreenWidth() / 2, GetScreenHeight()}, 5,
               GRAY);

    drawPaddle(&paddle_left);
    drawPaddle(&paddle_right);
    drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
