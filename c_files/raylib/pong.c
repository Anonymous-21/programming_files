#include <raylib.h>
#include <raymath.h>

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

void ball_init(Ball *ball)
{
  ball->initial_pos =
      (Vector2){GetScreenWidth() * 0.5f, GetScreenHeight() * 0.5f};
  ball->pos = ball->initial_pos;
  ball->radius = 10.0f;
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
  DrawCircleV(ball->pos, ball->radius, ball->color);
}

void ball_update(Ball *ball)
{
  // activate/deactivate ball
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
  if (ball->pos.y < ball->radius ||
      ball->pos.y > GetScreenHeight() - ball->radius)
  {
    ball->direction.y *= -1;
  }

  // normalize direction vector
  if (ball->direction.x != 0 && ball->direction.y != 0)
  {
    ball->direction = Vector2Normalize(ball->direction);
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

void paddle_init(Paddle *paddle, float x)
{
  float height = 100.0f;
  paddle->initial_rect =
      (Rectangle){x, GetScreenHeight() * 0.5f - height / 2, 10.0f, height};
  paddle->rect = paddle->initial_rect;
  paddle->speed = 300.0f;
  paddle->color = BLACK;
}

void paddle_reset(Paddle *paddle) { paddle->rect = paddle->initial_rect; }

void paddle_draw(Paddle *paddle)
{
  DrawRectangleRec(paddle->rect, paddle->color);
}

void paddle_update_player(Paddle *player)
{
  // move paddle
  if (IsKeyDown(KEY_UP))
  {
    player->rect.y -= player->speed * GetFrameTime();
  }
  if (IsKeyDown(KEY_DOWN))
  {
    player->rect.y += player->speed * GetFrameTime();
  }

  // paddle bounds
  player->rect.y =
      Clamp(player->rect.y, 0, GetScreenHeight() - player->rect.height);
}

void paddle_update_ai(Paddle *ai, Ball *ball)
{
  // move paddle
  if (ball->pos.y < ai->rect.y + ai->rect.height / 2)
  {
    ai->rect.y -= ai->speed * GetFrameTime();
  }
  if (ball->pos.y > ai->rect.y + ai->rect.height / 2)
  {
    ai->rect.y += ai->speed * GetFrameTime();
  }

  // paddle bounds
  ai->rect.y = Clamp(ai->rect.y, 0, GetScreenHeight() - ai->rect.height);
}

// GAME MANAGER

typedef struct Game
{
  int score_left;
  int score_right;

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
  paddle_init(&game->ai, GetScreenWidth() - game->player.rect.width - 10.0f);
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
  DrawText(TextFormat("%d", game->score_left), 200, 30, 40, BLACK);
  DrawText(TextFormat("%d", game->score_right), GetScreenWidth() - 200, 30, 40,
           BLACK);

  ball_draw(&game->ball);
  paddle_draw(&game->player);
  paddle_draw(&game->ai);
}

void game_update(Game *game)
{
  ball_update(&game->ball);
  paddle_update_player(&game->player);
  paddle_update_ai(&game->ai, &game->ball);

  // ball collision paddle
  if (CheckCollisionCircleRec(game->ball.pos, game->ball.radius,
                              game->player.rect))
  {
    game->ball.direction.x *= -1;
  }
  if (CheckCollisionCircleRec(game->ball.pos, game->ball.radius,
                              game->ai.rect))
  {
    game->ball.direction.x *= -1;
  }

  // update scores
  if (game->ball.pos.x < game->ball.radius)
  {
    game->score_right += 1;
    game_reset(game);
  }
  if (game->ball.pos.x > GetScreenWidth() - game->ball.radius)
  {
    game->score_left += 1;
    game_reset(game);
  }
}

// MAIN

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

    game_update(&game);
    game_draw(&game);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
