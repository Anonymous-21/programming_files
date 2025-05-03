#include <raylib.h>
#include <math.h>

typedef struct Ring
{
  Vector2 center;
  float inner_radius;
  float outer_radius;
  float start_angle;
  float end_angle;
  int segments;
  Color color;

} Ring;

typedef struct Line
{
  Vector2 start_pos;
  Vector2 end_pos;
  float thickness;
  Color color;

} Line;

int main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Radar Sweep";
  const Color SCREEN_BACKGROUND = SKYBLUE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Ring ring = {
      .center = (Vector2){GetScreenWidth() * 0.5f, GetScreenHeight() * 0.5f},
      .inner_radius = 250.0f,
      .outer_radius = 260.0f,
      .start_angle = 0.0f,
      .end_angle = 360.0f,
      .segments = 64,
      .color = RED,
  };

  Line line = {
      .start_pos = ring.center,
      .end_pos = ring.center,
      .thickness = 5.0f,
      .color = BLACK,
  };

  float angle = 0.0f;
  float sweep_speed = 100.0f;

  while (!WindowShouldClose())
  {
    angle += sweep_speed * GetFrameTime();
    if (angle >= 360)
    {
      angle = 0;
    }

    line.end_pos.x = ring.center.x + ring.inner_radius * cosf(angle * DEG2RAD);
    line.end_pos.y = ring.center.y + ring.inner_radius * sinf(angle * DEG2RAD);

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