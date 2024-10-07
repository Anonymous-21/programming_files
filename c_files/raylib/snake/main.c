#include "raylib.h"
#include "grid.h"
#include "snake.h"

int main() {
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

  initSnake(&grid, &snake);
  
  while (!WindowShouldClose()) {
    updateSnake(&snake);

    BeginDrawing();

    ClearBackground(screenBackground);

    drawGrid(&grid);
    drawSnake(&snake);

    EndDrawing();
  }

  CloseWindow();
}
