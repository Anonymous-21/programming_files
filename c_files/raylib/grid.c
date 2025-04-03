#include "raylib.h"

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "";
    const Color SCREEN_BACKGROUND = RAYWHITE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    int block_size = 40;

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        for (int x = 0; x < GetScreenWidth(); x += block_size)
        {
            DrawLineEx((Vector2){x, 0}, (Vector2){x, GetScreenHeight()}, 2, BLACK);
        }
        for (int y = 0; y < GetScreenHeight(); y += block_size)
        {
            DrawLineEx((Vector2){0, y}, (Vector2){GetScreenWidth(), y}, 2, BLACK);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}