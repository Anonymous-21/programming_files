#include "paddle.h"
#include "raylib.h"

void initPaddle(Paddle *paddle, int x) {
  paddle->width = 10;
  paddle->height = 100;
  paddle->x = x;
  paddle->y = GetScreenHeight() / 2 - paddle->height / 2;
  paddle->color = BLACK;
}

void drawPaddle(Paddle *paddle) {
  DrawRectangleRec(
      (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
      paddle->color);
}
