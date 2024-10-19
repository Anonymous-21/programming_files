#include "ball.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->initial_x = (float)GetScreenWidth() / 2 - (float)ball->radius / 2;
  ball->initial_y = (float)GetScreenHeight() / 2 - (float)ball->radius / 2;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->color = RED;
  ball->speed_x = 5;
  ball->speed_y = 6;
  ball->active = false;
}

void resetBall(Ball *ball) {
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
}

void DrawBall(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

int moveBall(Ball *ball, int lives, bool *game_paused) {

  ball->x += ball->speed_x;
  ball->y += ball->speed_y;

  if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius) {
    ball->speed_x *= -1;
  } else if (ball->y <= ball->radius) {
    ball->speed_y *= -1;
  } else if (ball->y >= GetScreenHeight() - ball->radius) {
    lives--;
    resetBall(ball);
    *game_paused = true;
  }

  return lives;
}
