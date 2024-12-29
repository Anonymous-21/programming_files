#ifndef BALL_H
#define BALL_H

#include "raylib.h"

typedef struct Ball
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float radius;
    Color color;
    float initial_speed_x;
    float initial_speed_y;
    float speed_x;
    float speed_y;
    float speed_increment;
    bool is_active;

} Ball;

void ball_initialize(Ball *ball);
void ball_reset(Ball *ball);
void ball_draw(Ball *ball);
void ball_update(Ball *ball);

#endif