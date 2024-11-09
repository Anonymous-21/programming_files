#include "raylib.h"

int main() {
  const int TITLE_LENGTH = 10;

  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[TITLE_LENGTH] = "Pong";
  const Color SCREEN_BACKGROUND = RAYWHITE;
  const int GAME_FPS = 60;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);
    EndDrawing();
  }

  CloseWindow();

  return 0;
}
