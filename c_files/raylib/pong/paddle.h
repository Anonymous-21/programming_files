#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Paddle {
  int x;
  int y;
  int width;
  int height;
  Color color;

} Paddle;

void initPaddle(Paddle *paddle, int x);
void drawPaddle(Paddle *paddle);

#endif // PADDLE_H
