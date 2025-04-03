#include "raylib.h"
#include "raymath.h"
#include "utils.h"

typedef struct Box
{
    float x;
    float y;
    float width;
    float height;
    float speed;
    Vector2 direction;
    Color color;

} Box;

void box_init(Box *box)
{
    box->width = 40.0f;
    box->height = box->width;
    box->x = (float)GetScreenWidth() / 2 - box->width / 2;
    box->y = (float)GetScreenHeight() / 2 - box->height / 2;
    box->speed = 300.0f;
    box->direction = (Vector2){0, 0};
    box->color = BLUE;
}

void box_draw(Box *box)
{
    DrawRectangleRec((Rectangle){box->x,
                                 box->y,
                                 box->width,
                                 box->height},
                     box->color);
}

void box_update(Box *box)
{
    // get keyboard input
    box->direction.x = (int)(IsKeyDown(KEY_D) || IsKeyDown(KEY_RIGHT)) -
                       (int)(IsKeyDown(KEY_A) || IsKeyDown(KEY_LEFT));
    box->direction.y = (int)(IsKeyDown(KEY_S) || IsKeyDown(KEY_DOWN)) -
                       (int)(IsKeyDown(KEY_W) || IsKeyDown(KEY_UP));

    // normalize direction vector
    box->direction = Vector2Normalize(box->direction);

    // move box
    box->x += box->direction.x * box->speed * GetFrameTime();
    box->y += box->direction.y * box->speed * GetFrameTime();

    // box bounds
    box->x = max_float(0.0f, min_float(box->x, GetScreenWidth() - box->width));
    box->y = max_float(0.0f, min_float(box->y, GetScreenHeight() - box->height));
}

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Moving Box";
    const Color SCREEN_BACKGROUND = RAYWHITE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    Box box;

    box_init(&box);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        box_draw(&box);
        box_update(&box);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}