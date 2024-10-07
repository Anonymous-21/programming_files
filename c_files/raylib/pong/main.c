#include "ball.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

int main() {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Pong";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  int left_score = 0;
  int right_score = 0;
  char left_score_str[MAX];
  char right_score_str[MAX];

  Paddle paddle_left, paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);

  initBall(&ball);

  while (!WindowShouldClose()) {

    // update score and convert to string
    snprintf(left_score_str, MAX, "%d\n", left_score);
    snprintf(right_score_str, MAX, "%d\n", right_score);

    movePaddle(&paddle_left, KEY_W, KEY_S);
    movePaddle(&paddle_right, KEY_UP, KEY_DOWN);

    moveBall(&ball);

    collisionPaddleBall(&paddle_left, &ball);
    collisionPaddleBall(&paddle_right, &ball);

    // add scores and reset ball and paddles
    if (ball.x <= ball.radius) {
      right_score++;
      resetBall(&ball);
      resetPaddle(&paddle_left);
      resetPaddle(&paddle_right);
      ball.frames_counter = 0;
      ball.change_x *= -1;
    } else if (ball.x >= GetScreenWidth() - ball.radius) {
      left_score++;
      resetBall(&ball);
      resetPaddle(&paddle_left);
      resetPaddle(&paddle_right);
      ball.frames_counter = 0;
      ball.change_x *= -1;
    }

    BeginDrawing();

    ClearBackground(screenBackground);

    // draw scores
    // left score
    DrawText(left_score_str, (float)GetScreenWidth()/2 - 70, 10, 30, GRAY);
    // right score
    DrawText(right_score_str, (float)GetScreenWidth()/2 + 50, 10, 30, GRAY);

    // draw line divider
    DrawLineEx((Vector2){(float)GetScreenWidth() / 2, 0},
               (Vector2){(float)GetScreenWidth() / 2, GetScreenHeight()}, 5,
               GRAY);

    drawPaddle(&paddle_left);
    drawPaddle(&paddle_right);

    drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();
}
