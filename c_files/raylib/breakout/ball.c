#include "ball.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->x = (float)GetScreenWidth() / 2 - (float)ball->radius / 2;
  ball->y = (float)GetScreenHeight() / 2 - (float)ball->radius / 2;
  ball->color = RED;
  ball->speed_x = 5;
  ball->speed_y = 6;
  ball->active = false;
}

void DrawBall(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void moveBall(Ball *ball) {

  ball->x += ball->speed_x;
  ball->y += ball->speed_y;

  if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius) {
    ball->speed_x *= -1;
  } else if (ball->y <= ball->radius ||
             ball->y >= GetScreenHeight() - ball->radius) {
    ball->speed_y *= -1;
  }
}
