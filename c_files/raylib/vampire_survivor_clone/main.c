#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "player.h"
#include "bullet.h"
#include "bullet_list.h"
#include "enemy.h"
#include "enemy_list.h"
#include "collision_handler.h"

#define HEALTH_STR_LENGTH 10

int main(void)
{
    const int screenWidth = 1000;
    const int screenHeight = 800;
    const char screenTitle[] = "VS Clone";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    char player_health_str[HEALTH_STR_LENGTH];
    char player_max_health_str[HEALTH_STR_LENGTH];

    srand(time(NULL));

    Player player;
    BulletList bullet_list;
    EnemyList enemy_list;

    initPlayer(&player);
    initBulletList(&bullet_list);
    initEnemyList(&enemy_list);

    while (!WindowShouldClose())
    {
        // convert player health to string
        snprintf(player_health_str, HEALTH_STR_LENGTH, "%d\n", player.health);
        snprintf(player_max_health_str, HEALTH_STR_LENGTH, "%d\n", player.max_health);

        updatePlayer(&player);
        updateBulletList(&bullet_list, &player);
        updateEnemyList(&enemy_list, &player);

        playerCollisionEnemy(&enemy_list, &player);

        BeginDrawing();
        ClearBackground(screenBackground);

        // draw player health
        DrawText(player_health_str,
                 player.x - 100,
                 player.y - 100,
                 30,
                 GRAY);

        drawBulletList(&bullet_list);
        drawPlayer(&player);
        drawEnemyList(&enemy_list);

        EndDrawing();
    }

    freeMemoryBulletList(&bullet_list);
    CloseWindow();

    return 0;
}