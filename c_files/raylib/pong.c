#include "raylib.h"
#include <stdio.h>
#include <math.h>

#define SCORE_STR_LENGTH 10

/*
    PADDLE
*/

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

} Paddle;

void initPaddle(Paddle *paddle, float x, float speed)
{
    paddle->width = 10;
    paddle->height = 100;
    paddle->initial_x = x;
    paddle->initial_y = (float)GetScreenHeight() / 2 - paddle->height / 2;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->color = BLACK;
    paddle->speed = speed;
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

void updatePaddle(Paddle *paddle)
{
    if ((IsKeyDown(KEY_W) || IsKeyDown(KEY_UP)) &&
        paddle->y >= 0)
    {
        paddle->y -= paddle->speed;
    }
    else if ((IsKeyDown(KEY_S) || IsKeyDown(KEY_DOWN)) &&
             paddle->y + paddle->height <= GetScreenHeight())
    {
        paddle->y += paddle->speed;
    }
}

/*
    BALL
*/

typedef struct Ball
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float radius;
    Color color;
    float speed_x;
    float speed_y;
    bool active;

} Ball;

void initBall(Ball *ball)
{
    ball->radius = 10;
    ball->initial_x = (float)GetScreenWidth() / 2 - ball->radius;
    ball->initial_y = (float)GetScreenHeight() / 2 - ball->radius;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->color = RED;
    ball->speed_x = 6;
    ball->speed_y = 7;
    ball->active = false;
}

void resetBall(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed_x *= -1;
    ball->active = false;
}

void drawBall(Ball *ball)
{
    if (!ball->active && (int)GetTime() % 2 == 0)
    {
        DrawText("Press SPACE to begin!",
                 GetScreenWidth() / 2 - 160,
                 GetScreenHeight() - 50,
                 30,
                 BLACK);
    }

    DrawCircleV((Vector2){ball->x, ball->y},
                ball->radius,
                ball->color);
}

void updateBall(Ball *ball, Paddle *paddle_left, Paddle *ai, int *score_left, int *score_right)
{
    if (IsKeyPressed(KEY_SPACE))
    {
        ball->active = true;
    }

    if (ball->active)
    {
        ball->x += ball->speed_x;
        ball->y += ball->speed_y;
    }

    if (ball->x - ball->radius < 0)
    {
        *score_right += 1;
        resetBall(ball);
        resetPaddle(paddle_left);
        resetPaddle(ai);
    }
    else if (ball->x + ball->radius > GetScreenWidth())
    {
        *score_left += 1;
        resetBall(ball);
        resetPaddle(paddle_left);
        resetPaddle(ai);
    }

    if (ball->y - ball->radius <= 0 || ball->y + ball->radius > GetScreenHeight())
    {
        ball->speed_y *= -1;
    }

    // BALL COLLISION PADDLE
    if (CheckCollisionCircleRec((Vector2){ball->x, ball->y},
                                ball->radius,
                                (Rectangle){paddle_left->x,
                                            paddle_left->y,
                                            paddle_left->width,
                                            paddle_left->height}))
    {
        ball->speed_x *= -1;
    }
    else if (CheckCollisionCircleRec((Vector2){ball->x, ball->y},
                                     ball->radius,
                                     (Rectangle){ai->x,
                                                 ai->y,
                                                 ai->width,
                                                 ai->height}))
    {
        ball->speed_x *= -1;
    }
}

/*
    ENEMY AI
*/
void aiFollowBall(Paddle *ai, Ball *ball)
{
    if (ball->x + ball->radius > (float)GetScreenWidth() / 2 + 100)
    {
        float distance_x = ball->x - (ai->x + ai->width / 2);
        float distance_y = ball->y - (ai->y + ai->height / 2);
        float distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

        if (distance > 0)
        {
            distance_x /= distance;
            distance_y /= distance;

            if (ball->y < ai->y)
            {
                ai->y -= ai->speed;
            }
            else if (ball->y > ai->y + ai->height)
            {
                ai->y += ai->speed;
            }
        }
    }
}

/*
    MAIN LOOP
*/

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Pong";
    const Color screenBackground = SKYBLUE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    int score_left = 0;
    int score_right = 0;
    char score_left_str[SCORE_STR_LENGTH];
    char score_right_str[SCORE_STR_LENGTH];

    Paddle paddle_left;
    Paddle ai;
    Ball ball;

    initPaddle(&paddle_left, 10, 5);
    initPaddle(&ai, GetScreenWidth() - paddle_left.width - 10, 7);
    initBall(&ball);

    while (!WindowShouldClose())
    {
        // CONVERT SCORES TO STRINGS
        snprintf(score_left_str, SCORE_STR_LENGTH, "%d\n", score_left);
        snprintf(score_right_str, SCORE_STR_LENGTH, "%d\n", score_right);

        updatePaddle(&paddle_left);
        aiFollowBall(&ai, &ball);
        updateBall(&ball, &paddle_left, &ai, &score_left, &score_right);

        BeginDrawing();
        ClearBackground(screenBackground);

        // DRAW SCORES
        // (str, x, y, font_size, color)
        DrawText(score_left_str,
                 120,
                 20,
                 40,
                 BLACK);
        DrawText(score_right_str,
                 GetScreenWidth() - 140,
                 20,
                 40,
                 BLACK);

        drawPaddle(&paddle_left);
        drawPaddle(&ai);
        drawBall(&ball);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}