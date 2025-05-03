#include "raylib.h"
#include "raymath.h"
#include <stdbool.h>

#define ROWS 5
#define COLS 10
#define BRICK_WIDTH 79
#define BRICK_HEIGHT 30
#define BRICK_GAP 2

// BRICKS

typedef struct Brick
{
  Rectangle rect;
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
      int x = j * (BRICK_WIDTH + BRICK_GAP);
      int y = i * (BRICK_HEIGHT + BRICK_GAP);

      Brick brick = {
          .rect = (Rectangle){x, y, BRICK_WIDTH, BRICK_HEIGHT},
          .active = true,
          .color = GRAY,
      };

      bricks->list[i * COLS + j] = brick;
    }
  }
}

void bricks_draw(Bricks *bricks)
{
  for (int i = 0; i < ROWS * COLS; i++)
  {
    if (bricks->list[i].active)
    {
      DrawRectangleRec(bricks->list[i].rect, bricks->list[i].color);
    }
  }
}

// PADDLE

typedef struct Paddle
{
  Rectangle initial_rect;
  Rectangle rect;
  float speed;
  Color color;

} Paddle;

void paddle_init(Paddle *paddle)
{
  float width = 100.0f;
  float height = 10.0f;
  paddle->initial_rect =
      (Rectangle){GetScreenWidth() * 0.5f - width / 2,
                  GetScreenHeight() - height - 10.0f, width, height};
  paddle->rect = paddle->initial_rect;
  paddle->speed = 300.0f;
  paddle->color = BLACK;
}

void paddle_reset(Paddle *paddle) { paddle->rect = paddle->initial_rect; }

void paddle_draw(Paddle *paddle)
{
  DrawRectangleRec(paddle->rect, paddle->color);
}

void paddle_update(Paddle *paddle)
{
  // move paddle
  if (IsKeyDown(KEY_LEFT))
  {
    paddle->rect.x -= paddle->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_RIGHT))
  {
    paddle->rect.x += paddle->speed * GetFrameTime();
  }

  // paddle bounds
  paddle->rect.x =
      Clamp(paddle->rect.x, 0, GetScreenWidth() - paddle->rect.width);
}

// BALL

typedef struct Ball
{
  Vector2 initial_pos;
  Vector2 pos;
  float radius;
  float speed;
  Vector2 direction;
  Color color;
  bool active;

} Ball;

void ball_init(Ball *ball, Paddle *paddle)
{
  ball->radius = 10.0f;
  ball->initial_pos = (Vector2){paddle->rect.x + paddle->rect.width / 2,
                                paddle->rect.y - ball->radius * 2};
  ball->pos = ball->initial_pos;
  ball->speed = 400.0f;
  ball->direction = (Vector2){1, 1};
  ball->color = RED;
  ball->active = false;
}

void ball_reset(Ball *ball)
{
  ball->pos = ball->initial_pos;
  ball->direction.x *= -1;
  ball->active = false;
}

void ball_draw(Ball *ball)
{
  DrawCircleV((Vector2){ball->pos.x, ball->pos.y}, ball->radius, ball->color);
}

void ball_update(Ball *ball, Paddle *paddle)
{
  // update ball position
  if (!ball->active)
  {
    ball->pos = (Vector2){paddle->rect.x + paddle->rect.width / 2,
                          paddle->rect.y - ball->radius * 2};
  }

  // activate ball
  if (IsKeyPressed(KEY_SPACE))
  {
    ball->active = !ball->active;
  }

  // move ball
  if (ball->active)
  {
    ball->pos.x += ball->direction.x * ball->speed * GetFrameTime();
    ball->pos.y += ball->direction.y * ball->speed * GetFrameTime();
  }

  // ball bounds
  if (ball->pos.x < ball->radius ||
      ball->pos.x > GetScreenWidth() - ball->radius)
  {
    ball->direction.x *= -1;
  }
  if (ball->pos.y < ball->radius)
  {
    ball->direction.y *= -1;
  }

  // normalize direction vector
  if (ball->direction.x != 0 && ball->direction.y != 0)
  {
    ball->direction = Vector2Normalize(ball->direction);
  }
}

// GAME OVER

typedef struct Game
{
  int lives;
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
  if (!game->game_over && !game->game_won)
  { // draw lives
    DrawText(TextFormat("%d", game->lives), 20, GetScreenHeight() - 50, 40,
             BLACK);

    bricks_draw(&game->bricks);
    paddle_draw(&game->paddle);
    ball_draw(&game->ball);
  }

  if (game->game_over)
  {
    char text1[] = "GAME OVER";
    float font_size1 = 40;
    float text_width1 = MeasureText(text1, font_size1);
    char text2[] = "press ENTER to restart";
    float font_size2 = 30;
    float text_width2 = MeasureText(text2, font_size2);

    DrawText(text1, GetScreenWidth() * 0.5f - text_width1 / 2,
             GetScreenHeight() * 0.5f - font_size1 / 2, font_size1, BLACK);
    DrawText(text2, GetScreenWidth() * 0.5f - text_width2 / 2,
             GetScreenHeight() * 0.5f - font_size2 / 2 + 100, font_size2,
             BLACK);
  }
  if (game->game_won)
  {
    char text1[] = "YOU WIN";
    float font_size1 = 40;
    float text_width1 = MeasureText(text1, font_size1);
    char text2[] = "press ENTER to restart";
    float font_size2 = 30;
    float text_width2 = MeasureText(text2, font_size2);

    DrawText(text1, GetScreenWidth() * 0.5f - text_width1 / 2,
             GetScreenHeight() * 0.5f - font_size1 / 2, font_size1, BLACK);
    DrawText(text2, GetScreenWidth() * 0.5f - text_width2 / 2,
             GetScreenHeight() * 0.5f - font_size2 / 2 + 100, font_size2,
             BLACK);
  }
}

void game_update(Game *game)
{
  if (game->lives <= 0)
  {
    game->game_over = true;
  }

  // game win condition
  bool remaining;
  for (int i = 0; i < ROWS * COLS; i++)
  {
    remaining = false;

    if (game->bricks.list[i].active)
    {
      remaining = true;
      break;
    }
  }

  if (!remaining)
  {
    game->game_won = true;
  }

  if (!game->game_over && !game->game_won)
  {
    paddle_update(&game->paddle);
    ball_update(&game->ball, &game->paddle);

    // ball collision paddle
    if (CheckCollisionCircleRec(game->ball.pos, game->ball.radius,
                                game->paddle.rect))
    {
      game->ball.direction.y *= -1;
    }

    // ball collision bricks
    for (int i = 0; i < ROWS * COLS; i++)
    {
      if (game->bricks.list[i].active)
      {
        if (CheckCollisionCircleRec(game->ball.pos, game->ball.radius,
                                    game->bricks.list[i].rect))
        {
          game->bricks.list[i].active = false;
          game->ball.direction.y *= -1;
        }
      }
    }

    // update lives
    if (game->ball.pos.y > GetScreenHeight() - game->ball.radius)
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

// MAIN

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

    game_update(&game);
    game_draw(&game);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
