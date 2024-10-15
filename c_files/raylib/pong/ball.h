#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball {
  int x;
  int y;
  int radius;
  Color color;

} Ball;

void initBall(Ball *ball);
void drawBall(Ball *ball);

#endif // BALL_H
