#include <raylib.h>
#include <raymath.h>
#include "balls.h"

// BASE BALL

void ball_init(Ball *ball, float radius, float speed, int damage, Color color, BallType type)
{
  ball->radius = radius;
  ball->pos = (Vector2){ball->radius, ball->radius};
  ball->speed = speed;
  ball->direction = (Vector2){1, 1};
  ball->damage = damage;
  ball->color = color;
  ball->type = type;
}

void ball_draw(Ball *ball)
{
  DrawCircleV(ball->pos, ball->radius, ball->color);
}

void ball_update(Ball *ball)
{
  // move ball
  ball->pos.x += ball->direction.x * ball->speed * GetFrameTime();
  ball->pos.y += ball->direction.y * ball->speed * GetFrameTime();

  // ball bounds
  if (ball->pos.x < ball->radius || ball->pos.x > GetScreenWidth() - ball->radius)
  {
    ball->direction.x *= -1;
  }
  if (ball->pos.y < ball->radius || ball->pos.y > GetScreenHeight() - ball->radius)
  {
    ball->direction.y *= -1;
  }

  // normalize ball direction
  if (ball->direction.x != 0 && ball->direction.y != 0)
  {
    ball->direction = Vector2Normalize(ball->direction);
  }
}

// NORMAL BALL

void ball_normal_init(Ball *ball)
{
  ball_init(ball, 10.0f, 250.0f, 1, RED, BALL_NORMAL);
}

void ball_normal_draw(Ball *ball)
{
  ball_draw(ball);
}

void ball_normal_update(Ball *ball)
{
  ball_update(ball);
}

// AGILE BALL

void ball_agile_init(Ball *ball)
{
  ball_init(ball, 10.0f, 250.0f, 1, YELLOW, BALL_AGILE);
}

void ball_agile_draw(Ball *ball)
{
  ball_draw(ball);
}

void ball_agile_update(Ball *ball)
{
  ball_update(ball);
}

// HEAVY BALL

void ball_heavy_init(Ball *ball)
{
  ball_init(ball, 10.0f, 250.0f, 1, YELLOW, BALL_HEAVY);
}

void ball_heavy_draw(Ball *ball)
{
  ball_draw(ball);
}

void ball_heavy_update(Ball *ball)
{
  ball_update(ball);
}

// SPLITTER BALL

void ball_splitter_init(Ball *ball)
{
  ball_init(ball, 10.0f, 250.0f, 1, YELLOW, BALL_SPLITTER);
}

void ball_splitter_draw(Ball *ball)
{
  ball_draw(ball);
}

void ball_splitter_update(Ball *ball)
{
  ball_update(ball);
}

// HOMING BALL

void ball_homing_init(Ball *ball)
{
  ball_init(ball, 10.0f, 250.0f, 1, YELLOW, BALL_HOMING);
}

void ball_homing_draw(Ball *ball)
{
  ball_draw(ball);
}

void ball_homing_update(Ball *ball)
{
  ball_update(ball);
}