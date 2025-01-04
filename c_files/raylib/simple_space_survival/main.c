#include "raylib.h"

// ***********************************************
// MAIN LOOP
// ***********************************************
int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Simple Space Survival";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Texture2D background = LoadTexture("assets/background.png");

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(screenBackground);

        // draw background
        DrawTexture(background, 0, 0, WHITE);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}