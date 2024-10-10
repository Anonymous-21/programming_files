#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Ball Ball;

typedef struct Paddle {
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;

} Paddle;

void initPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle);
void paddleCollisionBall(Paddle *paddle, Ball *ball);

#endif // PADDLE_H
