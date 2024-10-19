#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Paddle
{
  float x;
  float y;
  float width;
  float height;
  Color color;
  float speed;
  
}Paddle;

void initPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle);

#endif // PADDLE_H
