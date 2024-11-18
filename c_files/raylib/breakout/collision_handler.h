#ifndef COLLISION_HANDLER_H
#define COLLISION_HANDLER_H

#include "paddle.h"
#include "ball.h"
#include "bricks.h"

void paddleCollisionWalls(Paddle *paddle);
void ballCollisionWalls(Ball *ball, Paddle *paddle, int *lives);
void ballCollisionPaddle(Ball *ball, Paddle *paddle);
void ballCollisionBricks(Ball *ball, Bricks *bricks);

#endif // COLLISION_HANDLER_H