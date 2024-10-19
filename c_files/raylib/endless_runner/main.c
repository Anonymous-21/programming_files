#include "obstacles.h"
#include "player.h"
#include "raylib.h"
#include <stdio.h>

#define SCORE_LENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 200;
  const char screenTitle[] = "Endless Runner";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  int score = 0;
  char score_str[SCORE_LENGTH];

  Player player;
  Obstacles obstacles;

  initPlayer(&player);
  initObstacles(&obstacles);

  while (!WindowShouldClose()) {

    if (!game_over) {
      // update score and convert to string
      score++;
      snprintf(score_str, SCORE_LENGTH, "Score: %d\n", score);

      movePlayer(&player);
      updateObstacles(&obstacles);

      // collistion between obstacles and player
      for (int i = 0; i < obstacles.list_size; i++) {
        if (CheckCollisionRecs(
                (Rectangle){player.x, player.y, player.width, player.height},
                (Rectangle){obstacles.list[i].x, obstacles.list[i].y,
                            obstacles.width, obstacles.height})) {
          game_over = true;
        }
      }
    } else if (game_over) {
      if (IsKeyPressed(KEY_ENTER)) {
        game_over = false;
        score = 0;
        initPlayer(&player);
        initObstacles(&obstacles);
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    // draw score
    DrawText(score_str, GetScreenWidth() - 150, 10, 20, GRAY);

    drawPlayer(&player);
    drawObstacles(&obstacles);

    if (game_over) {
      DrawText("Game Over", GetScreenWidth() / 2 - 70,
               GetScreenHeight() / 2 - 70, 30, GRAY);
      DrawText("Press 'Enter' to restart", GetScreenWidth() / 2 - 120,
               GetScreenHeight() / 2, 20, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
