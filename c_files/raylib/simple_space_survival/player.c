#include "raylib.h"
#include "player.h"

void init_player(Player *player, Texture2D background)
{
    player->background = background;
    player->x = player->background.width/2;
    player->y = player->background.height/2;
}