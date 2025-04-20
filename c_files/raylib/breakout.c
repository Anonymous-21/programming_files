#include "raylib.h"
#include "raymath.h"
#include "utils.h"
#include <stdbool.h>

#define ROWS 5
#define COLS 10
#define BRICK_WIDTH 79
#define BRICK_HEIGHT 30
#define BRICK_GAP 2

//+++++++++++++++++++++++++++++++
// BRICKS
//+++++++++++++++++++++++++++++++

typedef struct Brick {
  int x;
  int y;
  int width;
  int height;
  Color color;
  bool active;

} Brick;

// bricks list
Brick bricks[ROWS * COLS];

void bricks_init() {

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      int x = j * (BRICK_WIDTH + BRICK_GAP);
      int y = i * (BRICK_HEIGHT + BRICK_GAP);

      Brick brick = {
          .x = x,
          .y = y,
          .width = BRICK_WIDTH,
          .height = BRICK_HEIGHT,
          .active = true,
          .color = GRAY,
      };

      bricks[i * COLS + j] = brick;
    }
  }
}

void bricks_draw() {
  for (int i = 0; i < ROWS * COLS; i++) {
    if (bricks[i].active) {
      DrawRectangleRec((Rectangle){bricks[i].x, bricks[i].y, bricks[i].width,
                                   bricks[i].height},
                       bricks[i].color);
    }
  }
}

//+++++++++++++++++++++++++++++++
// PADDLE
//+++++++++++++++++++++++++++++++

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

void paddle_init(Paddle *paddle) {
  paddle->width = 100.0f;
  paddle->height = 10.0f;
  paddle->initial_x = (float)(GetScreenWidth()) / 2 - paddle->width / 2;
  paddle->initial_y = GetScreenHeight() - paddle->height - 10;
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

void paddle_update(Paddle *paddle) {
  // move paddle
  if (IsKeyDown(KEY_RIGHT)) {
    paddle->x += paddle->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_LEFT)) {
    paddle->x -= paddle->speed * GetFrameTime();
  }

  // paddle bounds
  paddle->x =
      max_float(0.0f, min_float(paddle->x, GetScreenWidth() - paddle->width));
}

//+++++++++++++++++++++++++++++++
// BALL
//+++++++++++++++++++++++++++++++

typedef struct Ball {
  float initial_x;
  float initial_y;
  float x;
  float y;
  float radius;
  float speed;
  Vector2 direction;
  Color color;
  bool active;

} Ball;

void ball_init(Ball *ball) {
  ball->radius = 10.0f;
  ball->initial_x = GetScreenWidth() * 0.5f;
  ball->initial_y = GetScreenHeight() * 0.5f;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->speed = 350.0f;
  ball->direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1;
  ball->direction.y = 1;
  ball->color = RED;
  ball->active = false;
}

void ball_reset(Ball *ball) {
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1;
  ball->active = false;
}

void ball_draw(Ball *ball) {
  DrawCircleV((Vector2){ball->x, ball->y}, ball->radius, ball->color);
}

void ball_update(Ball *ball) {
  // activate ball
  if (IsKeyPressed(KEY_SPACE)) {
    ball->active = !ball->active;
  }

  // move ball
  if (ball->active) {
    ball->x += ball->direction.x * ball->speed * GetFrameTime();
    ball->y += ball->direction.y * ball->speed * GetFrameTime();
  }

  // ball bounds
  if (ball->x < ball->radius || ball->x > GetScreenWidth() - ball->radius) {
    ball->direction.x *= -1;
  }
  if (ball->y < ball->radius) {
    ball->direction.y *= -1;
  }

  // normalize direction vector
  if (ball->direction.x != 0 && ball->direction.y != 0) {
    ball->direction = Vector2Normalize(ball->direction);
  }
}

//+++++++++++++++++++++++++++++++
// GAME
//+++++++++++++++++++++++++++++++

typedef struct Game {
  int lives;
  bool game_over;
  bool game_won;

  Paddle paddle;
  Ball ball;

} Game;

void game_init(Game *game) {
  game->lives = 5;
  game->game_over = false;
  game->game_won = false;

  bricks_init();
  paddle_init(&game->paddle);
  ball_init(&game->ball);
}

void game_reset(Game *game) {
  paddle_reset(&game->paddle);
  ball_reset(&game->ball);
}

void game_draw(Game *game) {

  if (!game->game_over && !game->game_won) { // draw lives
    DrawText(TextFormat("%d", game->lives), 30, GetScreenHeight() - 50, 40,
             BLACK);

    bricks_draw();
    paddle_draw(&game->paddle);
    ball_draw(&game->ball);
  }

  if (game->game_over) {
    DrawText("GAME OVER", GetScreenWidth() * 0.5f - 100,
             GetScreenHeight() * 0.5f, 40, BLACK);
    DrawText("press [enter] to restart", GetScreenWidth() * 0.5f - 150,
             GetScreenHeight() * 0.5f + 100, 30, BLACK);
  }

  if (game->game_won) {
    DrawText("YOU WIN", GetScreenWidth() * 0.5f - 100, GetScreenHeight() * 0.5f,
             40, BLACK);
    DrawText("press [enter] to restart", GetScreenWidth() * 0.5f - 150,
             GetScreenHeight() * 0.5f + 100, 30, BLACK);
  }
}

void game_update(Game *game) {
  // game over condition
  if (game->lives <= 0) {
    game->game_over = true;
  }

  // game won condition
  bool all_bricks_inactive = true;
  for (int i = 0; i < ROWS * COLS; i++) {
    if (bricks[i].active) {
      all_bricks_inactive = false;
      break;
    }
  }

  if (all_bricks_inactive) {
    game->game_won = true;
  }

  // game start
  if (!game->game_over) {
    paddle_update(&game->paddle);
    ball_update(&game->ball);

    // ball collision paddle
    if (CheckCollisionCircleRec(
            (Vector2){game->ball.x, game->ball.y}, game->ball.radius,
            (Rectangle){game->paddle.x, game->paddle.y, game->paddle.width,
                        game->paddle.height})) {
      game->ball.direction.y *= -1;
    }

    // update lives
    if (game->ball.y > GetScreenHeight()) {
      game->lives -= 1;
      game_reset(game);
    }

    // ball collision bricks
    for (int i = 0; i < ROWS * COLS; i++) {
      if (bricks[i].active) {
        if (CheckCollisionCircleRec(
                (Vector2){game->ball.x, game->ball.y}, game->ball.radius,
                (Rectangle){bricks[i].x, bricks[i].y, bricks[i].width,
                            bricks[i].height})) {
          game->ball.direction.y *= -1;
          bricks[i].active = false;
        }
      }
    }
  } else {
    if (IsKeyPressed(KEY_ENTER)) {
      game->lives = 5;
      game->game_over = false;
      game->game_won = false;

      bricks_init();
      paddle_init(&game->paddle);
      ball_init(&game->ball);
    }
  }
}

//+++++++++++++++++++++++++++++++
// MAIN
//+++++++++++++++++++++++++++++++

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Breakout";
  const Color SCREEN_BACKGROUND = RAYWHITE;

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
