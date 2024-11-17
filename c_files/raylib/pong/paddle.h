#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Paddle {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float width;
  float height;
  Color color;
  float change_y;
} Paddle;

void initPaddle(Paddle *paddle, float x);
void resetPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle, KeyboardKey key_up, KeyboardKey key_down);

#endif // PADDLE_H
