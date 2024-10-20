#include "raylib.h"


int main(void)
{
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "test window";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(screenBackground);
    EndDrawing();
  }

  CloseWindow();

  return 0;
}
