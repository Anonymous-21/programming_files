#include "raylib.h"
#include "raymath.h"

#define NUM_OF_BALLS 200

class Ball {
public:
  int x;
  int y;
  int radius;
  int speed;
  Vector2 direction;
  Color color;

  void init() {
    radius = GetRandomValue(5, 30);
    x = GetRandomValue(radius, GetScreenWidth() - radius);
    y = GetRandomValue(radius, GetScreenHeight() - radius);
    speed = GetRandomValue(100, 300);
    direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1;
    direction.y = GetRandomValue(0, 1) == 0 ? -1 : 1;
    color = (Color){static_cast<unsigned char>(GetRandomValue(0, 255)),
                    static_cast<unsigned char>(GetRandomValue(0, 255)),
                    static_cast<unsigned char>(GetRandomValue(0, 255)), 255};
  }

  void draw() { DrawCircle(x, y, radius, color); }

  void update() {
    // move ball
    x += direction.x * speed * GetFrameTime();
    y += direction.y * speed * GetFrameTime();

    // ball bounds
    if (x < radius || x > GetScreenWidth() - radius) {
      direction.x *= -1;
    } else if (y < radius || y > GetScreenHeight() - radius) {
      direction.y *= -1;
    }

    // // normalize direction
    // if (direction.x != 0 && direction.y != 0) {
    //   direction = Vector2Normalize(direction);
    // }
  }
};

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Bouncing Balls";
  const Color screenBackground = SKYBLUE;

  InitWindow(screenWidth, screenHeight, screenTitle);

  Ball balls[NUM_OF_BALLS];

  for (int i = 0; i < NUM_OF_BALLS; i++) {
    Ball ball;
    ball.init();

    balls[i] = ball;
  }

  while (!WindowShouldClose()) {
    for (int i = 0; i < NUM_OF_BALLS; i++) {
      balls[i].update();
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    for (int i = 0; i < NUM_OF_BALLS; i++) {
      balls[i].draw();
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
