#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

typedef struct Player
{
    double x;
    double y;
    double width;
    double height;
    Color color;
    double speed;
    double diagonal_speed;
    double max_health;
    double health;

} Player;

void initPlayer(Player *player);
void drawPlayer(Player *player);
void updatePlayer(Player *player);

#endif