#include "raylib.h"

void genGrid(Vector2 *array[], int rows, int cols, int block_size, int gap) {
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      int x = j * block_size + gap;
      int y = i * block_size + gap;

      array[i][j] = (Vector2){x, y};
    }
  }
}

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Inventory";
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
