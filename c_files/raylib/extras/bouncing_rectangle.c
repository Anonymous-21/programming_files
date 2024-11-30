#include "raylib.h"

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Bouncing Rectangle";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  Rectangle rect = (Rectangle){0, 0, 30, 30};
  Color rect_color = BLUE;
  int change_x = 5;
  int change_y = 6;

  while (!WindowShouldClose()) {

    rect.x += change_x;
    rect.y += change_y;

    if (rect.x <= 0 || rect.x >= GetScreenWidth() - rect.width) {
      change_x *= -1;
    } else if (rect.y <= 0 || rect.y >= GetScreenHeight() - rect.height) {
      change_y *= -1;
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    DrawRectangleRec(rect, rect_color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
