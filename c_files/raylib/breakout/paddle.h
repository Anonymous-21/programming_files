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
  float speed;

} Paddle;

void initPaddle(Paddle *paddle);
void resetPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void updatePaddle(Paddle *paddle);

#endif // PADDLE_H
