#include "raylib.h"
#include <math.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Radar Sweep";
  const Color screenBackground = BLACK;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  double angle = 0;

  double ring_x = (double)GetScreenWidth() / 2;
  double ring_y = (double)GetScreenHeight() / 2;
  double ring_inner_radius = 250;
  double ring_outer_radius = 260;
  double ring_start_angle = 0;
  double ring_end_angle = 360;
  double ring_segments = 50;
  Color ring_color = GREEN;

  double line_start_x = ring_x;
  double line_start_y = ring_y;
  double line_end_x = ring_x;
  double line_end_y = ring_y;
  double line_thickness = 5;
  Color line_color = YELLOW;

  while (!WindowShouldClose()) {

    angle++;
    if (angle > 360) {
      angle = 0;
    }

    double angle_radians = (PI / 180) * angle;

    line_end_x = ring_x + cos(angle_radians) * ring_inner_radius;
    line_end_y = ring_y + sin(angle_radians) * ring_inner_radius;

    BeginDrawing();
    ClearBackground(screenBackground);

    DrawRing((Vector2){ring_x, ring_y}, ring_inner_radius, ring_outer_radius,
             ring_start_angle, ring_end_angle, ring_segments, ring_color);

    DrawLineEx((Vector2){line_start_x, line_start_y},
               (Vector2){line_end_x, line_end_y}, line_thickness, line_color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
