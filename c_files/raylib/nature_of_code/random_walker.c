#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    float width = 6.0f;
    float height = 6.0f;
    Color color = BLACK;

    Vector2 *list = malloc(sizeof(Vector2));
    if (list == NULL)
    {
        printf("Memory not allocated\n");
        return 1;
    }

    list[0] = (Vector2){(float)GetScreenWidth() / 2, (float)GetScreenHeight() / 2};
    int size = 1;

    while (!WindowShouldClose())
    {
        int choice = GetRandomValue(1, 4);
        Vector2 pos = list[size - 1];

        if (choice == 1)
        {
            pos.x += 6;
        }
        else if (choice == 2)
        {
            pos.x -= 6;
        }
        else if (choice == 3)
        {
            pos.y += 6;
        }
        else if (choice == 4)
        {
            pos.y -= 6;
        }

        if (pos.x <= 0)
        {
            pos.x = 0;
        }
        else if (pos.x >= GetScreenWidth() - width)
        {
            pos.x = GetScreenWidth() - width;
        }
        else if (pos.y <= 0)
        {
            pos.y = 0;
        }
        else if (pos.y >= GetScreenHeight() - height)
        {
            pos.y = GetScreenHeight() - height;
        }

        list = realloc(list, (size + 1) * sizeof(Vector2));
        if (list == NULL)
        {
            printf("Memory not reallocated\n");
            return 1;
        }
        list[size] = pos;
        size++;

        BeginDrawing();
        ClearBackground(screenBackground);

        for (int i = 0; i < size; i++)
        {
            DrawRectangleRec((Rectangle){list[i].x, list[i].y, width, height}, color);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
