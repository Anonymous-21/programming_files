#include "paddle.h"
#include "raylib.h"

void initPaddle(Paddle *paddle) {
  paddle->width = 100;
  paddle->height = 10;
  paddle->x = (float)GetScreenWidth() / 2 - (float)paddle->width / 2;
  paddle->y = GetScreenHeight() - paddle->height - 20;
  paddle->color = BLACK;
  paddle->speed = 8;
}

void drawPaddle(Paddle *paddle) {
  DrawRectangleRec(
      (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
      paddle->color);
}

void movePaddle(Paddle *paddle) {
  if (IsKeyDown(KEY_RIGHT) && paddle->x <= GetScreenWidth() - paddle->width) {
    paddle->x += paddle->speed;
  } else if (IsKeyDown(KEY_LEFT) && paddle->x >= 0) {
    paddle->x -= paddle->speed;
  }
}
