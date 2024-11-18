#include "raylib.h"

#include "paddle.h"

void initPaddle(Paddle *paddle)
{
    paddle->width = 100;
    paddle->height = 10;
    paddle->initial_x = (float)GetScreenWidth() / 2 - paddle->width / 2;
    paddle->initial_y = GetScreenHeight() - paddle->height - 20;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->color = BLACK;
    paddle->change_x = 8;
}

void resetPaddle(Paddle *paddle)
{
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
}

void drawPaddle(Paddle *paddle)
{
    DrawRectangleRec((Rectangle){paddle->x,
                                 paddle->y,
                                 paddle->width,
                                 paddle->height},
                     paddle->color);
}

void movePaddle(Paddle *paddle)
{
    if (IsKeyDown(KEY_LEFT))
    {
        paddle->x -= paddle->change_x;
    }
    else if (IsKeyDown(KEY_RIGHT))
    {
        paddle->x += paddle->change_x;
    }
}