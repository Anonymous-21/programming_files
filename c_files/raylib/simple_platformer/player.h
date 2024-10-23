#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

typedef struct Player {
  int x;
  int y;
  int width;
  int height;
  Color color;
  int change_x;
  int change_y;
  int gravity;
  int jump_force;
  bool can_jump;

} Player;

void initPlayer(Player *player);
void drawPlayer(Player *player);
void updatePlayer(Player *player);

#endif // PLAYER_H
