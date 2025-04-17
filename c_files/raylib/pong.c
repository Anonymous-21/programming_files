#include "raylib.h"
#include "raymath.h"
#include "utils.h"

//+++++++++++++++++++++++++++++++++++++++++++
// BALL
//+++++++++++++++++++++++++++++++++++++++++++

typedef struct Ball {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float radius;
  float speed;
  Vector2 direction;
  Color color;

} Ball;

void ball_init(Ball *ball) {
  ball->initial_x = GetScreenWidth() * 0.5f;
  ball->initial_y = GetScreenHeight() * 0.5f;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->radius = 10.0f;
  ball->speed = 400.0f;
  ball->direction = (Vector2){1, 1};
  ball->color = RED;
}

void ball_reset(Ball *ball) {
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->direction.x *= -1;
}

void ball_draw(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void ball_update(Ball *ball) {
  // move ball
  ball->x += ball->direction.x * ball->speed * GetFrameTime();
  ball->y += ball->direction.y * ball->speed * GetFrameTime();

  // ball bounds
  if (ball->y < ball->radius || ball->y > GetScreenHeight() - ball->radius) {
    ball->direction.y *= -1;
  }

  // normalize direction vector
  if (ball->direction.x != 0 && ball->direction.y != 0) {
    ball->direction = Vector2Normalize(ball->direction);
  }
}

//+++++++++++++++++++++++++++++++++++++++++++
// PADDLE
//+++++++++++++++++++++++++++++++++++++++++++

typedef struct Paddle {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float width;
  float height;
  float speed;
  Color color;

} Paddle;

void paddle_init(Paddle *paddle, float x) {
  paddle->width = 10.0f;
  paddle->height = 100.0f;
  paddle->initial_x = x;
  paddle->initial_y = GetScreenHeight() * 0.5f - paddle->height / 2;
  paddle->x = paddle->initial_x;
  paddle->y = paddle->initial_y;
  paddle->speed = 300.0f;
  paddle->color = BLACK;
}

void paddle_reset(Paddle *paddle) {
  paddle->x = paddle->initial_x;
  paddle->y = paddle->initial_y;
}

void paddle_draw(Paddle *paddle) {
  DrawRectangleRec(
      (Rectangle){paddle->x, paddle->y, paddle->width, paddle->height},
      paddle->color);
}

void paddle_update_player(Paddle *paddle) {
  // move paddle
  if (IsKeyDown(KEY_UP)) {
    paddle->y -= paddle->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_DOWN)) {
    paddle->y += paddle->speed * GetFrameTime();
  }

  // paddle bounds
  paddle->y =
      max_float(0.0f, min_float(paddle->y, GetScreenHeight() - paddle->height));
}

void paddle_update_ai(Paddle *paddle, Ball *ball) {
  // move paddle
  if (ball->y < paddle->y + paddle->height / 2) {
    paddle->y -= paddle->speed * GetFrameTime();
  }
  if (ball->y > paddle->y + paddle->height / 2) {
    paddle->y += paddle->speed * GetFrameTime();
  }

  // paddle bounds
  paddle->y =
      max_float(0.0f, min_float(paddle->y, GetScreenHeight() - paddle->height));
}
//+++++++++++++++++++++++++++++++++++++++++++
// GAME
//+++++++++++++++++++++++++++++++++++++++++++

typedef struct Game {
  int score_left;
  int score_right;

  Ball ball;
  Paddle player;
  Paddle ai;

} Game;

void game_init(Game *game) {
  game->score_left = 0;
  game->score_right = 0;

  ball_init(&game->ball);
  paddle_init(&game->player, 10.0f);
  paddle_init(&game->ai, GetScreenWidth() - game->player.width - 10.0f);
}

void game_reset(Game *game) {
  ball_reset(&game->ball);
  paddle_reset(&game->player);
  paddle_reset(&game->ai);
}

void game_draw(Game *game) {
  // draw scores
  DrawText(TextFormat("%d", game->score_left), 200, 30, 40, BLACK);
  DrawText(TextFormat("%d", game->score_right), GetScreenWidth() - 200, 30, 40,
           BLACK);

  // draw rest
  ball_draw(&game->ball);
  paddle_draw(&game->player);
  paddle_draw(&game->ai);
}

void game_update(Game *game) {
  ball_update(&game->ball);
  paddle_update_player(&game->player);
  paddle_update_ai(&game->ai, &game->ball);

  // ball collision paddle
  if (CheckCollisionCircleRec(
          (Vector2){game->ball.x, game->ball.y}, game->ball.radius,
          (Rectangle){game->player.x, game->player.y, game->player.width,
                      game->player.height})) {
    game->ball.direction.x *= -1;
  }
  if (CheckCollisionCircleRec((Vector2){game->ball.x, game->ball.y},
                              game->ball.radius,
                              (Rectangle){game->ai.x, game->ai.y,
                                          game->ai.width, game->ai.height})) {
    game->ball.direction.x *= -1;
  }

  // update scores
  if (game->ball.x < game->ball.radius) {
    game->score_right += 1;
    game_reset(game);
  }
  if (game->ball.x > GetScreenWidth()) {
    game->score_left += 1;
    game_reset(game);
  }
}

//+++++++++++++++++++++++++++++++++++++++++++
// MAIN
//+++++++++++++++++++++++++++++++++++++++++++

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Pong";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Game game;
  game_init(&game);

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    game_draw(&game);
    game_update(&game);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
