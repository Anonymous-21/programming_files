#include <raylib.h>
#include <raymath.h>

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
ball_init(Ball* ball)
{
  ball->initial_x = (float)GetScreenWidth() / 2;
  ball->initial_y = (float)GetScreenHeight() / 2;
  ball->x = ball->initial_x;
  ball->y = ball->initial_y;
  ball->radius = 10.0f;
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
ball_update(Ball* ball)
{
  // activate ball
  if (IsKeyPressed(KEY_SPACE)) {
    ball->is_active = !ball->is_active;
  }

  // move ball
  if (ball->is_active) {
    ball->x += ball->direction.x * ball->speed * GetFrameTime();
    ball->y += ball->direction.y * ball->speed * GetFrameTime();
  }

  // normalize direction
  if (ball->direction.x != 0 && ball->direction.y != 0) {
    ball->direction = Vector2Normalize(ball->direction);
  }

  // ball bounds
  if (ball->y < ball->radius || ball->y > GetScreenHeight() - ball->radius) {
    ball->direction.y *= -1;
  }
}

// PADDLE
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

void
paddle_init(Paddle* paddle, float x)
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

void
paddle_reset(Paddle* paddle)
{
  paddle->x = paddle->initial_x;
  paddle->y = paddle->initial_y;
}

void
paddle_draw(Paddle* paddle)
{
  DrawRectangleRec(
    (Rectangle){ paddle->x, paddle->y, paddle->width, paddle->height },
    paddle->color);
}

void
paddle_update_player(Paddle* paddle)
{
  // move paddle
  if (IsKeyDown(KEY_UP) && paddle->y > 0) {
    paddle->y -= paddle->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_DOWN) && paddle->y < GetScreenHeight() - paddle->height) {
    paddle->y += paddle->speed * GetFrameTime();
  }
}

void
paddle_update_ai(Paddle* paddle, Ball* ball)
{
  // move paddle
  if (ball->y < paddle->y + paddle->height / 2 && paddle->y > 0) {
    paddle->y -= paddle->speed * GetFrameTime();
  }
  if (ball->y > paddle->y + paddle->height / 2 &&
      paddle->y < GetScreenHeight() - paddle->height) {
    paddle->y += paddle->speed * GetFrameTime();
  }
}

// RESET FUNCTION
void
reset(Paddle* player, Paddle* ai, Ball* ball)
{
  ball_reset(ball);
  paddle_reset(player);
  paddle_reset(ai);
}

// MAIN
int
main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Pong";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  int score_left = 0;
  int score_right = 0;
  Ball ball;
  Paddle player;
  Paddle ai;

  ball_init(&ball);
  paddle_init(&player, 10.0f);
  paddle_init(&ai, GetScreenWidth() - player.width - 10.0f);

  while (!WindowShouldClose()) {

    // UPDATE
    ball_update(&ball);
    paddle_update_player(&player);
    paddle_update_ai(&ai, &ball);

    // ball collision paddles
    if (CheckCollisionCircleRec(
          (Vector2){ ball.x, ball.y },
          ball.radius,
          (Rectangle){ player.x, player.y, player.width, player.height })) {
      ball.direction.x *= -1;
    }
    if (CheckCollisionCircleRec(
          (Vector2){ ball.x, ball.y },
          ball.radius,
          (Rectangle){ ai.x, ai.y, ai.width, ai.height })) {
      ball.direction.x *= -1;
    }

    // update scores
    if (ball.x < ball.radius) {
      score_right++;
      reset(&player, &ai, &ball);
    }

    if (ball.x > GetScreenWidth() - ball.radius) {
      score_left++;
      reset(&player, &ai, &ball);
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    // DRAW

    // draw scores
    DrawText(TextFormat("%d", score_left), 200, 30, 40, BLACK);
    DrawText(
      TextFormat("%d", score_right), GetScreenWidth() - 200, 30, 40, BLACK);

    ball_draw(&ball);
    paddle_draw(&player);
    paddle_draw(&ai);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
