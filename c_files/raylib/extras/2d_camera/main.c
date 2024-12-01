#include "raylib.h"

double min(double x, double y) { return (x < y) ? x : y; }

double max(double x, double y) { return (x > y) ? x : y; }

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "2D Camera";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Texture2D background =
        LoadTexture("/home/anonymous/Downloads/programming_files/c_files/raylib/"
                    "extras/2d_camera/background.png");

    Rectangle player = (Rectangle){(double)GetScreenWidth() / 2 - 30,
                                   (double)GetScreenHeight() / 2 - 30, 30, 30};
    Color player_color = WHITE;
    double player_speed = 8;

    Camera2D camera = {0};
    camera.offset =
        (Vector2){(double)GetScreenWidth() / 2, (double)GetScreenHeight() / 2};
    camera.target =
        (Vector2){player.x - player.width / 2, player.y - player.height / 2};
    camera.rotation = 0.0f;
    camera.zoom = 1.0f;

    while (!WindowShouldClose())
    {
        // player movement
        if (IsKeyDown(KEY_LEFT) && player.x >= 0)
        {
            player.x -= player_speed;
        }
        else if (IsKeyDown(KEY_RIGHT) &&
                 player.x <= background.width - player.width)
        {
            player.x += player_speed;
        }
        else if (IsKeyDown(KEY_UP) && player.y >= 0)
        {
            player.y -= player_speed;
        }
        else if (IsKeyDown(KEY_DOWN) &&
                 player.y <= background.height - player.height)
        {
            player.y += player_speed;
        }

        // update camera target - player_position
        camera.target =
            (Vector2){player.x - player.width / 2, player.y - player.height / 2};

        // camera bounds
        camera.target.x =
            max((double)GetScreenWidth() / 2,
                min(player.x, background.width - (double)GetScreenWidth() / 2));
        camera.target.y =
            max((double)GetScreenHeight() / 2,
                min(player.y, background.height - (double)GetScreenHeight() / 2));

        BeginDrawing();
        ClearBackground(screenBackground);
        BeginMode2D(camera);

        DrawTexture(background, 0, 0, WHITE);
        DrawRectangleRec(player, player_color);

        EndMode2D();
        EndDrawing();
    }

    CloseWindow();

    return 0;
}