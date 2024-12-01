#include "player.h"
#include "raylib.h"

void initPlayer(Player *player)
{
    player->width = 40;
    player->height = 40;
    player->x = (double)GetScreenWidth() / 2 - player->width / 2;
    player->y = (double)GetScreenHeight() / 2 - player->height / 2;
    player->color = BLUE;
}

void drawPlayer(Player *player)
{
    DrawRectangleRec(
        (Rectangle){player->x, player->y, player->width, player->height},
        player->color);
}