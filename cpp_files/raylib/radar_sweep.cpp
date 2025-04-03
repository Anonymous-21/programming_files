#include "raylib.h"
#include <cmath>

typedef struct Ring {
  Vector2 center;
  float inner_radius;
  float outer_radius;
  float start_angle;
  float end_angle;
  int segments;
  Color color;

} Ring;

typedef struct Line {
  Vector2 start_pos;
  Vector2 end_pos;
  float thickness;
  Color color;

} Line;

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Radar Sweep";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Ring ring;
  ring.center = (Vector2){static_cast<float>(GetScreenWidth()) / 2,
                          static_cast<float>(GetScreenHeight()) / 2};
  ring.inner_radius = 250.0f;
  ring.outer_radius = 260.0f;
  ring.start_angle = 0.0f;
  ring.end_angle = 360.0f;
  ring.segments = 32;
  ring.color = DARKGREEN;

  Line line;
  line.start_pos = ring.center;
  line.end_pos = (Vector2){0, 0};
  line.thickness = 10.0f;
  line.color = YELLOW;

  float angle = 0.0f;
  float sweep_speed = 50.0f;

  while (!WindowShouldClose()) {
    angle += sweep_speed * GetFrameTime();
    if (angle > 360) {
      angle = 0.0f;
    }

    line.end_pos.x =
        ring.center.x + std::cos(angle * (PI / 180)) * ring.inner_radius;
    line.end_pos.y =
        ring.center.y + std::sin(angle * (PI / 180)) * ring.inner_radius;

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    DrawRing(ring.center, ring.inner_radius, ring.outer_radius,
             ring.start_angle, ring.end_angle, ring.segments, ring.color);

    DrawLineEx(line.start_pos, line.end_pos, line.thickness, line.color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
