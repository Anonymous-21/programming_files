#include "raylib.h"

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "";
    const Color SCREEN_BACKGROUND = RAYWHITE;
    const int GAME_FPS = 60;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
    // SetTargetFPS(GAME_FPS);

    Rectangle rect = (Rectangle){200, GetScreenHeight() - 100, 20, 100};
    Color color = BLUE;
    float change_y = 0.0f;
    float gravity = 150.0f;
    float jump_strength = -200.0f;
    bool jumping = false;

    while (!WindowShouldClose())
    {
        if (IsKeyPressed(KEY_UP))
        {
            change_y = jump_strength;
            jumping = true;
        }

        if (jumping)
        {
            change_y += gravity * GetFrameTime();
            rect.y += change_y * GetFrameTime();

            if (rect.y >= GetScreenHeight() - rect.height)
            {
                rect.y = GetScreenHeight() - rect.height;
                jumping = false;
                change_y = 0.0f;
            }
        }

        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        DrawRectangleRec(rect, color);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}