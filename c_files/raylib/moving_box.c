#include "raylib.h"
#include "raymath.h"

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Test";
    const Color screenBackground = RAYWHITE;

    InitWindow(screenWidth, screenHeight, screenTitle);

    Rectangle rect = (Rectangle){GetScreenWidth() * 0.5f, GetScreenHeight() * 0.5f, 50, 50};
    Color color = BLUE;
    Vector2 direction = (Vector2){0, 0};
    float speed = 300.0f;

    while (!WindowShouldClose())
    {
        // get input and move rect
        direction.x = (int)IsKeyDown(KEY_RIGHT) - (int)IsKeyDown(KEY_LEFT);
        direction.y = (int)IsKeyDown(KEY_DOWN) - (int)IsKeyDown(KEY_UP);

        if (direction.x != 0 && direction.y != 0)
        {
            direction = Vector2Normalize(direction);
        }

        rect.x += direction.x * speed * GetFrameTime();
        rect.y += direction.y * speed * GetFrameTime();

        BeginDrawing();
        ClearBackground(screenBackground);

        DrawRectangleRec(rect, color);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}