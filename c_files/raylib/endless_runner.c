#include "raylib.h"
#include "utils.h"
#include <stdio.h>

#define PILLARS_LENGTH 20
#define SCORE_LENGTH 10

//***************************************
// PLAYER
//***************************************

typedef struct Player
{
    Rectangle rect;
    Color color;
    float gravity;
    float change_y;
    float jump_strength;
    bool jumping;

} Player;

void player_init(Player *player)
{
    player->rect = (Rectangle){80, GetScreenHeight() - 50, 15, 50};
    player->color = DARKGREEN;
    player->gravity = 1.0f;
    player->change_y = 0.0f;
    player->jump_strength = -12.0f;
    player->jumping = false;
}

void player_draw(Player *player)
{
    DrawRectangleRec(player->rect, player->color);
}

void player_update(Player *player)
{
    // enable jumping
    if (IsKeyPressed(KEY_UP) && !player->jumping)
    {
        player->change_y = player->jump_strength;
        player->jumping = true;
    }

    // move player
    if (player->jumping)
    {
        player->change_y += player->gravity;
        player->rect.y += player->change_y;

        if (player->rect.y > GetScreenHeight() - player->rect.height)
        {
            player->rect.y = GetScreenHeight() - player->rect.height;
            player->change_y = 0.0f;
            player->jumping = false;
        }
    }

    // player bounds
    player->rect.y = max_float(0.0f,
                               min_float(player->rect.y,
                                         GetScreenWidth() - player->rect.height));
}

//***************************************
// PILLARS
//***************************************

typedef struct Pillar
{
    Rectangle rect;
    Color color;
    float speed;
    bool scored;

} Pillar;

void pillar_init(Pillar *pillar)
{
    float random_height = GetRandomValue(30, 50);
    pillar->rect = (Rectangle){GetScreenWidth(),
                               GetScreenHeight() - random_height,
                               GetRandomValue(10, 30),
                               random_height};
    pillar->color = BLACK;
    pillar->speed = 5.0f;
    pillar->scored = false;
}

void pillar_draw(Pillar *pillar)
{
    DrawRectangleRec(pillar->rect, pillar->color);
}

void pillar_update(Pillar *pillar)
{
    pillar->rect.x -= pillar->speed;
}

// LIST OF PILLARS

typedef struct Pillars
{
    Pillar list[PILLARS_LENGTH];
    int size;
    float gap;

} Pillars;

void pillars_init(Pillars *pillars)
{
    pillars->size = 0;
    pillars->gap = GetRandomValue(150, 250);
}

void pillars_draw(Pillars *pillars)
{
    for (int i = 0; i < pillars->size; i++)
    {
        pillar_draw(&pillars->list[i]);
    }
}

void pillars_update(Pillars *pillars)
{
    // update pillars list
    if (pillars->size <= 0 ||
        pillars->list[pillars->size - 1].rect.x < GetScreenWidth() - pillars->gap)
    {
        Pillar pillar;
        pillar_init(&pillar);
        pillars->list[pillars->size] = pillar;
        pillars->size += 1;
        pillars->gap = GetRandomValue(150, 250);
    }

    // move pillars
    for (int i = 0; i < pillars->size; i++)
    {
        pillar_update(&pillars->list[i]);

        // remove pillar
        if (pillars->list[i].rect.x + pillars->list[i].rect.width < 0)
        {
            for (int j = i; j < pillars->size; j++)
            {
                pillars->list[j] = pillars->list[j + 1];
            }
            pillars->size -= 1;
        }
    }
}

//***************************************
// GAME MANAGER
//***************************************

typedef struct Game
{
    int score;
    char score_str[SCORE_LENGTH];
    bool game_over;

    Player player;
    Pillars pillars;

} Game;

void game_init(Game *game)
{
    game->score = 0;
    game->game_over = false;

    player_init(&game->player);
    pillars_init(&game->pillars);
}

void game_draw(Game *game)
{
    // draw score
    DrawText(game->score_str, 5, 5, 40, BLACK);

    player_draw(&game->player);
    pillars_draw(&game->pillars);

    if (game->game_over)
    {
        DrawText("GAME OVER",
                 GetScreenWidth() / 2 - 120,
                 GetScreenHeight() / 2 - 20,
                 40,
                 BLACK);
    }
}

void game_update(Game *game)
{
    if (!game->game_over)
    {
        // convert score to string
        snprintf(game->score_str, SCORE_LENGTH, "%d", game->score);

        player_update(&game->player);
        pillars_update(&game->pillars);

        for (int i = 0; i < game->pillars.size; i++)
        {
            // update score
            if (game->player.rect.x > (game->pillars.list[i].rect.x + game->pillars.list[i].rect.width))
            {
                if (!game->pillars.list[i].scored)
                {
                    game->score += 1;
                    game->pillars.list[i].scored = true;
                }
            }

            // check collision - player and pillars
            if (CheckCollisionRecs(game->player.rect, game->pillars.list[i].rect))
            {
                game->game_over = true;
            }
        }
    }
    else
    {
        if (IsKeyPressed(KEY_ENTER))
        {
            game->score = 0;
            game->game_over = false;

            player_init(&game->player);
            pillars_init(&game->pillars);
        }
    }
}

//***************************************
// MAIN
//***************************************

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 200;
    const char SCREEN_TITLE[] = "Endless Runner";
    const Color SCREEN_BACKGROUND = SKYBLUE;
    const int GAME_FPS = 60;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
    SetTargetFPS(GAME_FPS);

    Game game;
    game_init(&game);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        game_draw(&game);
        game_update(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}