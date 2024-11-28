#include "ball.h"
#include "paddle.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->initial_x = (float)GetScreenWidth() / 2;
  ball->initial_y = (float)GetScreenHeight() / 2;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->color = RED;
  ball->change_x = 5;
  ball->change_y = 6;
}

void resetBall(Ball *ball) {
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->change_x *= -1;
}

void drawBall(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void updateBall(Ball *ball, Paddle *paddle_left, Paddle *paddle_right,
                int *score_left, int *score_right) {
  // move ball
  ball->x += ball->change_x;
  ball->y += ball->change_y;

  // ball collision wall
  if (ball->y <= ball->radius || ball->y >= GetScreenHeight() - ball->radius) {
    ball->change_y *= -1;
  }

  // update score
  if (ball->x < 0) {
    *score_right += 1;
    resetBall(ball);
    resetPaddle(paddle_left);
    resetPaddle(paddle_right);

  } else if (ball->x >= GetScreenWidth()) {
    *score_left += 1;
    resetBall(ball);
    resetPaddle(paddle_left);
    resetPaddle(paddle_right);
  }
}
