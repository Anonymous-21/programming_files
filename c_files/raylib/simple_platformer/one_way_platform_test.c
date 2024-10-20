#include "raylib.h"
#include <stdbool.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "test window";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  // player

  int player_width = 30;
  int player_height = 30;
  int ground_level = GetScreenHeight() - player_height;
  int player_x = 10;
  int player_y = ground_level;
  Color player_color = BLUE;
  int player_change_x = 8;
  int player_change_y = 0;
  int gravity = 1;
  int jump_force = -20;
  bool can_jump = true;

  // platform

  int platform_x = GetScreenWidth() / 2;
  int platform_y = 500;
  int platform_width = 100;
  int platform_height = 10;
  Color platform_color = BLACK;

  while (!WindowShouldClose()) {

    // move player
    if (IsKeyDown(KEY_D) && player_x <= GetScreenWidth() - player_width) {
      player_x += player_change_x;
    } else if (IsKeyDown(KEY_A) && player_x >= 0) {
      player_x -= player_change_x;
    }

    // player jump
    if (IsKeyPressed(KEY_SPACE) && can_jump) {
      player_change_y = jump_force;
      can_jump = false;
    }

    player_change_y += gravity;
    player_y += player_change_y;

    if (player_y >= ground_level) {
      can_jump = true;
      player_y = ground_level;
      player_change_y = 0;
    }

    // platform collision player
    if (CheckCollisionRecs(
            (Rectangle){player_x, player_y, player_width, player_height},
            (Rectangle){platform_x, platform_y, platform_width, platform_height})) {

      if (player_change_y > 0)
      {
        can_jump = true;
        player_y = platform_y - player_height;
        player_change_y = 0;
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    // draw player
    DrawRectangle(player_x, player_y, player_width, player_height,
                  player_color);

    // draw platform
    DrawRectangle(platform_x, platform_y, platform_width, platform_height,
                  platform_color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
