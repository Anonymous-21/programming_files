#include "ball.h"
#include "paddle.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->x = GetScreenWidth() / 2;
  ball->y = GetScreenHeight() / 2;
  ball->color = RED;
  ball->change_x = 5;
  ball->change_y = 6;
  ball->active = false;
}

void ballReset(Ball *ball) {
  ball->x = GetScreenWidth() / 2;
  ball->y = GetScreenHeight() / 2;
}

void drawBall(Ball *ball) {
  DrawCircle(ball->x, ball->y, ball->radius, ball->color);
}

int moveBall(Ball *ball, int lives) {
  // activate ball
  if (IsKeyPressed(KEY_SPACE))
  {
    ball->active = true;
  }

  // move ball
  if (ball->active)
  {
    ball->x += ball->change_x;
    ball->y += ball->change_y;
  }

  // set ball direction based on wall collisions
  if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius) {
    ball->change_x *= -1;
  } else if (ball->y <= ball->radius) {
    ball->change_y *= -1;
  } else if (ball->y >= GetScreenHeight() - ball->radius) {
    lives--;
    ball->active = false;
    ballReset(ball);
  }

  return lives;
}
