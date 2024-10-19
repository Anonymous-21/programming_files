#include "player.h"
#include "raylib.h"

void initPlayer(Player *player) {
  player->width = 20;
  player->height = 50;
  player->ground_level = GetScreenHeight() - player->height;
  player->x = 20;
  player->y = player->ground_level;
  player->color = BLUE;
  player->change_y = 0;
  player->gravity = 1;
  player->jump_force = -15;
  player->can_jump = false;
}

void drawPlayer(Player *player) {

  DrawRectangleRec(
      (Rectangle){player->x, player->y, player->width, player->height},
      player->color);
}

void movePlayer(Player *player) {

  if (IsKeyPressed(KEY_UP) && player->y == player->ground_level) {
    if (player->y < player->ground_level) {
      player->can_jump = false;
    }
    player->change_y = player->jump_force;
    player->can_jump = true;
  }

  if (player->can_jump) {
    player->change_y += player->gravity;
    player->y += player->change_y;
  }

  if (player->y >= player->ground_level) {
    player->y = player->ground_level;
  }
}
