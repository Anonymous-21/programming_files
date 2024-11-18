#include "raylib.h"
#include "ball.h"
#include "paddle.h"
#include "bricks.h"

void paddleCollisionWalls(Paddle *paddle)
{
    if (paddle->x <= 0)
    {
        paddle->x = 0;
    }
    else if (paddle->x >= GetScreenWidth() - paddle->width)
    {
        paddle->x = GetScreenWidth() - paddle->width;
    }
}

void ballCollisionWalls(Ball *ball, Paddle *paddle, int *lives)
{
    if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius)
    {
        ball->change_x *= -1;
    }
    else if (ball->y <= ball->radius)
    {
        ball->change_y *= -1;
    }
    else if (ball->y >= GetScreenHeight() - ball->radius)
    {
        *lives -= 1;
        resetBall(ball);
        resetPaddle(paddle);
    }
}

void ballCollisionPaddle(Ball *ball, Paddle *paddle)
{
    if (CheckCollisionCircleRec((Vector2){ball->x, ball->y},
                                ball->radius,
                                (Rectangle){paddle->x,
                                            paddle->y,
                                            paddle->width,
                                            paddle->height}))
    {
        ball->change_y *= -1;
    }
}

void ballCollisionBricks(Ball *ball, Bricks *bricks)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            if (bricks->list[i][j].active)
            {
                if (CheckCollisionCircleRec((Vector2){ball->x, ball->y},
                                            ball->radius,
                                            (Rectangle){bricks->list[i][j].position.x,
                                                        bricks->list[i][j].position.y,
                                                        BRICK_WIDTH,
                                                        BRICK_HEIGHT}))
                {
                    bricks->list[i][j].active = false;
                    ball->change_y *= -1;
                }
            }
        }
    }
}