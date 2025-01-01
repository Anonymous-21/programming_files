#include "raylib.h"
#include <stdio.h>

#define NUMBER_OF_PILLARS 20
#define SCORE_STR_LENGTH 10

// ********************************************
// PLAYER
// ********************************************
typedef struct Player
{
    float x;
    float y;
    float width;
    float height;
    Color color;
    float gravity;
    float jump_force;
    float change_y;
    bool jumping;

} Player;

void init_player(Player *player)
{
    player->width = 15.0f;
    player->height = 40.0f;
    player->x = 20.0f;
    player->y = GetScreenHeight() - player->height;
    player->color = RED;
    player->gravity = 1.0f;
    player->jump_force = -15.0f;
    player->change_y = 0.0f;
    player->jumping = false;
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
    if (IsKeyPressed(KEY_UP) && !player->jumping)
    {
        player->change_y = player->jump_force;
        player->jumping = true;
    }
    if (player->jumping)
    {
        player->change_y += player->gravity;
        player->y += player->change_y;
    }

    if (player->y >= GetScreenHeight() - player->height)
    {
        player->jumping = false;
        player->change_y = 0;
        player->y = GetScreenHeight() - player->height;
    }
}

// ********************************************
// PILLAR
// ********************************************
typedef struct Pillar
{
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;
    float speed_increment;

} Pillar;

void init_pillar(Pillar *pillar)
{
    pillar->width = 20.0f;
    pillar->height = GetRandomValue(20, 50);
    pillar->x = GetScreenWidth();
    pillar->y = GetScreenHeight() - pillar->height;
    pillar->color = DARKGREEN;
    pillar->speed = 3.0f;
    pillar->speed_increment = 0.005f;
}

void draw_pillar(Pillar *pillar)
{
    DrawRectangleRec((Rectangle){pillar->x,
                                 pillar->y,
                                 pillar->width,
                                 pillar->height},
                     pillar->color);
}

void update_pillar(Pillar *pillar)
{
    pillar->x -= pillar->speed;
    pillar->speed -= pillar->speed_increment;
}

// ********************************************
// PILLAR LIST
// ********************************************
typedef struct PillarList
{
    Pillar list[NUMBER_OF_PILLARS];
    int size;
    float distance_between_pillars;

} PillarList;

void init_pillar_list(PillarList *pillar_list)
{
    pillar_list->size = 0;
    pillar_list->distance_between_pillars = GetRandomValue(100, 200);
}

void draw_pillar_list(PillarList *pillar_list)
{
    for (int i = 0; i < pillar_list->size; i++)
    {
        draw_pillar(&pillar_list->list[i]);
    }
}

void update_pillar_list(PillarList *pillar_list)
{
    if (pillar_list->size <= 0 ||
        GetScreenWidth() - pillar_list->list[pillar_list->size - 1].x > pillar_list->distance_between_pillars)
    {
        Pillar pillar;
        init_pillar(&pillar);
        pillar_list->list[pillar_list->size] = pillar;
        pillar_list->size++;
        pillar_list->distance_between_pillars = GetRandomValue(100, 200);
    }

    for (int i = 0; i < pillar_list->size; i++)
    {
        update_pillar(&pillar_list->list[i]);

        if (pillar_list->list[i].x + pillar_list->list[i].width < 0)
        {
            for (int j = i; j < pillar_list->size; j++)
            {
                pillar_list->list[j] = pillar_list->list[j + 1];
            }
            pillar_list->size--;
        }
    }
}

// ********************************************
// MAIN LOOP
// ********************************************
int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 200;
    const char screenTitle[] = "Endless Runner";
    const Color screenBackground = SKYBLUE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    int score = 0;
    char score_str[SCORE_STR_LENGTH];
    bool game_over = false;

    Player player;
    PillarList pillar_list;

    init_player(&player);
    init_pillar_list(&pillar_list);

    while (!WindowShouldClose())
    {
        if (!game_over)
        {
            // convert score to string
            snprintf(score_str, SCORE_STR_LENGTH, "%d\n", score);

            update_player(&player);
            update_pillar_list(&pillar_list);

            for (int i = 0; i < pillar_list.size; i++)
            {
                if (player.x == pillar_list.list[i].x + pillar_list.list[i].width)
                {
                    score++;
                }

                if (CheckCollisionRecs((Rectangle){player.x,
                                                   player.y,
                                                   player.width,
                                                   player.height},
                                       (Rectangle){pillar_list.list[i].x,
                                                   pillar_list.list[i].y,
                                                   pillar_list.list[i].width,
                                                   pillar_list.list[i].height}))
                {
                    game_over = true;
                }
            }
        }
        else
        {
            if (IsKeyPressed(KEY_ENTER))
            {
                score = 0;
                game_over = false;
                init_player(&player);
                init_pillar_list(&pillar_list);
            }
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        // game over
        if (game_over)
        {
            DrawText("Game Over", GetScreenWidth() / 2 - 70, 100, 30, BLACK);
        }

        // draw score
        DrawText(score_str, 10, 10, 40, BLACK);

        draw_player(&player);
        draw_pillar_list(&pillar_list);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
