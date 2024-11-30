#include "raylib.h"

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Box";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  int radius = 10;
  Color color = DARKGREEN;
  int gap = 10;
  int margin_x = (GetScreenWidth() - ((radius * 2) * 10 + (gap * 9))) / 2;
  int margin_y = (GetScreenHeight() - ((radius * 2) * 10 + (gap * 9))) / 2;

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(screenBackground);

    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < i + 1; j++) {

        int x = j * (radius * 2 + gap) + margin_x;
        int y = i * (radius * 2 + gap) + margin_y;

        DrawCircle(x, y, radius, color);
      }
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
