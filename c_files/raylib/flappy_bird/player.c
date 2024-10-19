#include "player.h"
#include "raylib.h"

void initPlayer(Player *player) {
  player->x = 20;
  player->y = 20;
  player->width = 30;
  player->height = 30;
  player->color = BLUE;
  player->change_y = 0;
  player->gravity = 1;
  player->jump_force = -12;
}

void drawPlayer(Player *player) {
  DrawRectangleRec(
      (Rectangle){player->x, player->y, player->width, player->height},
      player->color);
}

void updatePlayer(Player *player) {
  if (IsKeyPressed(KEY_UP)) {
    player->change_y = player->jump_force;
  }

  player->change_y += player->gravity;
  player->y += player->change_y;
}
