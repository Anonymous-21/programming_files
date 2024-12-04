#include "raylib.h"

#include "player.h"

void initPlayer(Player *player)
{
    player->x = (double)GetScreenWidth() / 2;
    player->y = (double)GetScreenHeight() / 2;
    player->width = 30;
    player->height = 30;
    player->color = BLUE;
    player->speed = 5;
    player->diagonal_speed = 0.75;
    player->max_health = 100;
    player->health = player->max_health;
}

void drawPlayer(Player *player)
{
    DrawRectangleRec((Rectangle){player->x,
                                 player->y,
                                 player->width,
                                 player->height},
                     player->color);
}

void updatePlayer(Player *player)
{
    if (IsKeyDown(KEY_D))
    {
        player->x += player->speed;

        if (IsKeyDown(KEY_W))
        {
            player->x += player->diagonal_speed;
            player->y -= player->diagonal_speed;
        }
        else if (IsKeyDown(KEY_S))
        {
            player->x += player->diagonal_speed;
            player->y += player->diagonal_speed;
        }
    }
    else if (IsKeyDown(KEY_A))
    {
        player->x -= player->speed;

        if (IsKeyDown(KEY_W))
        {
            player->x -= player->diagonal_speed;
            player->y -= player->diagonal_speed;
        }
        else if (IsKeyDown(KEY_S))
        {
            player->x -= player->diagonal_speed;
            player->y += player->diagonal_speed;
        }
    }
    else if (IsKeyDown(KEY_W))
    {
        player->y -= player->speed;
    }
    else if (IsKeyDown(KEY_S))
    {
        player->y += player->speed;
    }
}