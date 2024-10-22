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

  bool game_over = false;
  char current_level_str[CURRENT_LEVEL_LENGTH];

  Levels levels;
  Player player;

  initLevels(&levels);
  initPlayer(&player);

  while (!WindowShouldClose()) {

    // convert current level to string for display
    snprintf(current_level_str, CURRENT_LEVEL_LENGTH, "Level: %d\n",
             levels.current_level);

    // update Level
    updateLevels(&levels);

    // update player
    updatePlayer(&player);

    // player collision
    // walls and floor
    for (int i = 0; i < ROW; i++) {
      for (int j = 0; j < COL; j++) {
        int x = j * levels.block_size;
        int y = i * levels.block_size;

        if (levels.level[i][j] == 1) {
          if (CheckCollisionRecs(
                  (Rectangle){x, y, levels.block_size, levels.block_size},
                  (Rectangle){player.x, player.y, player.width,
                              player.height})) {
            if (player.y < y) {
              player.can_jump = true;
              player.change_y = 0;
              player.y = y - player.height;
            } else if (player.y >= y) {
              player.y = y + levels.block_size;
            }
            if (player.x > x) {
              player.x = x + levels.block_size;
            } else if (player.x <= x) {
              player.x = x - player.width;
            }
          }
        }
      }
    }

    // player level transition
    if (levels.current_level <= 1) {
      levels.current_level = 1;
    } else if (levels.current_level >= 5) {
      levels.current_level = 5;
    }

    if (player.x < 0) {
      levels.current_level--;
      player.x = GetScreenWidth() - player.width;
    } else if (player.x > GetScreenWidth() - player.width) {
      levels.current_level++;
      player.x = 0;
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    // draw current level number
    DrawText(current_level_str, levels.block_size + 10, levels.block_size + 10,
             30, GRAY);

    // draw level
    drawLevels(&levels);

    // draw player
    drawPlayer(&player);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
