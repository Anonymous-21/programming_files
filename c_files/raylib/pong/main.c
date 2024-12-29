#include <stdio.h>
#include "raylib.h"

#include "ball.h"
#include "paddle.h"

#define SCORE_STR_LENGTH 10

typedef struct Game
{
    int score_left;
    int score_right;
    char score_str_left[SCORE_STR_LENGTH];
    char score_str_right[SCORE_STR_LENGTH];

    Paddle paddle_left;
    Paddle paddle_right;
    Ball ball;

} Game;

void game_initialize(Game *game)
{
    game->score_left = 0;
    game->score_right = 0;

    paddle_initialize(&game->paddle_left, 10);
    paddle_initialize(&game->paddle_right,
                      GetScreenWidth() - game->paddle_left.width - 10);
    ball_initialize(&game->ball);
}

void game_reset(Game *game)
{
    paddle_reset(&game->paddle_left);
    paddle_reset(&game->paddle_right);
    ball_reset(&game->ball);
}

void game_draw(Game *game)
{
    // draw scores
    DrawText(game->score_str_left, 200, 20, 40, BLACK);
    DrawText(game->score_str_right, GetScreenWidth() - 220, 20, 40, BLACK);

    paddle_draw(&game->paddle_left);
    paddle_draw(&game->paddle_right);
    ball_draw(&game->ball);
}

void game_update(Game *game)
{
    // convert scores to string
    snprintf(game->score_str_left, SCORE_STR_LENGTH, "%d\n", game->score_left);
    snprintf(game->score_str_right, SCORE_STR_LENGTH, "%d\n", game->score_right);

    paddle_left_update(&game->paddle_left);
    paddle_right_update(&game->paddle_right, &game->ball);
    ball_update(&game->ball);

    // ball horizontal collision walls
    if (game->ball.x < 0)
    {
        game->score_left++;
        game_reset(game);
    }
    else if (game->ball.x > GetScreenWidth())
    {
        game->score_right++;
        game_reset(game);
    }

    // ball collision paddle
    if (CheckCollisionCircleRec(
            (Vector2){game->ball.x, game->ball.y},
            game->ball.radius,
            (Rectangle){game->paddle_left.x,
                        game->paddle_left.y,
                        game->paddle_left.width,
                        game->paddle_left.height}))
    {
        game->ball.speed_x *= -1;
    }
    else if (CheckCollisionCircleRec(
                 (Vector2){game->ball.x, game->ball.y},
                 game->ball.radius,
                 (Rectangle){game->paddle_right.x,
                             game->paddle_right.y,
                             game->paddle_right.width,
                             game->paddle_right.height}))
    {
        game->ball.speed_x *= -1;
    }
}

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

    game_initialize(&game);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(screenBackground);

        game_draw(&game);
        game_update(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}