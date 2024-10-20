#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

typedef struct Player {
  float x;
  float y;
  float width;
  float height;
  Color color;
  float change_y;
  float gravity;
  float jump_force;

} Player;

void initPlayer(Player *player);
void drawPlayer(Player *player);
void updatePlayer(Player *player);

#endif // PLAYER_H
