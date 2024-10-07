#ifndef PADDLE_H
#define PADDLE_H

#include "ball.h"
#include "raylib.h"

typedef struct Paddle {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float width;
  float height;
  float speed;
  Color color;
} Paddle;

void initPaddle(Paddle *paddle, float x);
void resetPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle, KeyboardKey key_up, KeyboardKey key_down);
void collisionPaddleBall(Paddle *paddle, Ball *ball);

#endif // PADDLE_H
