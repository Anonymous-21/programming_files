#include <raylib.h>
#include <raymath.h>
#include <math.h>

#define NUM_OF_BALLS 200

typedef struct Ball
{
  Vector2 pos;
  float radius;
  Vector2 velocity;
  Color color;

} Ball;

int main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Bouncing Balls";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Ball balls[NUM_OF_BALLS];

  for (int i = 0; i < NUM_OF_BALLS; i++)
  {
    float speed = GetRandomValue(100, 300);
    float angle = GetRandomValue(0, 360) * DEG2RAD;

    Ball ball = {
        .radius = GetRandomValue(5, 30),
        .pos.x = GetRandomValue(ball.radius, GetScreenWidth() - ball.radius),
        .pos.y = GetRandomValue(ball.radius, GetScreenHeight() - ball.radius),
        .color =
            (Color){
                GetRandomValue(0, 255),
                GetRandomValue(0, 255),
                GetRandomValue(0, 255),
                255,
            },
        .velocity.x = cosf(angle) * speed,
        .velocity.y = sinf(angle) * speed,
    };

    balls[i] = ball;
  }

  while (!WindowShouldClose())
  {
    for (int i = 0; i < NUM_OF_BALLS; i++)
    {
      // move ball
      balls[i].pos.x += balls[i].velocity.x * GetFrameTime();
      balls[i].pos.y += balls[i].velocity.y * GetFrameTime();

      // ball bounds
      if (balls[i].pos.x < balls[i].radius ||
          balls[i].pos.x > GetScreenWidth() - balls[i].radius)
      {
        balls[i].velocity.x *= -1;
      }
      
      if (balls[i].pos.y < balls[i].radius ||
          balls[i].pos.y > GetScreenHeight() - balls[i].radius)
      {
        balls[i].velocity.y *= -1;
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    for (int i = 0; i < NUM_OF_BALLS; i++)
    {
      DrawCircleV(balls[i].pos, balls[i].radius, balls[i].color);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}