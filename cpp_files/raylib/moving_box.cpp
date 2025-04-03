#include "raylib.h"
#include "raymath.h"
#include <algorithm>

class Box
{
public:
    Rectangle rect;
    Vector2 direction;
    float speed;
    Color color;

    void init()
    {
        rect = (Rectangle){200, 200, 40, 40};
        direction = (Vector2){0, 0};
        speed = 300.0f;
        color = BLUE;
    }

    void draw()
    {
        DrawRectangleRec(rect, color);
    }

    void update()
    {
        // get input
        direction.x = static_cast<int>(IsKeyDown(KEY_RIGHT)) - static_cast<int>(IsKeyDown(KEY_LEFT));
        direction.y = static_cast<int>(IsKeyDown(KEY_DOWN)) - static_cast<int>(IsKeyDown(KEY_UP));

        // normalize direction
        direction = Vector2Normalize(direction);

        // move box
        rect.x += direction.x * speed * GetFrameTime();
        rect.y += direction.y * speed * GetFrameTime();

        // box bounds
        rect.x = std::max(0.0f, std::min(rect.x, GetScreenWidth() - rect.width));
        rect.y = std::max(0.0f, std::min(rect.y, GetScreenHeight() - rect.height));
    }
};

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Moving Box";
    const Color SCREEN_BACKGROUND = RAYWHITE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    Box box;
    box.init();

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        box.draw();
        box.update();

        EndDrawing();
    }

    CloseWindow();

    return 0;
}