#ifndef PADDLE_H
#define PADDLE_H

#include "raylib.h"

typedef struct Ball Ball;

typedef struct Paddle
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;
    float ai_speed;

} Paddle;

void paddle_initialize(Paddle *paddle, float x);
void paddle_reset(Paddle *paddle);
void paddle_draw(Paddle *paddle);
void paddle_left_update(Paddle *paddle_left);
void paddle_right_update(Paddle *paddle_right, Ball *ball);


#endif