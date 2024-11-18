#include "raylib.h"
#include <stdio.h>

#include "constants.h"
#include "paddle.h"
#include "ball.h"
#include "bricks.h"
#include "collision_handler.h"

int main(void)
{
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
    SetTargetFPS(GAME_FPS);

    int lives = 5;
    char lives_str[LIVES_LENGTH];
    bool game_active = true;
    bool game_over = false;
    bool game_won = false;

    Paddle paddle;
    Ball ball;
    Bricks bricks;

    initPaddle(&paddle);
    initBall(&ball);
    initBricks(&bricks);

    while (!WindowShouldClose())
    {
        // game_over condition
        if (lives <= 0)
        {
            game_over = true;
        }

        // game_win condition - every brick inactive
        bool all_bricks_inactive = true;
        for (int i = 0; i < ROWS; i++)
        {
            for (int j = 0; j < COLS; j++)
            {
                if (bricks.list[i][j].active)
                {
                    all_bricks_inactive = false;
                    break;
                }
            }
        }
        if (all_bricks_inactive)
        {
            game_won = true;
        }

        // update game
        if (game_active)
        {
            // move paddle
            movePaddle(&paddle);
            // move ball
            moveBall(&ball);

            // collision
            paddleCollisionWalls(&paddle);
            ballCollisionWalls(&ball, &paddle, &lives);
            ballCollisionPaddle(&ball, &paddle);
            ballCollisionBricks(&ball, &bricks);
        }
        if (game_over || game_won)
        {
            game_active = false;

            if (IsKeyPressed(KEY_ENTER))
            {
                // reset game
                game_over = false;
                game_won = false;
                lives = 5;
                snprintf(lives_str, LIVES_LENGTH, "Lives: %d\n", lives);

                // reinitialize game components
                initBall(&ball);
                initBricks(&bricks);
                initPaddle(&paddle);

                // start game
                game_active = true;
            }
        }

        // conver lives to string
        snprintf(lives_str, LIVES_LENGTH, "Lives: %d\n", lives);

        // begin drawing program
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        if (game_active)
        {
            // draw lives
            DrawText(lives_str,
                     10,
                     GetScreenHeight() - 30,
                     30,
                     GRAY);
            // draw paddle
            drawPaddle(&paddle);
            // draw ball
            drawBall(&ball);
            // draw bricks
            drawBricks(&bricks);
        }
        if (game_over)
        {
            DrawRectangle(0,
                          0,
                          GetScreenWidth(),
                          GetScreenHeight(),
                          SKYBLUE);
            DrawText("Game Over",
                     (float)GetScreenWidth() / 2 - 90,
                     (float)GetScreenHeight() / 2 - 70,
                     40,
                     BLACK);
            DrawText("Press 'Enter' to continue",
                     (float)GetScreenWidth() / 2 - 160,
                     (float)GetScreenHeight() / 2,
                     30,
                     BLACK);
        }
        if (game_won)
        {
            DrawRectangle(0,
                          0,
                          GetScreenWidth(),
                          GetScreenHeight(),
                          SKYBLUE);
            DrawText("You Win",
                     (float)GetScreenWidth() / 2 - 70,
                     (float)GetScreenHeight() / 2 - 70,
                     40,
                     BLACK);
            DrawText("Press 'Enter' to continue",
                     (float)GetScreenWidth() / 2 - 160,
                     (float)GetScreenHeight() / 2,
                     30,
                     BLACK);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}