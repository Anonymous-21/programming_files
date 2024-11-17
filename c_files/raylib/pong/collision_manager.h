#ifndef COLLISION_MANAGER_H
#define COLLISION_MANAGER_H

#include "raylib.h"

typedef struct Paddle Paddle;
typedef struct Ball Ball;

void paddleCollisionWalls(Paddle *paddle);
void ballVerticalCollision(Ball *ball);
void ballHorizontalCollision(Ball *ball, Paddle *paddle_left,
                             Paddle *paddle_right, int *left_score,
                             int *right_score);
void ballCollisionPaddle(Ball *ball, Paddle *paddle);

#endif // COLLISION_MANAGER_H
