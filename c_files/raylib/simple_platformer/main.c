#include "levels.h"
#include "player.h"
#include "raylib.h"
#include <stdio.h>

#define CURRENT_LEVEL_LENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 800;
  const char screenTitle[] = "Simple Platformer";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  char current_level_str[CURRENT_LEVEL_LENGTH];

  Player player;
  Levels levels;

  initPlayer(&player);
  initLevels(&levels);

  while (!WindowShouldClose()) {

    // convert current level to string
    snprintf(current_level_str, CURRENT_LEVEL_LENGTH, "Level: %d\n",
             levels.current_level);

    // move player

    updatePlayer(&player);
    updateLevels(&levels);

    // update current level

    if (player.x < 0 && levels.current_level > 1) {
      levels.current_level--;
      player.x = GetScreenWidth() - player.width;
      player.y = player.ground_level;
    } else if (player.x > GetScreenWidth() - player.width &&
               levels.current_level < 5) {
      levels.current_level++;
      player.x = 0;
      player.y = player.ground_level;
    }

    // player collision environment

    for (int i = 0; i < ROW; i++) {
      for (int j = 0; j < COL; j++) {
        int x = j * levels.block_size;
        int y = i * levels.block_size;

        if (levels.level[i][j] == 1) {
          if (CheckCollisionRecs(
                  (Rectangle){player.x, player.y, player.width, player.height},
                  (Rectangle){x, y, levels.block_size, levels.block_size})) {
            player.can_jump = true;
            player.change_y = 0;
            player.y = y - player.height;
          }
        } else if (levels.level[i][j] == 2) {
          if (CheckCollisionRecs(
                  (Rectangle){player.x, player.y, player.width, player.height},
                  (Rectangle){x, y, levels.block_size, levels.block_size})) {
            player.x = x + levels.block_size;
          }
        } else if (levels.level[i][j] == 3) {
          if (CheckCollisionRecs(
                  (Rectangle){player.x, player.y, player.width, player.height},
                  (Rectangle){x, y, levels.block_size, levels.block_size})) {
            player.y = y + levels.block_size;
          }
        } else if (levels.level[i][j] == 4) {
          if (CheckCollisionRecs(
                  (Rectangle){player.x, player.y, player.width, player.height},
                  (Rectangle){x, y, levels.block_size, levels.block_size})) {
            player.x = x - player.width;
          }
        } else if (levels.level[i][j] == 6) {
          if (CheckCollisionRecs(
                  (Rectangle){player.x, player.y, player.width, player.height},
                  (Rectangle){x, y, levels.block_size, levels.block_size})) {
            levels.level1_pass = true;
          }
        }
      }

      BeginDrawing();
      ClearBackground(screenBackground);

      // draw current level number
      DrawText(current_level_str, 50, 50, 30, GRAY);

      // draw levels
      drawLevels(&levels);

      // draw player
      drawPlayer(&player);

      EndDrawing();
    }

    CloseWindow();

    return 0;
  }
}
