#include <stdio.h>
#include "raylib.h"

int main(void)
{
    InitWindow(800, 600, "basic window");
    SetTargetFPS(60);

    while (!WindowShouldClose())
    {
        BeginDrawing();
            ClearBackground(RAYWHITE);
        EndDrawing();
    }

    CloseWindow();
}