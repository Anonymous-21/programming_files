#include "paddle.h"
#include "ball.h"
#include "raylib.h"

void initPaddle(Paddle *paddle, float x) {
  paddle->width = 10;
  paddle->height = 100;
  paddle->initial_x = x;
  paddle->initial_y = (float)GetScreenHeight() / 2 - paddle->height / 2;
  paddle->x = paddle->initial_x;
  paddle->y = paddle->initial_y;
  paddle->color = BLACK;
  paddle->speed = 8;
}

void paddleReset(Paddle *paddle) {
  paddle->x = paddle->initial_x;
  paddle->y = paddle->initial_y;
}

void drawPaddle(Paddle *paddle) {
  DrawRectangleRec(
      (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
      paddle->color);
}

void movePaddle(Paddle *paddle, KeyboardKey key_up, KeyboardKey key_down) {
  if (IsKeyDown(key_up) && paddle->y >= 0) {
    paddle->y -= paddle->speed;
  } else if (IsKeyDown(key_down) &&
             paddle->y <= GetScreenHeight() - paddle->height) {
    paddle->y += paddle->speed;
  }
}

void collisionPaddleBall(Paddle *paddle, Ball *ball) {
  if (CheckCollisionCircleRec(
          (Vector2){ball->x, ball->y}, ball->radius,
          (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height})) {
    ball->change_x *= -1;
  }
}
