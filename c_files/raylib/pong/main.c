#include "ball.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitlte[] = "Pong";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  const int LEFT_SCORE_LENGTH = 10;
  const int RIGHT_SCORE_LENGTH = 10;

  InitWindow(screenWidth, screenHeight, screenTitlte);
  SetTargetFPS(gameFps);

  int left_score = 0;
  int right_score = 0;
  char left_score_str[LEFT_SCORE_LENGTH];
  char right_score_str[RIGHT_SCORE_LENGTH];

  Paddle paddle_left;
  Paddle paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);
  initBall(&ball);

  while (!WindowShouldClose()) {
    // paddles
    movePaddle(&paddle_left, KEY_W, KEY_S);
    movePaddle(&paddle_right, KEY_UP, KEY_DOWN);

    // ball
    moveBall(&ball);
    ballCollisionWalls(&ball, &left_score, &right_score);

    // update score and convert to string
    snprintf(left_score_str, LEFT_SCORE_LENGTH, "%d\n", left_score);
    snprintf(right_score_str, RIGHT_SCORE_LENGTH, "%d\n", right_score);

    // paddle collision ball
    if (CheckCollisionCircleRec((Vector2){ball.x, ball.y}, ball.radius,
                                (Rectangle){paddle_left.x, paddle_left.y,
                                            paddle_left.width,
                                            paddle_right.height})) {
      ball.change_x *= -1;
    } else if (CheckCollisionCircleRec(
                   (Vector2){ball.x, ball.y}, ball.radius,
                   (Rectangle){paddle_right.x, paddle_right.y,
                               paddle_right.width, paddle_right.height})) {
      ball.change_x *= -1;
    }

    // begin drawing
    BeginDrawing();
    ClearBackground(screenBackground);

    // draw screen divider
    DrawLineEx((Vector2){(float)GetScreenWidth() / 2, 0},
               (Vector2){(float)GetScreenWidth() / 2, GetScreenHeight()}, 5,
               GRAY);

    // draw scores
    DrawText(left_score_str, GetScreenWidth() / 2 - 70, 20, 30, GRAY);
    DrawText(right_score_str, GetScreenWidth() / 2 + 50, 20, 30, GRAY);

    // draw paddles
    drawPaddle(&paddle_left);
    drawPaddle(&paddle_right);

    // draw ball
    drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
