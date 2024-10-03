#include "raylib.h"
#include "paddle.h"

#define screenWidth 800
#define screenHeight 600
#define screenTitle "pong"
#define screenBackground RAYWHITE
#define gameFps 60

int main(void)
{
    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    while (!WindowShouldClose())
    {
        BeginDrawing();

            ClearBackground(screenBackground);

        EndDrawing();
    }

    CloseWindow();
}
