#include "grid.h"
#include "snake.h"
#include "raylib.h"

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 800;
  const char screenTitle[] = "Snake";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  Grid grid;
  Snake snake;

  initGrid(&grid);
  initSnake(&snake, &grid);

  while (!WindowShouldClose()) {
    BeginDrawing();

    ClearBackground(screenBackground);

    drawGrid(&grid);
    drawSnake(&snake);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
