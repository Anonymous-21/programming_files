#include "ball.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->initial_x = (float)GetScreenWidth() / 2;
  ball->initial_y = (float)GetScreenHeight() / 2 - ball->radius / 2;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->color = RED;
  ball->change_x = 5;
  ball->change_y = 6;
  ball->frames_counter = 0;
}

void ballReset(Ball *ball) {
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->change_x *= -1;
}

void drawBall(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void moveBall(Ball *ball) {
  // 1 sec delay
  ball->frames_counter++;
  if (ball->frames_counter > 60) {
    ball->frames_counter = 61;
    ball->x += ball->change_x;
    ball->y += ball->change_y;
  }
}

void ballCollisionVerticalWalls(Ball *ball) {
  if (ball->y <= ball->radius || ball->y >= GetScreenHeight() - ball->radius) {
    ball->change_y *= -1;
  }
}
