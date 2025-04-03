#include <stdio.h>
#include "raylib.h"
#include "raymath.h"
#include "utils.h"

#define SCORE_MAX 10

//*********************************
// BALL
//*********************************

typedef struct Ball
{
    float initial_x;
    float initial_y;
    float x;
    float y;
    float radius;
    float initial_speed;
    float speed;
    float speed_increment;
    Vector2 direction;
    Color color;
    bool show_text;
    bool active;
    float last_current_time;

} Ball;

void ball_init(Ball *ball)
{
    ball->initial_x = (float)GetScreenWidth() / 2;
    ball->initial_y = (float)GetScreenHeight() / 2;
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->radius = 10.0f;
    ball->initial_speed = 300.0f;
    ball->speed = ball->initial_speed;
    ball->speed_increment = 5.0f;
    ball->direction = (Vector2){1, 1};
    ball->color = RED;
    ball->active = false;
    ball->show_text = false;
    ball->last_current_time = 0.0f;
}

void ball_reset(Ball *ball)
{
    ball->x = ball->initial_x;
    ball->y = ball->initial_y;
    ball->speed = ball->initial_speed;
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

void ball_update(Ball *ball)
{
    // show ball activation instructions
    if (!ball->active)
    {
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

//*********************************
// Paddle
//*********************************

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

void paddle_init(Paddle *paddle, float x)
{
    paddle->width = 10.0f;
    paddle->height = 100.0f;
    paddle->initial_x = x;
    paddle->initial_y = (float)GetScreenHeight() / 2 - paddle->height / 2;
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

void paddle_update_player(Paddle *paddle)
{
    // get input and move paddle
    if (IsKeyDown(KEY_W) || IsKeyDown(KEY_UP))
    {
        paddle->y -= paddle->speed * GetFrameTime();
    }
    else if (IsKeyDown(KEY_S) || IsKeyDown(KEY_DOWN))
    {
        paddle->y += paddle->speed * GetFrameTime();
    }

    // paddle bounds
    paddle->y = max_float(0.0f, min_float(paddle->y, GetScreenHeight() - paddle->height));
}

void paddle_update_ai(Paddle *paddle, Ball *ball)
{
    // move paddle
    if (ball->y > paddle->y + paddle->height / 2)
    {
        paddle->y += paddle->speed * GetFrameTime();
    }
    else if (ball->y < paddle->y + paddle->height / 2)
    {
        paddle->y -= paddle->speed * GetFrameTime();
    }

    // paddle bounds
    paddle->y = max_float(0.0f, min_float(paddle->y, GetScreenHeight() - paddle->height));
}

//*********************************
// Game Manager
//*********************************

typedef struct Game
{
    int score_left;
    int score_right;
    char score_left_str[SCORE_MAX];
    char score_right_str[SCORE_MAX];

    Ball ball;
    Paddle player;
    Paddle ai;

} Game;

void game_init(Game *game)
{
    game->score_left = 0;
    game->score_right = 0;

    ball_init(&game->ball);
    paddle_init(&game->player, 10.0f);
    paddle_init(&game->ai, GetScreenWidth() - 10.0f - game->player.width);
}

void game_reset(Game *game)
{
    ball_reset(&game->ball);
    paddle_reset(&game->player);
    paddle_reset(&game->ai);
}

void game_draw(Game *game)
{
    // draw scores
    DrawText(game->score_left_str, 200, 20, 40, BLACK);
    DrawText(game->score_right_str, GetScreenWidth() - 200, 20, 40, BLACK);

    ball_draw(&game->ball);
    paddle_draw(&game->player);
    paddle_draw(&game->ai);
}

void game_update(Game *game)
{
    // convert scores to strings
    snprintf(game->score_left_str, SCORE_MAX, "%d", game->score_left);
    snprintf(game->score_right_str, SCORE_MAX, "%d", game->score_right);

    ball_update(&game->ball);
    paddle_update_player(&game->player);
    paddle_update_ai(&game->ai, &game->ball);

    // ball collision paddles
    if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                game->ball.radius,
                                (Rectangle){game->player.x,
                                            game->player.y,
                                            game->player.width,
                                            game->player.height}))
    {
        game->ball.direction.x *= -1;
        game->ball.speed += game->ball.speed_increment;
    }
    if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                                game->ball.radius,
                                (Rectangle){game->ai.x,
                                            game->ai.y,
                                            game->ai.width,
                                            game->ai.height}))
    {
        game->ball.direction.x *= -1;
        game->ball.speed += game->ball.speed_increment;
    }

    // update scores
    if (game->ball.x < game->ball.radius)
    {
        game->score_right += 1;
        game_reset(game);
    }
    else if (game->ball.x > GetScreenWidth() - game->ball.radius)
    {
        game->score_left += 1;
        game_reset(game);
    }
}

//*********************************
// MAIN
//*********************************

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Pong";
    const Color SCREEN_BACKGROUND = SKYBLUE;

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
