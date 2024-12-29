#include "raylib.h"

#include "ball.h"

void ball_initialize(Ball *ball)
{
    ball->initial_x = (float)GetScreenWidth() / 2;
    ball->initial_y = (float)GetScreenHeight() / 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->radius = 10;
    ball->color = RED;
    ball->initial_speed_x = 5;
    ball->initial_speed_y = 5;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_increment = 0.005;
    ball->is_active = false;
}

void ball_reset(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_x *= -1;
    ball->is_active = false;
}

void ball_draw(Ball *ball)
{
    DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void ball_update(Ball *ball)
{
    if (IsKeyDown(KEY_SPACE))
    {
        ball->is_active = true;
    }

    if (ball->is_active)
    {
        ball->x += ball->speed_x;
        ball->y += ball->speed_y;

        ball->speed_x += ball->speed_increment;
        ball->speed_y += ball->speed_increment;
    }

    if (ball->y <= ball->radius || ball->y >= GetScreenHeight() - ball->radius)
    {
        ball->speed_y *= -1;
    }
}