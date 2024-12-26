#include "raylib.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

#define SCORE_STR_LENGTH 5

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
    float ai_speed;

} Paddle;

void initPaddle(Paddle *paddle, float x)
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
    if (IsKeyDown(KEY_W) && paddle->y >= 0)
    {
        paddle->y -= paddle->speed;
    }
    else if (IsKeyDown(KEY_S) && paddle->y <= GetScreenWidth() - paddle->width)
    {
        paddle->y += paddle->speed;
    }
}

void updateAiPaddle(Paddle *paddle, float ball_x, float ball_y)
{
    if (ball_x > (float)GetScreenWidth() / 2)
    {
        float distance_x = ball_x - (paddle->x + paddle->width / 2);
        float distance_y = ball_y - (paddle->y + paddle->height / 2);
        float distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

        if (distance > 0)
        {
            distance_y /= distance;

            paddle->y += distance_y * paddle->ai_speed;
        }
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
    float initial_speed_x;
    float initial_speed_y;
    float speed_x;
    float speed_y;
    float speed_increment;
    float frames_counter;

} Ball;

void initBall(Ball *ball)
{
    ball->initial_x = (float)GetScreenWidth() / 2;
    ball->initial_y = (float)GetScreenHeight() / 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->radius = 10.0f;
    ball->color = RED;
    ball->initial_speed_x = 4.0f;
    ball->initial_speed_y = 5.0f;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_increment = 0.005f;
}

void resetBall(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed_x *= -1;
    ball->frames_counter = 0;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
}

void drawBall(Ball *ball)
{
    DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void updateBall(Ball *ball)
{
    ball->frames_counter++;
    if (ball->frames_counter >= 60)
    {
        ball->frames_counter = 61;

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

/*
    GAME
*/
typedef struct Game
{
    int score_left;
    int score_right;
    char score_left_str[SCORE_STR_LENGTH];
    char score_right_str[SCORE_STR_LENGTH];

    Paddle paddle_left;
    Paddle ai;
    Ball ball;

} Game;

void initGame(Game *game)
{
    game->score_left = 0;
    game->score_right = 0;

    initPaddle(&game->paddle_left, 10);
    initPaddle(&game->ai, GetScreenWidth() - game->paddle_left.width - 10);
    initBall(&game->ball);
}

void resetGame(Game *game)
{
    resetPaddle(&game->paddle_left);
    resetPaddle(&game->ai);
    resetBall(&game->ball);
}

void drawGame(Game *game)
{
    // draw scores
    DrawText(game->score_left_str,
             200,
             30,
             40,
             BLACK);
    DrawText(game->score_right_str,
             GetScreenWidth() - 220,
             30,
             40,
             BLACK);

    drawPaddle(&game->paddle_left);
    drawPaddle(&game->ai);
    drawBall(&game->ball);
}

void updateGame(Game *game)
{
    // convert score to string
    snprintf(game->score_left_str, SCORE_STR_LENGTH, "%d\n", game->score_left);
    snprintf(game->score_right_str, SCORE_STR_LENGTH, "%d\n", game->score_right);

    updatePaddle(&game->paddle_left);
    updateAiPaddle(&game->ai, game->ball.x, game->ball.y);
    updateBall(&game->ball);

    // ball collision paddle
    if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                game->ball.radius,
                                (Rectangle){game->paddle_left.x,
                                            game->paddle_left.y,
                                            game->paddle_left.width,
                                            game->paddle_left.height}))
    {
        game->ball.speed_x *= -1;
    }
    else if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                     game->ball.radius,
                                     (Rectangle){game->ai.x,
                                                 game->ai.y,
                                                 game->ai.width,
                                                 game->ai.height}))
    {
        game->ball.speed_x *= -1;
    }

    // update scores
    if (game->ball.x <= 0)
    {
        game->score_right++;
        resetGame(game);
    }
    else if (game->ball.x >= GetScreenWidth())
    {
        game->score_left++;
        resetGame(game);
    }
}

/*
    RAYLIB WINDOW
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

    Game game;

    initGame(&game);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(screenBackground);

        drawGame(&game);
        updateGame(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}