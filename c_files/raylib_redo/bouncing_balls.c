#include <raylib.h>
#include <raymath.h>

#define NUM_OF_BALLS 200

typedef struct Ball
{
  Vector2 pos;
  float radius;
  float speed;
  Vector2 direction;
  Color color;

} Ball;

int
main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Bouncing Balls";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Ball balls[NUM_OF_BALLS];

  for (int i = 0; i < NUM_OF_BALLS; i++) {
    Ball ball;
    ball.radius = GetRandomValue(10, 30);
    ball.pos.x = GetRandomValue(ball.radius, GetScreenWidth() - ball.radius);
    ball.pos.y = GetRandomValue(ball.radius, GetScreenHeight() - ball.radius);
    ball.speed = GetRandomValue(100, 300);
    ball.direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1;
    ball.direction.y = GetRandomValue(0, 1) == 0 ? -1 : 1;
    ball.color = (Color){ GetRandomValue(0, 255),
                          GetRandomValue(0, 255),
                          GetRandomValue(0, 255),
                          255 };

    balls[i] = ball;
  }

  while (!WindowShouldClose()) {
    for (int i = 0; i < NUM_OF_BALLS; i++) {
      // move balls
      balls[i].pos.x += balls[i].direction.x * balls[i].speed * GetFrameTime();
      balls[i].pos.y += balls[i].direction.y * balls[i].speed * GetFrameTime();

      // normalize ball direction
      if (balls[i].direction.x != 0 && balls[i].direction.y != 0) {
        balls[i].direction = Vector2Normalize(balls[i].direction);
      }

      // ball bounds
      if (balls[i].pos.x < balls[i].radius ||
          balls[i].pos.x > GetScreenWidth() - balls[i].radius) {
        balls[i].direction.x *= -1;
      }
      if (balls[i].pos.y < balls[i].radius ||
          balls[i].pos.y > GetScreenHeight() - balls[i].radius) {
        balls[i].direction.y *= -1;
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    for (int i = 0; i < NUM_OF_BALLS; i++) {
      DrawCircleV(balls[i].pos, balls[i].radius, balls[i].color);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}