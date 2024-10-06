#include <stdbool.h>
#include <stdio.h>
#include "raylib.h"

#define MAX 10

void ball_reset(int *ball_x,  int *ball_y, int ball_initial_x, int ball_initial_y);
void paddle_reset(int *paddle_y, int paddle_intial_y);

void ball_reset(int *ball_x, int *ball_y, int ball_initial_x, int ball_initial_y)
{
    *ball_x = ball_initial_x;
    *ball_y = ball_initial_y;
}

void paddle_reset(int *paddle_y, int paddle_initial_y)
{
    *paddle_y = paddle_initial_y;
}

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Pong";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    char left_score_str[MAX], right_score_str[MAX];

    bool game_over = false;
    int frames_counter = 0;
    int left_score = 0;
    int right_score = 0;

    // paddle
    int paddle_width = 10;
    int paddle_height = 100;
    Color paddle_color = BLACK;
    int paddle_initial_y = GetScreenHeight() / 2 - paddle_height / 2;
    int paddle_speed = 8;

    int paddle_left_initial_x = 10;
    int paddle_left_x = paddle_left_initial_x;
    int paddle_left_y = paddle_initial_y;

    int paddle_right_initial_x = GetScreenWidth() - paddle_width - 10;
    int paddle_right_x = paddle_right_initial_x;
    int paddle_right_y = paddle_initial_y;

    // ball
    int ball_radius = 10;
    int ball_initial_x = GetScreenWidth() / 2;
    int ball_initial_y = GetScreenHeight() / 2 - ball_radius;
    int ball_x = ball_initial_x;
    int ball_y = ball_initial_y;
    Color ball_color = RED;
    int ball_change_x = 5;
    int ball_change_y = 6;

    while (!WindowShouldClose())
    {
        if (!game_over)
        {
            // convert score to string
            snprintf(left_score_str, MAX, "%d\n", left_score);
            snprintf(right_score_str, MAX, "%d\n", right_score);
            
            // move paddles
            // left paddle
            if (IsKeyDown(KEY_W) && paddle_left_y >= 0)
            {
                paddle_left_y -= paddle_speed;
            }
            else if (IsKeyDown(KEY_S) && paddle_left_y <= GetScreenHeight() - paddle_height)
            {
                paddle_left_y += paddle_speed;
            }

            // right paddle
            if (IsKeyDown(KEY_UP) && paddle_right_y >= 0)
            {
                paddle_right_y -= paddle_speed;
            }
            else if (IsKeyDown(KEY_DOWN) && paddle_right_y <= GetScreenHeight() - paddle_height)
            {
                paddle_right_y += paddle_speed;
            }

            // move ball
            frames_counter ++;
            if (frames_counter > 60)
            {
                ball_x += ball_change_x;
                ball_y += ball_change_y;
            }

            if (ball_x <= ball_radius) 
            {
                frames_counter = 0;
                right_score ++;
                ball_change_x *= -1;
                ball_reset(&ball_x, &ball_y, ball_initial_x, ball_initial_y);
                paddle_reset(&paddle_left_y, paddle_initial_y);
                paddle_reset(&paddle_right_y, paddle_initial_y);
            }
            else if (ball_x >= GetScreenWidth() - ball_radius)
            {
                frames_counter = 0;
                left_score ++;
                ball_change_x *= -1;
                ball_reset(&ball_x, &ball_y, ball_initial_x, ball_initial_y);   
                paddle_reset(&paddle_left_y, paddle_initial_y);
                paddle_reset(&paddle_right_y, paddle_initial_y);
            }
            else if (ball_y <= 0 || ball_y >= GetScreenHeight() - ball_radius)
            {
                ball_change_y *= -1;
            }

            // paddle collision with ball
            if (CheckCollisionCircleRec((Vector2){ball_x, ball_y}, ball_radius, (Rectangle){paddle_left_x, paddle_left_y, paddle_width, paddle_height}))
            {
                    ball_change_x *= -1;
            }
            else if (CheckCollisionCircleRec((Vector2){ball_x, ball_y}, ball_radius, (Rectangle){paddle_right_x, paddle_right_y, paddle_width, paddle_height}))
            {
                    ball_change_x *= -1;
            }
        }
        else if (game_over)
        {
            DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), screenBackground);

            DrawText("GAME OVER", GetScreenWidth()/2, GetScreenHeight()/2 - 100, 30, GRAY);

            DrawText("Press 'ENTER' to continue", GetScreenWidth()/2, GetScreenHeight()/2, 20, GRAY);

            if (IsKeyPressed(KEY_ENTER))
            {
                // reset paddles
                paddle_left_x = paddle_left_initial_x;
                paddle_left_y = paddle_initial_y;

                paddle_right_x = paddle_right_initial_x;
                paddle_right_y = paddle_initial_y;

                // reset ball
                ball_reset(&ball_x, &ball_y, ball_initial_x, ball_initial_y);

                // reset score
                left_score = 0;
                right_score = 0;

                // reset game_over state
                game_over = false;
                
            }
        }

        BeginDrawing();

            ClearBackground(screenBackground);

            // draw scores
            DrawText(left_score_str, GetScreenWidth()/2 - 70, 10, 30, GRAY);
            DrawText(right_score_str, GetScreenWidth()/2 + 50, 10, 30, GRAY);

            // screen divider
            DrawLineEx((Vector2){(float)GetScreenWidth()/2, 0},
                       (Vector2){(float)GetScreenWidth()/2, GetScreenHeight()},
                       2,
                       GRAY);

            // draw paddle
            DrawRectangle(paddle_left_x, paddle_left_y, paddle_width, paddle_height, paddle_color);
            DrawRectangle(paddle_right_x, paddle_right_y, paddle_width, paddle_height, paddle_color);

            // draw ball
            DrawCircle(ball_x, ball_y, ball_radius, ball_color);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
