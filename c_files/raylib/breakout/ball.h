#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball {

  float radius;
  float initial_x;
  float initial_y;
  float x;
  float y;
  Color color;
  float speed_x;
  float speed_y;
  bool active;

} Ball;

void initBall(Ball *ball);
void resetBall(Ball *ball);
void drawBall(Ball *ball);
void updateBall(Ball *ball);

#endif // BALL_H
