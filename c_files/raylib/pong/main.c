#include "ball.h"
#include "constants.h"
#include "paddle.h"
#include "raylib.h"
#include <stdio.h>

#define STR_LENGTH 10

int main(void) {
  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
  SetTargetFPS(GAME_FPS);

  int score_left = 0;
  int score_right = 0;
  char score_left_str[STR_LENGTH];
  char score_right_str[STR_LENGTH];

  Paddle paddle_left;
  Paddle paddle_right;
  Ball ball;

  initPaddle(&paddle_left, 10);
  initPaddle(&paddle_right, GetScreenWidth() - paddle_left.width - 10);
  initBall(&ball);

  while (!WindowShouldClose()) {

    // convert score to string
    snprintf(score_left_str, STR_LENGTH, "%d\n", score_left);
    snprintf(score_right_str, STR_LENGTH, "%d\n", score_right);

    updatePaddle(&paddle_left, KEY_W, KEY_S);
    updatePaddle(&paddle_right, KEY_UP, KEY_DOWN);
    updateBall(&ball, &paddle_left, &paddle_right, &score_left, &score_right);

    // ball collision paddle
    if (CheckCollisionCircleRec((Vector2){ball.x, ball.y}, ball.radius,
                                (Rectangle){paddle_left.x, paddle_left.y,
                                            paddle_left.width,
                                            paddle_left.height})) {
      ball.change_x *= -1;
    } else if (CheckCollisionCircleRec(
                   (Vector2){ball.x, ball.y}, ball.radius,
                   (Rectangle){paddle_right.x, paddle_right.y,
                               paddle_right.width, paddle_right.height})) {
      ball.change_x *= -1;
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    // draw screen divider
    DrawLineEx((Vector2){(float)GetScreenWidth() / 2, 0},
               (Vector2){(float)GetScreenWidth() / 2, GetScreenHeight()}, 5,
               GRAY);

    // draw scores
    DrawText(score_left_str, GetScreenWidth() / 2 - 70, 20, 30, GRAY);
    DrawText(score_right_str, GetScreenWidth() / 2 + 50, 20, 30, GRAY);

    drawPaddle(&paddle_left);
    drawPaddle(&paddle_right);
    drawBall(&ball);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
