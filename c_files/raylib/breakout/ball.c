#include "ball.h"
#include "bricks.h"
#include "constants.h"
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

void updateBall(Ball *ball, Paddle *paddle, Bricks *bricks, int *lives) {
  // move ball
  ball->x += ball->change_x;
  ball->y += ball->change_y;

  // ball collision walls
  if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius) {
    ball->change_x *= -1;
  }

  if (ball->y <= ball->radius) {
    ball->change_y *= -1;
  } else if (ball->y >= GetScreenHeight() - ball->radius) {
    *lives -= 1;
    resetBall(ball);
    resetPaddle(paddle);
  }

  // ball collision paddle
  if (CheckCollisionCircleRec(
          (Vector2){ball->x, ball->y}, ball->radius,
          (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height})) {
    ball->change_y *= -1;
  }

  // ball collision bricks
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (CheckCollisionCircleRec(
              (Vector2){ball->x, ball->y}, ball->radius,
              (Rectangle){bricks->list[i * 10 + j].coordinates.x,
                          bricks->list[i * 10 + j].coordinates.y, BRICK_WIDTH,
                          BRICK_HEIGHT})) {
        bricks->list[i * 10 + j].is_active = false;
        ball->change_y *= -1;
      }
    }
  }
}
