#include "raylib.h"

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Blinking Text";
    const Color SCREEN_BACKGROUND = RAYWHITE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    bool show_text = false;
    float last_current_time = 0.0f;

    while (!WindowShouldClose())
    {
        float current_time = GetTime();
        if (current_time - last_current_time > 1)
        {
            show_text = !show_text;
            last_current_time = current_time;
        }

        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        if (show_text)
        {
            DrawText("TEST", GetScreenWidth() / 2, GetScreenHeight() / 2, 40, BLACK);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}