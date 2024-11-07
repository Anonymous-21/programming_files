#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball {
  int radius;
  int initial_x;
  int initial_y;
  int x;
  int y;
  Color color;
  int change_x;
  int change_y;
  int frames_counter;

} Ball;

void initBall(Ball *ball);
void resetBall(Ball *ball);
void drawBall(Ball *ball);
void moveBall(Ball *ball);
void ballCollisionWalls(Ball *ball, int *left_score, int *right_score);

#endif // BALL_H
