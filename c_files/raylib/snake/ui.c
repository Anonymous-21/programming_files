#include "raylib.h"

#include "ui.h"
#include "constants.h"

void drawOutline()
{
    DrawRectangleLinesEx(
        (Rectangle){
            MARGIN - 5,
            MARGIN - 5,
            605,
            605},
        5,
        GRAY);
}

void drawMainMenu(bool highlight_play_button, bool highlight_quit_button)
{
    DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), SKYBLUE);
    DrawRectangleRec((Rectangle){(float)GetScreenWidth() / 2 - 70,
                                 (float)GetScreenHeight() / 2 - 100,
                                 150,
                                 50},
                     GRAY);
    DrawRectangleRec((Rectangle){(float)GetScreenWidth() / 2 - 70,
                                 (float)GetScreenHeight() / 2,
                                 150,
                                 50},
                     GRAY);
    DrawText("Play",
             (float)GetScreenWidth() / 2 - 35,
             (float)GetScreenHeight() / 2 - 95,
             40,
             BLACK);
    DrawText("Quit",
             (float)GetScreenWidth() / 2 - 35,
             (float)GetScreenHeight() / 2 + 5,
             40,
             BLACK);

    if (highlight_play_button)
    {
        DrawRectangleLinesEx((Rectangle){(float)GetScreenWidth() / 2 - 70,
                                         (float)GetScreenHeight() / 2 - 100,
                                         150,
                                         50},
                             8,
                             RED);
    }
    if (highlight_quit_button)
    {
        DrawRectangleLinesEx((Rectangle){(float)GetScreenWidth() / 2 - 70,
                                         (float)GetScreenHeight() / 2,
                                         150,
                                         50},
                             8,
                             RED);
    }
}

void drawScore(char score_str[SCORE_LENGTH])
{
    DrawText(score_str,
             (float)GetScreenWidth() / 2 - 80,
             30,
             40,
             GRAY);
}

void drawGameOverMenu()
{
    DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), SKYBLUE);
    DrawText("Game Over",
             (float)GetScreenWidth() / 2 - 90,
             (float)GetScreenHeight() / 2 - 100,
             40,
             BLACK);
    DrawText("Press 'Enter' to continue",
             (float)GetScreenWidth() / 2 - 170,
             (float)GetScreenHeight() / 2,
             30,
             BLACK);
}

void drawGameWonMenu()
{
    DrawRectangle(0, 0, GetScreenWidth(), GetScreenHeight(), SKYBLUE);
    DrawText("You Win",
             (float)GetScreenWidth() / 2 - 90,
             (float)GetScreenHeight() / 2 - 100,
             40,
             BLACK);
    DrawText("Press 'Enter' to continue",
             (float)GetScreenWidth() / 2 - 170,
             (float)GetScreenHeight() / 2,
             30,
             BLACK);
}