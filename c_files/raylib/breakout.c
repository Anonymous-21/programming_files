#include <stdio.h>
#include "raylib.h"
#include "raymath.h"
#include "utils.h"

#define ROWS 5
#define COLS 10
#define BLOCK_WIDTH 79
#define BLOCK_HEIGHT 30
#define GAP 2

#define LIVES_LENGTH 10

//*****************************************
// Bricks
//*****************************************

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

void bricks_init(Bricks *bricks)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            int x = j * (BLOCK_WIDTH + GAP);
            int y = i * (BLOCK_HEIGHT + GAP);

            bricks->list[i * COLS + j].pos = (Vector2){x, y};
            bricks->list[i * COLS + j].active = true;
            bricks->list[i * COLS + j].color = GRAY;
        }
    }
}

void bricks_draw(Bricks *bricks)
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

//*****************************************
// Paddle
//*****************************************

typedef struct Paddle
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float width;
    float height;
    float speed;
    Color color;

} Paddle;

void paddle_init(Paddle *paddle)
{
    paddle->width = 100.0f;
    paddle->height = 10.0f;
    paddle->initial_x = (float)GetScreenWidth() / 2 - paddle->width / 2;
    paddle->initial_y = GetScreenHeight() - paddle->height - 10.0f;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->speed = 300.0f;
    paddle->color = BLACK;
}

void paddle_reset(Paddle *paddle)
{
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
}

void paddle_draw(Paddle *paddle)
{
    DrawRectangleRec((Rectangle){paddle->x,
                                 paddle->y,
                                 paddle->width,
                                 paddle->height},
                     paddle->color);
}

void paddle_update(Paddle *paddle)
{
    // move paddle
    if (IsKeyDown(KEY_A) || IsKeyDown(KEY_LEFT))
    {
        paddle->x -= paddle->speed * GetFrameTime();
    }
    else if (IsKeyDown(KEY_D) || IsKeyDown(KEY_RIGHT))
    {
        paddle->x += paddle->speed * GetFrameTime();
    }

    // paddle bounds
    paddle->x = max_float(0.0f, min_float(paddle->x, GetScreenWidth() - paddle->width));
}

//*****************************************
// Ball
//*****************************************

typedef struct Ball
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float radius;
    float speed;
    Vector2 direction;
    Color color;
    bool active;
    bool show_text;
    float last_current_time;

} Ball;

void ball_init(Ball *ball, Paddle *paddle)
{
    ball->radius = 10.0f;
    ball->initial_x = paddle->x + paddle->width / 2;
    ball->initial_y = paddle->y - ball->radius * 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->direction = (Vector2){1, 1};
    ball->speed = 350.0f;
    ball->color = RED;
    ball->active = false;
    ball->show_text = false;
    ball->last_current_time = 0.0f;
}

void ball_reset(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->direction.x *= -1;
    ball->active = false;
    ball->last_current_time = 0.0f;
}

void ball_draw(Ball *ball)
{
    if (ball->show_text)
    {
        DrawText(
            "Press SPACE to begin",
            GetScreenWidth() / 2 - 150,
            GetScreenHeight() / 2 + 100,
            30,
            BLACK);
    }

    DrawCircleV((Vector2){ball->x, ball->y},
                ball->radius,
                ball->color);
}

void ball_update(Ball *ball, Paddle *paddle)
{
    // show ball activation instruction
    if (!ball->active)
    {
        // update ball position
        ball->x = paddle->x + paddle->width / 2;
        ball->y = paddle->y - ball->radius * 2;

        float current_time = GetTime();
        if (current_time - ball->last_current_time > 1)
        {
            ball->show_text = !ball->show_text;
            ball->last_current_time = current_time;
        }
    }

    // activate ball
    if (IsKeyPressed(KEY_SPACE))
    {
        ball->active = true;
        ball->show_text = false;
    }

    // move ball
    if (ball->active)
    {
        ball->x += ball->direction.x * ball->speed * GetFrameTime();
        ball->y += ball->direction.y * ball->speed * GetFrameTime();
    }

    // ball bounds
    if (ball->x < ball->radius || ball->x > GetScreenWidth() - ball->radius)
    {
        ball->direction.x *= -1;
    }
    else if (ball->y < ball->radius || ball->y > GetScreenHeight() - ball->radius)
    {
        ball->direction.y *= -1;
    }

    // normalize direction vector
    ball->direction = Vector2Normalize(ball->direction);
}

//*****************************************
// Game Manager
//*****************************************

typedef struct Game
{
    int lives;
    char lives_str[LIVES_LENGTH];
    bool game_over;
    bool game_won;

    Bricks bricks;
    Paddle paddle;
    Ball ball;

} Game;

void game_init(Game *game)
{
    game->lives = 5;
    game->game_over = false;
    game->game_won = false;

    bricks_init(&game->bricks);
    paddle_init(&game->paddle);
    ball_init(&game->ball, &game->paddle);
}

void game_reset(Game *game)
{
    paddle_reset(&game->paddle);
    ball_reset(&game->ball);
}

void game_draw(Game *game)
{
    // draw lives
    DrawText(game->lives_str, 20, GetScreenHeight() - 40, 40, GRAY);

    if (game->game_over)
    {
        DrawText(
            "GAME OVER",
            GetScreenWidth() / 2 - 100,
            GetScreenHeight() / 2,
            40,
            BLACK);
        DrawText(
            "Press ENTER to restart",
            GetScreenWidth() / 2 - 170,
            GetScreenHeight() / 2 + 100,
            30,
            BLACK);
    }
    if (game->game_won)
    {
        DrawText("GAME WON",
                 GetScreenWidth() / 2 - 100,
                 GetScreenHeight() / 2,
                 40,
                 BLACK);
        DrawText(
            "Press ENTER to restart",
            GetScreenWidth() / 2 - 170,
            GetScreenHeight() / 2 + 100,
            30,
            BLACK);
    }

    bricks_draw(&game->bricks);
    paddle_draw(&game->paddle);
    ball_draw(&game->ball);
}

void game_update(Game *game)
{
    // game lose condition 
    if (game->lives <= 0)
    {
        game->game_over = true;
    }

    // game win condition
    bool all_done = true;

    for (int i = 0; i < ROWS * COLS; i++)
    {
        if (game->bricks.list[i].active)
        {
            all_done = false;
            break;
        }
    }

    if (all_done)
    {
        game->game_won;
    }

    // game start
    if (!game->game_over && !game->game_won)
    {
        // convert lives to string
        snprintf(game->lives_str, LIVES_LENGTH, "%d", game->lives);

        paddle_update(&game->paddle);
        ball_update(&game->ball, &game->paddle);

        // ball collision paddle
        if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                    game->ball.radius,
                                    (Rectangle){game->paddle.x,
                                                game->paddle.y,
                                                game->paddle.width,
                                                game->paddle.height}))
        {
            game->ball.direction.y *= -1;
        }

        // ball collision bricks
        for (int i = 0; i < ROWS * COLS; i++)
        {
            if (game->bricks.list[i].active)
            {
                if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                            game->ball.radius,
                                            (Rectangle){game->bricks.list[i].pos.x,
                                                        game->bricks.list[i].pos.y,
                                                        BLOCK_WIDTH,
                                                        BLOCK_HEIGHT}))
                {
                    game->ball.direction.y *= -1;
                    game->bricks.list[i].active = false;
                }
            }
        }

        // update lives
        if (game->ball.y > GetScreenHeight() - game->ball.radius)
        {
            game->lives -= 1;
            game_reset(game);
        }
    }
    else
    {
        if (IsKeyPressed(KEY_ENTER))
        {
            game->lives = 5;
            game->game_over = false;
            game->game_won = false;

            bricks_init(&game->bricks);
            paddle_init(&game->paddle);
            ball_init(&game->ball, &game->paddle);
        }
    }
}

//*****************************************
// Main
//*****************************************

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Breakout";
    const Color SCREEN_BACKGROUND = RAYWHITE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    Game game;

    game_init(&game);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        game_draw(&game);
        game_update(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
