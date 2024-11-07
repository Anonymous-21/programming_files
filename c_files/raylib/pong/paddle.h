#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Paddle {
  int initial_x;
  int initial_y;
  int x;
  int y;
  int width;
  int height;
  Color color;
  int speed;

} Paddle;

void initPaddle(Paddle *paddle, int x);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle, KeyboardKey key_up, KeyboardKey key_down);

#endif // PADDLE_H
