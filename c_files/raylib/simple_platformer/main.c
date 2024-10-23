#include "levels.h"
#include "player.h"
#include "raylib.h"

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 800;
  const char screenTitle[] = "Simple Platformer";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  Levels levels;
  Player player;

  initLevels(&levels);
  initPlayer(&player);

  while (!WindowShouldClose()) {

    updatePlayer(&player);

    // player collision walls
    for (int i = 0; i < ROW; i++) {
      for (int j = 0; j < COL; j++) {
        int x = j * levels.block_size;
        int y = i * levels.block_size;

        if (levels.level[i][j] == 1) {
          if (CheckCollisionRecs(
                  (Rectangle){x, y, levels.block_size, levels.block_size},
                  (Rectangle){player.x, player.y, player.width,
                              player.height})) {
            if (player.x > x) {
              player.x = x + levels.block_size;
            } else if (player.x < x) {
              player.x = x - player.width;
              player.change_y = 0;
              player.can_jump = true;
            }

            if (player.y > y) {
              player.y = y + levels.block_size;
            } else if (player.y < y) {
              player.y = y - player.height;
            }
          }
        }
      }
    }

    BeginDrawing();

    ClearBackground(screenBackground);

    drawLevels(&levels);
    drawPlayer(&player);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
