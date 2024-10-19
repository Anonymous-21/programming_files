#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

typedef struct Player
{
  float ground_level;
  float x;
  float y;
  float width;
  float height;
  Color color;
  float change_y;
  float jump_force;
  float gravity;
  bool can_jump;

}Player;

void initPlayer(Player *player);
void drawPlayer(Player *player);
void movePlayer(Player *player);

#endif // PlAYER_H
