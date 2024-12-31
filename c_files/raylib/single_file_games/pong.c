#include "raylib.h"
#include <math.h>
#include <stdio.h>

#define SCORE_STR_LENGTH 10

//**************************************
// BALL
//**************************************

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
    bool active;

} Ball;

void init_ball(Ball *ball)
{
    ball->initial_x = (float)GetScreenWidth() / 2;
    ball->initial_y = (float)GetScreenHeight() / 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->radius = 10;
    ball->color = RED;
    ball->initial_speed_x = 4.0f;
    ball->initial_speed_y = 4.0f;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_increment = 0.0005f;
    ball->active = false;
}

void reset_ball(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_x *= -1;
    ball->active = false;
}

void draw_ball(Ball *ball)
{
    DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void update_ball(Ball *ball)
{
    if (IsKeyPressed(KEY_SPACE))
    {
        ball->active = true;
    }

    if (ball->active)
    {
        ball->x += ball->speed_x;
        ball->y += ball->speed_y;

        // increment ball speed
        if (ball->speed_x > 0)
        {
            ball->speed_x += ball->speed_increment;
        }
        else if (ball->speed_x < 0)
        {
            ball->speed_x -= ball->speed_increment;
        }
        else if (ball->speed_y > 0)
        {
            ball->speed_x += ball->speed_increment;
        }
        else if (ball->speed_x < 0)
        {
            ball->speed_x -= ball->speed_increment;
        }
    }

    // ball vertical bounds
    if (ball->y <= ball->radius || ball->y >= GetScreenHeight() - ball->radius)
    {
        ball->speed_y *= -1;
    }
}

//**************************************
// PADDLE
//**************************************

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

void init_paddle(Paddle *paddle, float x)
{
    paddle->width = 10.0f;
    paddle->height = 100.0f;
    paddle->initial_x = x;
    paddle->initial_y = (float)GetScreenHeight() / 2 - paddle->height / 2;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->color = BLACK;
    paddle->speed = 5.0f;
    paddle->ai_speed = 7.0f;
}

void reset_paddle(Paddle *paddle)
{
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
}

void draw_paddle(Paddle *paddle)
{
    DrawRectangleRec((Rectangle){paddle->x,
                                 paddle->y,
                                 paddle->width,
                                 paddle->height},
                     paddle->color);
}

void update_paddle_left(Paddle *paddle_left)
{
    if (IsKeyDown(KEY_W) && paddle_left->y >= 0)
    {
        paddle_left->y -= paddle_left->speed;
    }
    else if (IsKeyDown(KEY_S) && paddle_left->y <= GetScreenHeight() - paddle_left->height)
    {
        paddle_left->y += paddle_left->speed;
    }
}

void update_paddle_ai(Paddle *paddle_ai, Ball *ball)
{
    if (ball->x > GetScreenWidth() / 2)
    {
        float distance_x = ball->x - (paddle_ai->x + paddle_ai->width / 2);
        float distance_y = ball->y - (paddle_ai->y + paddle_ai->height / 2);
        float distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));
        if (distance > 0)
        {
            distance_y /= distance;

            paddle_ai->y += distance_y * paddle_ai->ai_speed;
        }
    }
}

//**************************************
// MAIN LOOP
//**************************************

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
    Paddle paddle_ai;
    Ball ball;

    init_paddle(&paddle_left, 10.0f);
    init_paddle(&paddle_ai, GetScreenWidth() - paddle_left.width - 10.0f);
    init_ball(&ball);

    while (!WindowShouldClose())
    {
        // convert score to string
        snprintf(score_left_str, SCORE_STR_LENGTH, "%d\n", score_left);
        snprintf(score_right_str, SCORE_STR_LENGTH, "%d\n", score_right);

        update_paddle_left(&paddle_left);
        update_paddle_ai(&paddle_ai, &ball);
        update_ball(&ball);

        // ball horizontal bounds
        if (ball.x < 0)
        {
            score_right++;
            reset_paddle(&paddle_left);
            reset_paddle(&paddle_ai);
            reset_ball(&ball);
        }
        else if (ball.x > GetScreenWidth())
        {
            score_left++;
            reset_paddle(&paddle_left);
            reset_paddle(&paddle_ai);
            reset_ball(&ball);
        }

        // ball collision paddles
        if (CheckCollisionCircleRec((Vector2){ball.x, ball.y},
                                    ball.radius,
                                    (Rectangle){paddle_left.x,
                                                paddle_left.y,
                                                paddle_left.width,
                                                paddle_left.height}))
        {
            ball.speed_x *= -1;
        }
        else if (CheckCollisionCircleRec((Vector2){ball.x, ball.y},
                                         ball.radius,
                                         (Rectangle){paddle_ai.x,
                                                     paddle_ai.y,
                                                     paddle_ai.width,
                                                     paddle_ai.height}))
        {
            ball.speed_x *= -1;
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        // draw scores
        DrawText(score_left_str, 200, 30, 40, BLACK);
        DrawText(score_right_str, GetScreenWidth() - 220, 30, 40, BLACK);

        draw_paddle(&paddle_left);
        draw_paddle(&paddle_ai);
        draw_ball(&ball);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}