#include "ball.h"
#include "raylib.h"

void initBall(Ball *ball) {
  ball->radius = 10;
  ball->x = GetScreenWidth() / 2 - ball->radius;
  ball->y = GetScreenHeight() / 2 - ball->radius;
  ball->color = RED;
}

void drawBall(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}
