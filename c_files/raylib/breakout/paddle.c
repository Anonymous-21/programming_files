#include "paddle.h"
#include "ball.h"
#include "raylib.h"

void initPaddle(Paddle *paddle) {
  paddle->width = 100;
  paddle->height = 10;
  paddle->x = GetScreenWidth() / 2 - paddle->width / 2;
  paddle->y = GetScreenHeight() - 10 - paddle->height / 2;
  paddle->color = BLACK;
  paddle->speed = 5;
}

void drawPaddle(Paddle *paddle) {
  DrawRectangleRec(
      (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
      paddle->color);
}

void movePaddle(Paddle *paddle) {
  if (IsKeyDown(KEY_LEFT) && paddle->x >= 0) {
    paddle->x -= paddle->speed;
  } else if (IsKeyDown(KEY_RIGHT) &&
             paddle->x <= GetScreenWidth() - paddle->width) {
    paddle->x += paddle->speed;
  }
}

void paddleCollisionBall(Paddle *paddle, Ball *ball) {
  if (CheckCollisionCircleRec(
          (Vector2){ball->x, ball->y}, ball->radius,
          (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height})) {
    ball->change_y *= -1;
  }
}
