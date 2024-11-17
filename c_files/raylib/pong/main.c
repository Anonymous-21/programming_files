#include "ball.h"
#include "collision_manager.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Pong";
  const Color SCREEN_BACKGROUND = RAYWHITE;
  const int GAME_FPS = 60;

  const int SCORE_LENGTH = 10;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  int left_score = 0;
  int right_score = 0;
  char left_score_str[SCORE_LENGTH];
  char right_score_str[SCORE_LENGTH];

  Paddle paddle_left;
  Paddle paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);
  initBall(&ball);

  while (!WindowShouldClose()) {

    // convert score to string
    snprintf(left_score_str, SCORE_LENGTH, "%d\n", left_score);
    snprintf(right_score_str, SCORE_LENGTH, "%d\n", right_score);

    // Move objects
    movePaddle(&paddle_left, KEY_W, KEY_S);
    movePaddle(&paddle_right, KEY_UP, KEY_DOWN);
    moveBall(&ball);

    // collisions
    paddleCollisionWalls(&paddle_left);
    paddleCollisionWalls(&paddle_right);

    ballVerticalCollision(&ball);
    ballHorizontalCollision(&ball, &paddle_left, &paddle_right, &left_score, &right_score);

    ballCollisionPaddle(&ball, &paddle_left);
    ballCollisionPaddle(&ball, &paddle_right);

    // program
    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    // draw screen divider
    DrawLineEx((Vector2){(float)GetScreenWidth() / 2, 0},
               (Vector2){(float)GetScreenWidth() / 2, GetScreenHeight()}, 5,
               GRAY);

    // draw score
    DrawText(left_score_str, (float)GetScreenWidth() / 2 - 70, 10, 30, GRAY);
    DrawText(right_score_str, (float)GetScreenWidth() / 2 + 50, 10, 30, GRAY);

    drawPaddle(&paddle_left);
    drawPaddle(&paddle_right);
    drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
