#include <math.h>
#include "raylib.h"

#include "paddle.h"
#include "ball.h"

void paddle_initialize(Paddle *paddle, float x)
{
    paddle->width = 10;
    paddle->height = 100;
    paddle->initial_x = x;
    paddle->initial_y = (float)GetScreenHeight() / 2 - paddle->height / 2;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->color = BLACK;
    paddle->speed = 5;
    paddle->ai_speed = 7;
}

void paddle_reset(Paddle *paddle)
{
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
}

void paddle_draw(Paddle *paddle)
{
    DrawRectangleRec(
        (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
        paddle->color);
}

void paddle_left_update(Paddle *paddle)
{
    if (IsKeyDown(KEY_W) && paddle->y >= 0)
    {
        paddle->y -= paddle->speed;
    }
    else if (IsKeyDown(KEY_S) &&
             paddle->y <= GetScreenHeight() - paddle->height)
    {
        paddle->y += paddle->speed;
    }
}

void paddle_right_update(Paddle *paddle_right, Ball *ball)
{
    if (ball->x > (float)GetScreenWidth() / 2)
    {
        float distance_x = ball->x - (paddle_right->x + paddle_right->width / 2);
        float distance_y = ball->y - (paddle_right->y + paddle_right->height / 2);
        float distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));
        if (distance > 0)
        {
            distance_y /= distance;

            paddle_right->y += distance_y * paddle_right->ai_speed;
        }
    }

    if (paddle_right->y <= 0)
    {
        paddle_right->y = 0;
    }
    else if (paddle_right->y <= GetScreenHeight() - paddle_right->height)
    {
        paddle_right->y = GetScreenHeight() - paddle_right->height;
    }
}