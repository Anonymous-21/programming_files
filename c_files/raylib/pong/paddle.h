#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Ball Ball;

typedef struct Paddle {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float width;
  float height;
  Color color;
  int speed;

} Paddle;

void initPaddle(Paddle *paddle, float x);
void paddleReset(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle, KeyboardKey key_up, KeyboardKey key_down);
void collisionPaddleBall(Paddle *paddle, Ball *ball);

#endif // PADDLE_H
