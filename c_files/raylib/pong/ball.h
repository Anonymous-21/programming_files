#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Paddle Paddle;

typedef struct Ball {
  float radius;
  float initial_x;
  float initial_y;
  float x;
  float y;
  Color color;
  float change_x;
  float change_y;

} Ball;

void initBall(Ball *ball);
void resetBall(Ball *ball);
void drawBall(Ball *ball);
void updateBall(Ball *ball, Paddle *paddle_left, Paddle *paddle_right,
                int *score_left, int *score_right);

#endif // BALL_H
