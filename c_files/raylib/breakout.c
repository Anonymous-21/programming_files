#include "raylib.h"
#include <stdio.h>

#define LIVES_STR_LENGTH 5
#define ROWS 5
#define COLS 10
#define BRICK_WIDTH 79
#define BRICK_HEIGHT 30
#define BRICK_GAP 2

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

void initPaddle(Paddle *paddle)
{
    paddle->width = 100;
    paddle->height = 10;
    paddle->initial_x = (float)GetScreenWidth() / 2 - paddle->width / 2;
    paddle->initial_y = GetScreenHeight() - 40;
    paddle->x = paddle->initial_x;
    paddle->y = paddle->initial_y;
    paddle->color = BLACK;
    paddle->speed = 5;
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
    if (IsKeyDown(KEY_LEFT) && paddle->x >= 0)
    {
        paddle->x -= paddle->speed;
    }
    else if (IsKeyDown(KEY_RIGHT) && paddle->x <= GetScreenWidth() - paddle->width)
    {
        paddle->x += paddle->speed;
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
    bool is_active;

} Ball;

void initBall(Ball *ball)
{
    ball->initial_x = (float)GetScreenWidth() / 2;
    ball->initial_y = (float)GetScreenHeight() / 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->radius = 10;
    ball->color = RED;
    ball->initial_speed_x = 4;
    ball->initial_speed_y = 5;
    ball->speed_x = ball->initial_speed_x;
    ball->speed_y = ball->initial_speed_y;
    ball->speed_increment = 0.005;
    ball->is_active = false;
}

void resetBall(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed_x *= -1;
    ball->is_active = false;
}

void drawBall(Ball *ball)
{
    DrawCircleV((Vector2){ball->x, ball->y},
                ball->radius,
                ball->color);
}

void updateBall(Ball *ball)
{
    if (IsKeyPressed(KEY_SPACE))
    {
        ball->is_active = true;
    }

    if (ball->is_active)
    {
        ball->x += ball->speed_x;
        ball->y += ball->speed_y;
    }

    if (ball->x <= ball->radius || ball->x >= GetScreenWidth() - ball->radius)
    {
        ball->speed_x *= -1;
    }
    if (ball->y <= ball->radius)
    {
        ball->speed_y *= -1;
    }
}

/*
    BRICKS
*/
typedef struct Brick
{
    Vector2 position;
    bool is_active;
    Color color;

} Brick;

typedef struct Bricks
{
    Brick list[ROWS * COLS];

} Bricks;

void initBricks(Bricks *bricks)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            int x = j * (BRICK_WIDTH + BRICK_GAP);
            int y = i * (BRICK_HEIGHT + BRICK_GAP);

            bricks->list[i * COLS + j].position = (Vector2){x, y};
            bricks->list[i * COLS + j].is_active = true;
            bricks->list[i * COLS + j].color = GRAY;
        }
    }
}

void drawBricks(Bricks *bricks)
{
    for (int i = 0; i < (ROWS * COLS); i++)
    {
        if (bricks->list[i].is_active)
        {
            DrawRectangleRec((Rectangle){bricks->list[i].position.x,
                                         bricks->list[i].position.y,
                                         BRICK_WIDTH,
                                         BRICK_HEIGHT},
                             bricks->list[i].color);
        }
    }
}

/*
    GAME
*/
typedef struct Game
{
    int lives;
    char lives_str[LIVES_STR_LENGTH];
    bool game_over;
    bool game_won;

    Paddle paddle;
    Ball ball;
    Bricks bricks;

} Game;

void initGame(Game *game)
{
    game->lives = 5;
    game->game_over = false;
    game->game_won = false;

    initPaddle(&game->paddle);
    initBall(&game->ball);
    initBricks(&game->bricks);
}

void resetGame(Game *game)
{
    resetPaddle(&game->paddle);
    resetBall(&game->ball);
}

void drawGame(Game *game)
{
    // draw lives
    DrawText(game->lives_str,
             20,
             GetScreenHeight() - 40,
             40,
             BLACK);

    drawPaddle(&game->paddle);
    drawBall(&game->ball);
    drawBricks(&game->bricks);
}

void updateGame(Game *game)
{
    if (!game->game_over && !game->game_won)
    {
        // game over condition
        if (game->lives <= 0)
        {
            game->game_over = true;
        }

        // game won condition
        bool all_brick_inactive = true;
        for (int i = 0; i < (ROWS * COLS); i++)
        {
            if (game->bricks.list[i].is_active)
            {
                all_brick_inactive = false;
                break;
            }
        }

        if (all_brick_inactive)
        {
            game->game_won = true;
        }

        // convert lives to string
        snprintf(game->lives_str, LIVES_STR_LENGTH, "%d\n", game->lives);

        updatePaddle(&game->paddle);
        updateBall(&game->ball);

        // ball collision paddle
        if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                    game->ball.radius,
                                    (Rectangle){game->paddle.x,
                                                game->paddle.y,
                                                game->paddle.width,
                                                game->paddle.height}))
        {
            game->ball.speed_y *= -1;
        }

        // update lives
        if (game->ball.y > GetScreenHeight())
        {
            game->lives--;
            resetGame(game);
        }

        // ball collision bricks
        for (int i = 0; i < (ROWS * COLS); i++)
        {
            if (game->bricks.list[i].is_active)
            {
                if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                            game->ball.radius,
                                            (Rectangle){game->bricks.list[i].position.x,
                                                        game->bricks.list[i].position.y,
                                                        BRICK_WIDTH,
                                                        BRICK_HEIGHT}))
                {
                    game->bricks.list[i].is_active = false;
                    game->ball.speed_y *= -1;
                }
            }
        }
    }
    else
    {
        if (IsKeyPressed(KEY_ENTER))
        {
            game->lives = 5;
            game->game_over = false;
            game->game_won = false;

            initPaddle(&game->paddle);
            initBall(&game->ball);
            initBricks(&game->bricks);
        }
    }
}

/*
    RAYLIB WINDOW
*/
int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Breakout";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Game game;

    initGame(&game);

    while (!WindowShouldClose())
    {
        updateGame(&game);

        BeginDrawing();
        ClearBackground(screenBackground);

        drawGame(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}