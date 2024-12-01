#include "raylib.h"

#include "player.h"
#include "bullet.h"
#include "bullet_list.h"

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Shooting Test";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Player player;
    BulletList bullet_list;

    initPlayer(&player);
    initBulletList(&bullet_list);

    while (!WindowShouldClose())
    {
        updateBulletList(&bullet_list, &player);

        BeginDrawing();
        ClearBackground(screenBackground);

        drawBulletList(&bullet_list);
        drawPlayer(&player);

        EndDrawing();
    }

    freeBulletList(&bullet_list);
    CloseWindow();

    return 0;
}