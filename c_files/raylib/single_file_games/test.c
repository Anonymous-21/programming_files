#include "raylib.h"
#include <stdlib.h>

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 200
#define SCREEN_TITLE "Runner"
#define GAME_FPS 60

int main(void)
{
    // Initialization
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
    SetTargetFPS(GAME_FPS);

    bool gameOver = false;
    int score = 0;

    Rectangle rect = {10, GetScreenHeight() - 30, 20, 30};
    Color rectColor = RED;
    int gravity = 1;
    int jumpForce = -15;
    int changeY = 0;
    bool jumping = false;

    Rectangle pillars[100];
    int pillarCount = 0;
    int pillarWidth = 20;
    float pillarX = GetScreenWidth();
    Color pillarColor = DARKGREEN;
    int currentPillarGap = rand() % (200 - 100 + 1) + 100;

    int pillarSpeed = 2;

    // Main game loop
    while (!WindowShouldClose())
    {
        if (!gameOver)
        {
            if (pillarCount <= 0 || pillars[pillarCount - 1].x < GetScreenWidth() - currentPillarGap)
            {
                int pillarHeight = rand() % (50 - 20 + 1) + 20;
                int pillarY = GetScreenHeight() - pillarHeight;

                pillars[pillarCount] = (Rectangle){pillarX, pillarY, pillarWidth, pillarHeight};
                pillarCount++;

                currentPillarGap = rand() % (200 - 100 + 1) + 100;
            }

            for (int i = 0; i < pillarCount; i++)
            {
                pillars[i].x -= pillarSpeed;

                if (rect.x == pillars[i].x + pillars[i].width)
                {
                    score++;
                }

                if (CheckCollisionRecs(rect, pillars[i]))
                {
                    gameOver = true;
                }

                if (pillars[i].x + pillars[i].width < 0)
                {
                    for (int j = i; j < pillarCount - 1; j++)
                    {
                        pillars[j] = pillars[j + 1];
                    }
                    pillarCount--;
                    i--;
                }
            }

            if (IsKeyPressed(KEY_UP) && !jumping)
            {
                changeY = jumpForce;
                jumping = true;
            }

            if (jumping)
            {
                changeY += gravity;
                rect.y += changeY;
            }

            if (rect.y >= GetScreenHeight() - rect.height)
            {
                jumping = false;
                changeY = 0;
                rect.y = GetScreenHeight() - rect.height;
            }
        }
        else
        {
            if (IsKeyPressed(KEY_ENTER))
            {
                score = 0;
                gameOver = false;
                pillarCount = 0;
            }
        }

        // Drawing
        BeginDrawing();
        ClearBackground(SKYBLUE);

        // Draw score
        DrawText(TextFormat("%d", score), 20, 10, 40, BLACK);

        DrawRectangleRec(rect, rectColor);

        for (int i = 0; i < pillarCount; i++)
        {
            DrawRectangleRec(pillars[i], pillarColor);
        }

        if (gameOver)
        {
            DrawText("GAME OVER", GetScreenWidth() / 2 - 100, GetScreenHeight() / 2, 40, BLACK);
        }

        EndDrawing();
    }

    // De-Initialization
    CloseWindow();

    return 0;
}
