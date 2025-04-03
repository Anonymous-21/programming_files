#include "raylib.h"
#include "utils.h"
#include <stdio.h>

#define SCORE_LENGTH 10
#define PILLARS_LENGTH 20

#define VERTICAL_GAP 150
#define HORIZONTAL_GAP 250

// ***********************************
// PLAYER
// ***********************************

typedef struct Player
{
    Rectangle rect;
    Color color;
    float change_y;
    float gravity;
    float jump_strength;

} Player;

void player_init(Player *player)
{
    player->rect = (Rectangle){150, 150, 40, 40};
    player->color = RED;
    player->change_y = 0.0f;
    player->gravity = 1.0f;
    player->jump_strength = -12.0f;
}

void player_draw(Player *player)
{
    DrawRectangleRec(player->rect, player->color);
}

void player_update(Player *player)
{
    if (IsKeyPressed(KEY_UP))
    {
        player->change_y = player->jump_strength;
    }

    player->change_y += player->gravity;
    player->rect.y += player->change_y;

    // player bounds
    player->rect.y = max_float(0.0f,
                               min_float(player->rect.y,
                                         GetScreenHeight() - player->rect.height));
}

// ***********************************
// PILLARS
// ***********************************

typedef struct Pillar
{
    Rectangle rect;
    Color color;
    float speed;
    bool scored;

} Pillar;

void pillar_init(Pillar *pillar)
{
    pillar->rect = (Rectangle){GetScreenWidth(),
                               0,
                               50,
                               GetRandomValue(0, GetScreenHeight() - VERTICAL_GAP)};
    pillar->color = DARKGREEN;
    pillar->speed = 300.0f;
    pillar->scored = false;
}

void pillar_draw(Pillar *pillar)
{
    // upper pillar
    DrawRectangleRec(pillar->rect, pillar->color);

    // lower pillar
    float lower_y = pillar->rect.height + VERTICAL_GAP;
    DrawRectangleRec((Rectangle){pillar->rect.x,
                                 lower_y,
                                 pillar->rect.width,
                                 GetScreenHeight() - lower_y},
                     pillar->color);
}

void pillar_update(Pillar *pillar)
{
    pillar->rect.x -= pillar->speed * GetFrameTime();
}

// PILLARS LIST

typedef struct Pillars
{
    Pillar list[PILLARS_LENGTH];
    int size;

} Pillars;

void pillars_init(Pillars *pillars)
{
    pillars->size = 0;
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
    // update pillar list
    if (pillars->size <= 0 ||
        (pillars->list[pillars->size - 1].rect.x +
         pillars->list[pillars->size - 1].rect.width +
         HORIZONTAL_GAP) <
            GetScreenWidth())
    {
        Pillar pillar;
        pillar_init(&pillar);
        pillars->list[pillars->size] = pillar;
        pillars->size += 1;
    }

    // move pillars
    for (int i = 0; i < pillars->size; i++)
    {
        pillar_update(&pillars->list[i]);

        // remove offscreen pillar
        if (pillars->list[i].rect.x + pillars->list[i].rect.width + HORIZONTAL_GAP < 0)
        {
            for (int j = i; j < pillars->size; j++)
            {
                pillars->list[j] = pillars->list[j + 1];
            }

            pillars->size -= 1;
        }
    }
}

// ***********************************
// GAME MANAGER
// ***********************************

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
    player_draw(&game->player);
    pillars_draw(&game->pillars);

    // draw score
    DrawText(game->score_str, 20, 20, 40, BLACK);

    if (game->game_over)
    {
        DrawText("GAME OVER",
                 GetScreenWidth() / 2 - 150,
                 GetScreenHeight() / 2 - 100,
                 60,
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
            if (game->player.rect.x >
                (game->pillars.list[i].rect.x + game->pillars.list[i].rect.width))
            {
                if (!game->pillars.list[i].scored)
                {
                    game->score += 1;
                    game->pillars.list[i].scored = true;
                }
            }

            if (CheckCollisionRecs(game->player.rect, game->pillars.list[i].rect))
            {
                game->game_over = true;
            }
            if (CheckCollisionRecs(game->player.rect,
                                   (Rectangle){game->pillars.list[i].rect.x,
                                               game->pillars.list[i].rect.height + VERTICAL_GAP,
                                               game->pillars.list[i].rect.width,
                                               GetScreenHeight() - game->pillars.list[i].rect.height - VERTICAL_GAP}))
            {
                game->game_over = true;
            }
        }

        // player falls down
        if (game->player.rect.y + game->player.rect.height >= GetScreenHeight())
        {
            game->game_over = true;
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

// ***********************************
// MAIN
// ***********************************

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Flappy Bird";
    const Color SCREEN_BACKGROUND = SKYBLUE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

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
