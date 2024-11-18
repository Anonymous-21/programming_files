#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float width;
    float height;
    Color color;
    float change_x;

} Paddle;

void initPaddle(Paddle *paddle);
void resetPaddle(Paddle *paddle);
void drawPaddle(Paddle *paddle);
void movePaddle(Paddle *paddle);

#endif // PADDLE_H