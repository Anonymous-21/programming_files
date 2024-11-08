#include "ball.h"
#include "bricks.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Breakout";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  const int livesLength = 10;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  bool game_win = false;
  bool bricks_destroyed = false;
  int lives = 5;
  char lives_str[livesLength];

  Paddle paddle;
  Ball ball;
  Bricks bricks;

  initPaddle(&paddle);
  initBall(&ball);
  initBricks(&bricks);

  while (!WindowShouldClose()) {
    // convert lives to string
    snprintf(lives_str, livesLength, "Lives: %d\n", lives);

    // check for destroyed bricks
    for (int i = 0; i < bricks.rows; i++) {
      for (int j = 0; j < bricks.cols; j++) {
        if (bricks.list[i][j].x != -2 || bricks.list[i][j].y != -2) {
          bricks_destroyed = false;
          break;
        } else {
          bricks_destroyed = true;
        }
      }
    }

    // game win condition - all bricks destroyed
    if (bricks_destroyed) {
      game_win = true;
    }

    // game over condition - all lives lost
    if (lives <= 0) {
      game_over = true;
    }
    if (!game_over && !game_win) { // paddle
      movePaddle(&paddle);

      // ball
      moveBall(&ball);
      ballCollisionWalls(&ball, &lives);

      // ball collision paddle
      for (int i = 0; i < bricks.rows; i++) {
        for (int j = 0; j < bricks.cols; j++) {
        }
      }
      if (CheckCollisionCircleRec(
              (Vector2){ball.x, ball.y}, ball.radius,
              (Rectangle){paddle.x, paddle.y, paddle.width, paddle.height})) {
        ball.change_y *= -1;
      }

      // ball collision bricks
      for (int i = 0; i < bricks.rows; i++) {
        for (int j = 0; j < bricks.cols; j++) {
          if (CheckCollisionCircleRec(
                  (Vector2){ball.x, ball.y}, ball.radius,
                  (Rectangle){bricks.list[i][j].x, bricks.list[i][j].y,
                              bricks.width, bricks.height})) {
            ball.change_y *= -1;
            bricks.list[i][j] = (Vector2){-2, -2};
          }
        }
      }
    } else if (game_over || game_win) {
      if (IsKeyPressed(KEY_ENTER)) {
        bricks_destroyed = false;
        lives = 5;
        game_over = false;
        game_win = false;
        initPaddle(&paddle);
        initBall(&ball);
        initBricks(&bricks);
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    if (!game_over && !game_win) {
      drawPaddle(&paddle);
      drawBall(&ball);
      drawBricks(&bricks);
      DrawText(lives_str, 20, GetScreenHeight() - 40, 30, GRAY);
    } else if (game_win) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), RAYWHITE);
      DrawText("You win", GetScreenWidth() / 2 - 40, GetScreenHeight() / 2, 30,
               GRAY);
      DrawText("Press 'enter' to restart", GetScreenWidth() / 2 - 100,
               GetScreenHeight() / 2 + 50, 20, GRAY);
    } else if (game_over) {
      DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), RAYWHITE);
      DrawText("You lose", GetScreenWidth() / 2 - 40, GetScreenHeight() / 2, 30,
               GRAY);
      DrawText("Press 'enter' to restart", GetScreenWidth() / 2 - 100,
               GetScreenHeight() / 2 + 50, 20, GRAY);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
