#include "player.h"
#include "raylib.h"

void initPlayer(Player *player) {
  player->width = 30;
  player->height = 30;
  player->x = 60;
  player->y = GetScreenWidth() - player->height - 200;
  player->color = BLUE;
  player->change_x = 8;
  player->change_y = 0;
  player->gravity = 1;
  player->jump_force = -20;
  player->can_jump = true;
}

void drawPlayer(Player *player) {
  DrawRectangleRec(
      (Rectangle){player->x, player->y, player->width, player->height},
      player->color);
}

void updatePlayer(Player *player) {

  // horizontal movement
  if (IsKeyDown(KEY_RIGHT)) {
    player->x += player->change_x;
  } else if (IsKeyDown(KEY_LEFT)) {
    player->x -= player->change_x;
  }

  // vertical movement
  if (IsKeyPressed(KEY_UP) && player->can_jump) {
    player->change_y = player->jump_force;
    player->can_jump = false;
  }

  player->change_y += player->gravity;
  player->y += player->change_y;
}
