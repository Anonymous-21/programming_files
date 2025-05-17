#include <raylib.h>
#include <raymath.h>
#include <stdbool.h>

#define ROWS 5
#define COLS 10
#define BRICK_WIDTH 79
#define BRICK_HEIGHT 30
#define BRICK_GAP 2

// BRICK

typedef struct Brick
{
  float x;
  float y;
  float width;
  float height;
  Color color;
  bool is_active;

} Brick;

void
brick_init(Brick* brick, float x, float y)
{
  brick->x = x;
  brick->y = y;
  brick->width = BRICK_WIDTH;
  brick->height = BRICK_HEIGHT;
  brick->color = GRAY;
  brick->is_active = true;
}

void
brick_draw(Brick* brick)
{
  if (brick->is_active) {
    DrawRectangleRec(
      (Rectangle){ brick->x, brick->y, brick->width, brick->height },
      brick->color);
  }
}

// PADDLE

typedef struct Paddle
{
  float initial_x;
  float intiial_y;
  float x;
  float y;
  float width;
  float height;
  float speed;
  Color color;

} Paddle;

void
paddle_init(Paddle* paddle)
{
  paddle->width = 100.0f;
  paddle->height = 10.0f;
  paddle->initial_x = GetScreenWidth() * 0.5f - paddle->width / 2;
  paddle->intiial_y = GetScreenHeight() - paddle->height - 10.0f;
  paddle->x = paddle->initial_x;
  paddle->y = paddle->intiial_y;
  paddle->speed = 300.0f;
  paddle->color = BLACK;
}

void
paddle_reset(Paddle* paddle)
{
  paddle->x = paddle->initial_x;
  paddle->y = paddle->intiial_y;
}

void
paddle_draw(Paddle* paddle)
{
  DrawRectangleRec(
    (Rectangle){ paddle->x, paddle->y, paddle->width, paddle->height },
    paddle->color);
}

void
paddle_update(Paddle* paddle)
{
  // move paddle
  if (IsKeyDown(KEY_LEFT) && paddle->x > 0) {
    paddle->x -= paddle->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_RIGHT) && paddle->x < GetScreenWidth() - paddle->width) {
    paddle->x += paddle->speed * GetFrameTime();
  }
}

// BALL

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
  bool is_active;

} Ball;

void
ball_init(Ball* ball, Paddle* paddle)
{
  ball->radius = 10.0f;
  ball->initial_x = paddle->x + paddle->width / 2;
  ball->initial_y = paddle->y - ball->radius * 2;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->speed = 400.0f;
  ball->direction = (Vector2){
    GetRandomValue(0, 1) == 0 ? -1 : 1,
    GetRandomValue(0, 1) == 0 ? -1 : 1,
  };
  ball->color = RED;
  ball->is_active = false;
}

void
ball_reset(Ball* ball)
{
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->direction = (Vector2){
    GetRandomValue(0, 1) == 0 ? -1 : 1,
    GetRandomValue(0, 1) == 0 ? -1 : 1,
  };
  ball->is_active = false;
}

void
ball_draw(Ball* ball)
{
  DrawCircleV((Vector2){ ball->x, ball->y }, ball->radius, ball->color);
}

void
ball_update(Ball* ball, Paddle* paddle)
{
  // update ball position
  if (!ball->is_active) {
    ball->x = paddle->x + paddle->width / 2;
    ball->y = paddle->y - ball->radius * 2;
  }

  // activate ball
  if (IsKeyPressed(KEY_SPACE)) {
    ball->is_active = !ball->is_active;
  }

  // move ball
  if (ball->is_active) {
    ball->x += ball->direction.x * ball->speed * GetFrameTime();
    ball->y += ball->direction.y * ball->speed * GetFrameTime();
  }

  // normalize direction vector
  if (ball->direction.x != 0 && ball->direction.y != 0) {
    ball->direction = Vector2Normalize(ball->direction);
  }

  // ball bounds
  if (ball->x < ball->radius || ball->x > GetScreenWidth() - ball->radius) {
    ball->direction.x *= -1;
  }
  if (ball->y < ball->radius) {
    ball->direction.y *= -1;
  }
}

// UTILITY FUNCTIONS

void
reset(Paddle* paddle, Ball* ball)
{
  ball_reset(ball);
  paddle_reset(paddle);
}

void
center_and_draw_text(char* text,
                     int font_size,
                     int x,
                     int y,
                     int width,
                     int height)
{
  int text_width = MeasureText(text, font_size);
  int text_x = x + width / 2 - text_width / 2;
  int text_y = y + height / 2 - font_size / 2;
  Color color = BLACK;
  DrawText(text, text_x, text_y, font_size, color);
}

// MAIN

int
main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Breakout";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  int lives = 5;
  bool game_over = false;
  bool game_won = false;

  Brick bricks[ROWS * COLS];

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      float x = j * (BRICK_WIDTH + BRICK_GAP);
      float y = i * (BRICK_HEIGHT + BRICK_GAP);

      Brick brick;
      brick_init(&brick, x, y);

      bricks[i * COLS + j] = brick;
    }
  }

  Paddle paddle;
  Ball ball;

  paddle_init(&paddle);
  ball_init(&ball, &paddle);

  while (!WindowShouldClose()) {

    // UPDATE

    // game over condition
    if (lives <= 0) {
      game_over = true;
    }

    // game won condition
    bool bricks_active = false;
    for (int i = 0; i < ROWS * COLS; i++) {
      if (bricks[i].is_active) {
        bricks_active = true;
        break;
      }
    }

    if (!bricks_active) {
      game_won = true;
    }

    if (!game_over && !game_won) {
      paddle_update(&paddle);
      ball_update(&ball, &paddle);

      // ball collision paddle
      if (CheckCollisionCircleRec(
            (Vector2){ ball.x, ball.y },
            ball.radius,
            (Rectangle){ paddle.x, paddle.y, paddle.width, paddle.height })) {
        ball.direction.y *= -1;
      }

      // ball collision bricks
      for (int i = 0; i < ROWS * COLS; i++) {
        if (CheckCollisionCircleRec((Vector2){ ball.x, ball.y },
                                    ball.radius,
                                    (Rectangle){ bricks[i].x,
                                                 bricks[i].y,
                                                 bricks[i].width,
                                                 bricks[i].height })) {
          if (bricks[i].is_active) {
            ball.direction.y *= -1;
            bricks[i].is_active = false;
          }
        }
      }

      // update lives
      if (ball.y > GetScreenHeight() - ball.radius) {
        lives--;
        reset(&paddle, &ball);
      }

    } else {
      if (IsKeyPressed(KEY_ENTER)) {
        lives = 5;
        game_over = false;
        game_won = false;

        paddle_init(&paddle);
        ball_init(&ball, &paddle);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    // DRAW

    DrawText(TextFormat("%d", lives), 20, GetScreenHeight() - 50, 40, BLACK);

    for (int i = 0; i < ROWS * COLS; i++) {
      brick_draw(&bricks[i]);
    }

    paddle_draw(&paddle);
    ball_draw(&ball);

    if (game_over) {
      center_and_draw_text(
        "GAME OVER", 40, 0, 0, (int)GetScreenWidth(), (int)GetScreenHeight());
    }
    if (game_won) {
      center_and_draw_text(
        "YOU WIN", 40, 0, 0, (int)GetScreenWidth(), (int)GetScreenHeight());
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
