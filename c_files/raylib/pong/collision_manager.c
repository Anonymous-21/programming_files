#include "collision_manager.h"
#include "ball.h"
#include "paddle.h"
#include "raylib.h"

void paddleCollisionWalls(Paddle *paddle) {
  if (paddle->y < 0) {
    paddle->y = 0;
  } else if (paddle->y > GetScreenHeight() - paddle->height) {
    paddle->y = GetScreenHeight() - paddle->height;
  }
}

void ballCollisionPaddle(Ball *ball, Paddle *paddle) {
  if (CheckCollisionCircleRec(
          (Vector2){ball->x, ball->y}, ball->radius,
          (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height})) {
    ball->change_x *= -1;
  }
}

void ballVerticalCollision(Ball *ball) {
  if (ball->y <= ball->radius || ball->y >= GetScreenHeight() - ball->radius) {
    ball->change_y *= -1;
  }
}

void ballHorizontalCollision(Ball *ball, Paddle *paddle_left,
                             Paddle *paddle_right, int *left_score,
                             int *right_score) {
  if (ball->x < ball->radius) {
    *right_score += 1;
    resetBall(ball);
    resetPaddle(paddle_left);
    resetPaddle(paddle_right);
  } else if (ball->x > GetScreenWidth() - ball->radius) {
    *left_score += 1;
    resetBall(ball);
    resetPaddle(paddle_left);
    resetPaddle(paddle_right);
  }
}
