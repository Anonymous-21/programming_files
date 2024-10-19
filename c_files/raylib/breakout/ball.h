#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball {
  float radius;
  float x;
  float y;
  Color color;
  float speed_x;
  float speed_y;
  bool active;

} Ball;

void initBall(Ball *ball);
void DrawBall(Ball *ball);
void moveBall(Ball *ball);

#endif // BALL_H
