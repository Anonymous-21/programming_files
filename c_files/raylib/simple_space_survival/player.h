#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

typedef struct Player
{
    Texture2D background;
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;

}Player;

void init_player(Player *player, Texture2D background);
void draw_player(Player *player);

#endif