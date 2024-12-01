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

} Player;

void initPlayer(Player *player);
void drawPlayer(Player *player);

#endif // PLAYER_H