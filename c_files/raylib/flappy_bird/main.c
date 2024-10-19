#include "pillar.h"
#include "player.h"
#include "raylib.h"
#include <stdio.h>

#define SCORE_LENGTH 20

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Flappy Bird";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;
  int score = 0;
  char score_str[SCORE_LENGTH];

  Player player;
  Pillar pillar;

  initPlayer(&player);
  initPillar(&pillar);

  while (!WindowShouldClose()) {

    if (!game_over) {

      // increase pillar speed every 100 score
      if (score % 100 == 0) {
        pillar.speed += 0.01;
      }

      // update score and convert to string
      score++;
      snprintf(score_str, SCORE_LENGTH, "Score: %d\n", score);

      updatePlayer(&player);
      updatePillar(&pillar);

      // player collision roof
      if (player.y > GetScreenHeight() + player.height) {
        game_over = true;
      }

      // player collision with pillars
      for (int i = 0; i < pillar.list_size; i++) {
        // top pillar collision
        if (CheckCollisionRecs(

                (Rectangle){pillar.top_list[i].x, pillar.top_list[i].y,
                            pillar.width, pillar.top_list[i].z},
                (Rectangle){player.x, player.y, player.width, player.height})) {
          game_over = true;

          // bottom pillar collision
        } else if (CheckCollisionRecs(

                       (Rectangle){pillar.bottom_list[i].x,
                                   pillar.bottom_list[i].y, pillar.width,
                                   pillar.bottom_list[i].z},
                       (Rectangle){player.x, player.y, player.width,
                                   player.height})) {
          game_over = true;
        }
      }

    } else if (game_over) {

      if (IsKeyPressed(KEY_ENTER)) {

        score = 0;
        game_over = false;
        initPlayer(&player);
        initPillar(&pillar);
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    // draw score
    DrawText(score_str, GetScreenWidth() - 150, 20, 20, BLACK);

    drawPlayer(&player);
    drawPillar(&pillar);

    if (game_over) {
      DrawText("Game Over", GetScreenWidth() / 2 - 70,
               GetScreenHeight() / 2 - 30, 30, BLACK);
      DrawText("Press 'Enter' to restart", GetScreenWidth() / 2 - 130,
               GetScreenHeight() / 2 + 20, 20, BLACK);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
