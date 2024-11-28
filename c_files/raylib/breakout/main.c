#include "ball.h"
#include "bricks.h"
#include "constants.h"
#include "paddle.h"
#include "raylib.h"
#include <stdbool.h>
#include <stdio.h>

#define STR_LIVES_LENGTH 10

int main(void) {
  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  bool game_over = false;
  bool game_won = false;
  int lives = 5;
  char lives_str[STR_LIVES_LENGTH];

  Paddle paddle;
  Ball ball;
  Bricks bricks;

  initPaddle(&paddle);
  initBall(&ball);
  initBricks(&bricks);

  while (!WindowShouldClose()) {
    if (!game_over && !game_won) {
      // game over condition
      if (lives <= 0) {
        game_over = true;
      }

      // game won condition
      bool all_bricks_destroyed = true;

      for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
          if (bricks.list[i * 10 + j].is_active) {
            all_bricks_destroyed = false;
            break;
          }
        }
        if (!all_bricks_destroyed) {
          break;
        }
      }

      if (all_bricks_destroyed) {
        game_won = true;
      }

      // convert lives to string
      snprintf(lives_str, STR_LIVES_LENGTH, "Lives: %d\n", lives);

      updatePaddle(&paddle);
      updateBall(&ball, &paddle, &bricks, &lives);

      BeginDrawing();
      ClearBackground(SCREEN_BACKGROUND);

      // draw lives
      DrawText(lives_str, 20, GetScreenHeight() - 50, 30, GRAY);

      drawPaddle(&paddle);
      drawBall(&ball);
      drawBricks(&bricks);

      EndDrawing();
    } else {
      lives = 5;
      game_over = false;
      game_won = false;
      initPaddle(&paddle);
      initBall(&ball);
      initBricks(&bricks);
    }
  }

  CloseWindow();

  return 0;
}
