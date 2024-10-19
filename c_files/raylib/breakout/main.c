#include "ball.h"
#include "bricks.h"
#include "paddle.h"
#include "raylib.h"

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Breakout";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  bool game_paused = true;
  int lives = 5;

  Paddle paddle;
  Ball ball;
  Bricks bricks;

  initPaddle(&paddle);
  initBall(&ball);
  initBricks(&bricks);

  while (!WindowShouldClose()) {

    if (!game_over) {

      // pause/unpause game with space key
      if (IsKeyPressed(KEY_SPACE) && game_paused) {
        game_paused = false;
      } else if (IsKeyPressed(KEY_SPACE) && !game_paused) {
        game_paused = true;
      }

      if (!game_paused) {
        movePaddle(&paddle);
        moveBall(&ball);

        // ball collision with paddle
        if (CheckCollisionCircleRec(
                (Vector2){ball.x, ball.y}, ball.radius,
                (Rectangle){paddle.x, paddle.y, paddle.width, paddle.height})) {
          ball.speed_y *= -1;
        }

        // ball collision with bricks
        for (int i = 0; i < bricks.size; i++) {
          if (CheckCollisionCircleRec(
                  (Vector2){ball.x, ball.y}, ball.radius,
                  (Rectangle){bricks.grid[i].x, bricks.grid[i].y, bricks.width,
                              bricks.height})) {
            ball.speed_y *= -1;
            bricks.grid[i] = (Vector2){-2, -2};
          }
        }
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    if (!game_over) {
      drawPaddle(&paddle);
      DrawBall(&ball);
      drawBricks(&bricks);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(),
                    screenBackground);
      DrawText("Game Over", GetScreenWidth() / 2, GetScreenHeight() / 2 - 30,
               40, GRAY);
      DrawText("Press 'Enter' to restart!", GetScreenWidth() / 2,
               GetScreenHeight() / 2 + 20, 30, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();
}
