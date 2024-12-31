#include "raylib.h"
#include <stdio.h>

#define LIVES_STR_LENGTH 5

#define ROWS 5
#define COLS 10
#define BLOCK_WIDTH 79
#define BLOCK_HEIGHT 30
#define BLOCK_GAP 2

// ************************************
// BRICKS
// ************************************

typedef struct Brick
{
    Vector2 pos;
    Color color;
    bool active;

} Brick;

typedef struct Bricks
{
    Brick list[ROWS * COLS];

} Bricks;

void init_bricks(Bricks *bricks)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            int x = j * (BLOCK_WIDTH + BLOCK_GAP);
            int y = i * (BLOCK_HEIGHT + BLOCK_GAP);

            bricks->list[i * COLS + j].pos = (Vector2){x, y};
            bricks->list[i * COLS + j].color = GRAY;
            bricks->list[i * COLS + j].active = true;
        }
    }
}

void draw_bricks(Bricks *bricks)
{
    for (int i = 0; i < ROWS * COLS; i++)
    {
        if (bricks->list[i].active)
        {
            DrawRectangleRec((Rectangle){bricks->list[i].pos.x,
                                         bricks->list[i].pos.y,
                                         BLOCK_WIDTH,
                                         BLOCK_HEIGHT},
                             bricks->list[i].color);
        }
    }
}

// ************************************
// PADDLE
// ************************************

typedef struct Paddle
{
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;

} Paddle;

void init_paddle(Paddle *paddle)
{
    paddle->width = 100.0f;
    paddle->height = 10.0f;
    paddle->x = (float)GetScreenWidth() / 2 - paddle->width / 2;
    paddle->y = GetScreenHeight() - 20;
    paddle->color = BLACK;
    paddle->speed = 5.0f;
}

void draw_paddle(Paddle *paddle)
{
    DrawRectangleRec((Rectangle){paddle->x,
                                 paddle->y,
                                 paddle->width,
                                 paddle->height},
                     paddle->color);
}

void update_paddle(Paddle *paddle)
{
    if (IsKeyDown(KEY_LEFT) && paddle->x >= 0)
    {
        paddle->x -= paddle->speed;
    }
    else if (IsKeyDown(KEY_RIGHT) && paddle->x <= GetScreenWidth() - paddle->width)
    {
        paddle->x += paddle->speed;
    }
}

// ************************************
// BALL
// ************************************

typedef struct Ball
{
    float x;
    float y;
    float radius;
    Color color;
    float speed_x;
    float speed_y;
    float speed_increment;
    float active;

} Ball;

void init_ball(Ball *ball)
{
    ball->x = (float)GetScreenWidth() / 2;
    ball->y = (float)GetScreenHeight() / 2;
    ball->radius = 10.0f;
    ball->color = RED;
    ball->speed_x = 4.0f;
    ball->speed_y = 4.0f;
    ball->speed_increment = 0.0005f;
    ball->active = false;
}

void draw_ball(Ball *ball)
{
    DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void update_ball(Ball *ball)
{
    if (IsKeyDown(KEY_SPACE))
    {
        ball->active = true;
    }

    if (ball->active)
    {
        ball->x += ball->speed_x;
        ball->y += ball->speed_y;

        // increment speed
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
            ball->speed_y += ball->speed_increment;
        }
        else if (ball->speed_y < 0)
        {
            ball->speed_y -= ball->speed_increment;
        }
    }

    // ball collision walls
    if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius)
    {
        ball->speed_x *= -1;
    }
    if (ball->y <= ball->radius)
    {
        ball->speed_y *= -1;
    }
}

// ************************************
// MAIN LOOP
// ************************************

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Breakout";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    int lives = 5;
    char lives_str[LIVES_STR_LENGTH];
    bool game_over = false;
    bool game_won = false;

    Bricks bricks;
    Paddle paddle;
    Ball ball;

    init_bricks(&bricks);
    init_paddle(&paddle);
    init_ball(&ball);

    while (!WindowShouldClose())
    {
        if (!game_over && !game_won)
        {
            // game over condition
            if (lives <= 0)
            {
                game_over = true;
            }

            // game won condition
            bool all_bricks_destroyed = true;
            for (int i = 0; i < ROWS * COLS; i++)
            {
                if (bricks.list[i].active)
                {
                    all_bricks_destroyed = false;
                    break;
                }
            }
            if (all_bricks_destroyed)
            {
                game_won = true;
            }

            // convert lives to string
            snprintf(lives_str, LIVES_STR_LENGTH, "%d\n", lives);

            update_paddle(&paddle);
            update_ball(&ball);

            // update lives
            if (ball.y > GetScreenHeight())
            {
                lives--;
                init_paddle(&paddle);
                init_ball(&ball);
            }

            // ball collision paddle
            if (CheckCollisionCircleRec((Vector2){ball.x, ball.y},
                                        ball.radius,
                                        (Rectangle){paddle.x,
                                                    paddle.y,
                                                    paddle.width,
                                                    paddle.height}))
            {
                ball.speed_y *= -1;
            }

            // ball collision bricks
            for (int i = 0; i < ROWS * COLS; i++)
            {
                if (bricks.list[i].active)
                {
                    if (CheckCollisionCircleRec((Vector2){ball.x, ball.y},
                                                ball.radius,
                                                (Rectangle){bricks.list[i].pos.x,
                                                            bricks.list[i].pos.y,
                                                            BLOCK_WIDTH,
                                                            BLOCK_HEIGHT}))
                    {
                        bricks.list[i].active = false;
                        ball.speed_y *= -1;
                    }
                }
            }
        }
        else
        {
            if (IsKeyPressed(KEY_ENTER))
            {
                lives = 5;
                game_over = false;
                game_won = false;
                init_bricks(&bricks);
                init_paddle(&paddle);
                init_ball(&ball);
            }
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        // game over and game won screens
        if (game_over)
        {
            DrawText("GAME OVER", GetScreenWidth() / 2 - 100, GetScreenHeight() / 2 + 100, 30, BLACK);
        }
        if (game_won)
        {
            DrawText("YOU WIN", GetScreenWidth() / 2 - 80, GetScreenHeight() / 2 + 100, 30, BLACK);
        }

        // draw lives
        DrawText(lives_str, 20, GetScreenHeight() - 40, 40, BLACK);

        draw_bricks(&bricks);
        draw_paddle(&paddle);
        draw_ball(&ball);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}