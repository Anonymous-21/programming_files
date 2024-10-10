#ifndef BALL_H
#define BALL_H

#include "paddle.h"
#include "raylib.h"

typedef struct Paddle Paddle;

typedef struct Ball {
  int x;
  int y;
  int radius;
  Color color;
  int change_x;
  int change_y;
  bool active;

} Ball;

void initBall(Ball *ball);
void drawBall(Ball *ball);
int moveBall(Ball *ball, int lives);

#endif // BALL_H
