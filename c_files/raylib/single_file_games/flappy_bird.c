#include "raylib.h"

#define PILLAR_GAP 200

// ************************************
// PLAYER
// ************************************
typedef struct Player
{
    float x;
    float y;
    float width;
    float height;
    Color color;
    float jump_force;
    float gravity;
    float change_y;
} Player;

void init_player(Player *player)
{
    player->x = 20;
    player->y = 20;
    player->width = 30;
    player->height = 30;
    player->color = RED;
    player->jump_force = -15;
    player->gravity = 1;
    player->change_y = 0;
}

void draw_player(Player *player)
{
    DrawRectangleRec((Rectangle){player->x,
                                 player->y,
                                 player->width,
                                 player->height},
                     player->color);
}

void update_player(Player *player)
{
    if (IsKeyPressed(KEY_UP))
    {
        player->change_y = player->jump_force;
    }

    player->change_y += player->gravity;
    player->y += player->change_y;
}

// ************************************
// PILLARS
// ************************************
typedef struct Pillar
{
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;
    float speed_increment;

}Pillar;

void init_pillar(Pillar *pillar)
{
    pillar->x = GetScreenWidth();
    pillar->y = 0;
    pillar->width = 100;
    pillar->height = GetRandomValue(0, GetScreenHeight() - PILLAR_GAP);
    pillar->color = DARKGREEN;
    pillar->speed = 3;
    pillar->speed_increment = 0.005f;

}

// ************************************
// MAIN LOOP
// ************************************
int main(void)
{
    const int screenWidth = 400;
    const int screenHeight = 600;
    const char screenTitle[] = "Flappy Bird";
    const Color screenBackground = SKYBLUE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Player player;

    init_player(&player);

    while (!WindowShouldClose())
    {
        update_player(&player);

        BeginDrawing();
        ClearBackground(screenBackground);

        draw_player(&player);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}