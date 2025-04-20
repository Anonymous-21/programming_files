#include "raylib.h"
#include "raymath.h"

#define NUM_OF_BALLS 200

typedef struct Ball {
  float x;
  float y;
  float radius;
  float speed;
  Vector2 direction;
  Color color;

} Ball;

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Bouncing Balls";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Ball balls[NUM_OF_BALLS];

  for (int i = 0; i < NUM_OF_BALLS; i++) {
    Ball ball = {
        .radius = GetRandomValue(5, 30),
        .x = GetRandomValue(ball.radius, GetScreenWidth() - ball.radius),
        .y = GetRandomValue(ball.radius, GetScreenHeight() - ball.radius),
        .speed = GetRandomValue(100, 300),
        .direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1,
        .direction.y = GetRandomValue(0, 1) == 0 ? -1 : 1,
        .color = (Color){GetRandomValue(0, 255), GetRandomValue(0, 255),
                         GetRandomValue(0, 255), 255},
    };
    balls[i] = ball;
  }

  while (!WindowShouldClose()) {

    for (int i = 0; i < NUM_OF_BALLS; i++) {

      balls[i].x += balls[i].direction.x * balls[i].speed * GetFrameTime();
      balls[i].y += balls[i].direction.y * balls[i].speed * GetFrameTime();

      if (balls[i].x < balls[i].radius ||
          balls[i].x > GetScreenWidth() - balls[i].radius) {
        balls[i].direction.x *= -1;
      }
      if (balls[i].y < balls[i].radius ||
          balls[i].y > GetScreenHeight() - balls[i].radius) {
        balls[i].direction.y *= -1;
      }

      if (balls[i].direction.x != 0 && balls[i].direction.y != 0) {
        balls[i].direction = Vector2Normalize(balls[i].direction);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    for (int i = 0; i < NUM_OF_BALLS; i++) {
      DrawCircleV((Vector2){balls[i].x, balls[i].y}, balls[i].radius,
                  balls[i].color);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
