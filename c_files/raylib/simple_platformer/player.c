#include "player.h"
#include "raylib.h"

void initPlayer(Player *player) {
  player->width = 30;
  player->height = 30;
  player->ground_level = GetScreenHeight() - 40 - player->height;
  player->x = 40 + player->width;
  player->y = player->ground_level;
  player->color = BLUE;
  player->change_x = 8;
  player->change_y = 0;
  player->jump_force = -20;
  player->gravity = 1;
  player->can_jump = true;
}

void drawPlayer(Player *player) {
  DrawRectangleRec(
      (Rectangle){player->x, player->y, player->width, player->height},
      player->color);
}

void updatePlayer(Player *player) {

  // move player horizontally

  if (IsKeyDown(KEY_RIGHT)) {
    player->x += player->change_x;
  } else if (IsKeyDown(KEY_LEFT)) {
    player->x -= player->change_x;
  }

  // player jump

  if (IsKeyPressed(KEY_UP) && player->can_jump) {
    player->change_y = player->jump_force;
    player->can_jump = false;
  }

  player->change_y += player->gravity;
  player->y += player->change_y;
}
