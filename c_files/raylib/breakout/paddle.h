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

void initPaddle(Paddle *paddle);
void resetPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle);

#endif // PADDLE_H
