#include "raylib.h"
#include <stdio.h>

#define PILLAR_GAP 200
#define NUMBER_OF_PILLARS 100
#define SCORE_STR_LENGTH 10

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

} Pillar;

void init_pillar(Pillar *pillar)
{
    pillar->x = GetScreenWidth();
    pillar->y = 0;
    pillar->width = 100;
    pillar->height = GetRandomValue(0, GetScreenHeight() - PILLAR_GAP);
    pillar->color = DARKGREEN;
    pillar->speed = 4;
}

void draw_pillar(Pillar *pillar)
{
    DrawRectangleRec((Rectangle){pillar->x,
                                 pillar->y,
                                 pillar->width,
                                 pillar->height},
                     pillar->color);
    DrawRectangleRec((Rectangle){pillar->x,
                                 pillar->y + pillar->height + PILLAR_GAP,
                                 pillar->width,
                                 GetScreenHeight() - pillar->height},
                     pillar->color);
}

void update_pillar(Pillar *pillar)
{
    pillar->x -= pillar->speed;
}

// ************************************
// PILLAR LIST
// ************************************
typedef struct PillarList
{
    Pillar list[NUMBER_OF_PILLARS];
    int size;

} PillarList;

void init_pillar_list(PillarList *pillar_list)
{
    pillar_list->size = 0;
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
        pillar_list->list[pillar_list->size - 1].x < 0)
    {
        Pillar pillar;
        init_pillar(&pillar);
        pillar_list->list[pillar_list->size] = pillar;
        pillar_list->size++;
    }

    for (int i = 0; i < pillar_list->size; i++)
    {
        update_pillar(&pillar_list->list[i]);

        for (int i = 0; i < pillar_list->size; i++)
        {
            if (pillar_list->list[i].x + pillar_list->list[i].width < 0)
            {
                pillar_list->size--;
                for (int j = i; j < pillar_list->size; j++)
                {
                    pillar_list->list[j] = pillar_list->list[j + 1];
                }
            }
        }
    }
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
            // convert to string
            snprintf(score_str, SCORE_STR_LENGTH, "%d\n", score);

            update_player(&player);
            update_pillar_list(&pillar_list);

            // player collision pillars
            for (int i = 0; i < pillar_list.size; i++)
            {
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
                if (CheckCollisionRecs((Rectangle){player.x,
                                                   player.y,
                                                   player.width,
                                                   player.height},
                                       (Rectangle){pillar_list.list[i].x,
                                                   pillar_list.list[i].y + pillar_list.list[i].height + PILLAR_GAP,
                                                   pillar_list.list[i].width,
                                                   GetScreenHeight() - pillar_list.list[i].height}))
                {
                    game_over = true;
                }

                // update scores
                if (player.x == pillar_list.list[i].x + pillar_list.list[i].width)
                {
                    score++;
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

        draw_player(&player);
        draw_pillar_list(&pillar_list);

        // draw score
        DrawText(score_str, GetScreenWidth() - 80, 20, 40, BLACK);

        // game over
        if (game_over)
        {
            DrawText("Game Over", GetScreenWidth() / 2 - 70, GetScreenHeight() / 2, 30, BLACK);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}