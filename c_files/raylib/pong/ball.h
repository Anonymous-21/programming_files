#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball {
  float radius;
  float initial_x;
  float initial_y;
  float x;
  float y;
  float change_x;
  float change_y;
  Color color;
  int frames_counter;
} Ball;

void initBall(Ball *ball);
void resetBall(Ball *ball);
void drawBall(Ball *ball);
void moveBall(Ball *ball);

#endif // BALL_H
