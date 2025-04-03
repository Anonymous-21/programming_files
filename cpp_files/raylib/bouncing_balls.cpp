#include "raylib.h"
#include "raymath.h"
#include <vector>

#define NUMBER_OF_BALLS 200

Color get_color(int num)
{
    Color color;

    switch (num)
    {
    case 1:
        color = LIGHTGRAY;
        break;
    case 2:
        color = GRAY;
        break;
    case 3:
        color = DARKGRAY;
        break;
    case 4:
        color = YELLOW;
        break;
    case 5:
        color = GOLD;
        break;
    case 6:
        color = ORANGE;
        break;
    case 7:
        color = PINK;
        break;
    case 8:
        color = RED;
        break;
    case 9:
        color = MAROON;
        break;
    case 10:
        color = GREEN;
        break;
    case 11:
        color = LIME;
        break;
    case 12:
        color = DARKGREEN;
        break;
    case 13:
        color = SKYBLUE;
        break;
    case 14:
        color = BLUE;
        break;
    case 15:
        color = DARKBLUE;
        break;
    case 16:
        color = PURPLE;
        break;
    case 17:
        color = VIOLET;
        break;
    case 18:
        color = DARKPURPLE;
        break;
    case 19:
        color = BEIGE;
        break;
    case 20:
        color = BROWN;
        break;
    case 21:
        color = DARKBROWN;
        break;
    case 22:
        color = WHITE;
        break;
    case 23:
        color = BLACK;
        break;
    case 24:
        color = BLANK;
        break;
    case 25:
        color = MAGENTA;
        break;
    case 26:
        color = RAYWHITE;
        break;
    }

    return color;
}

class Ball
{
public:
    float x;
    float y;
    float radius;
    Vector2 direction;
    Vector2 velocity;
    Color color;

    void init()
    {
        radius = GetRandomValue(2, 30);
        float padding = 10.0f;
        x = GetRandomValue(radius + padding, GetScreenWidth() - radius - padding);
        y = GetRandomValue(radius + padding, GetScreenHeight() - radius - padding);
        color = get_color(GetRandomValue(1, 26));

        float speed = GetRandomValue(100, 500);
        float angle = GetRandomValue(0, 360) * DEG2RAD;
        velocity.x = cosf(angle) * speed;
        velocity.y = sinf(angle) * speed;
    }

    void draw()
    {
        DrawCircleV((Vector2){x, y}, radius, color);
    }

    void update()
    {
        // move ball
        x += velocity.x * GetFrameTime();
        y += velocity.y * GetFrameTime();

        // ball bounds
        if (x < radius || x > GetScreenWidth() - radius)
        {
            velocity.x *= -1;
        }
        else if (y < radius || y > GetScreenHeight() - radius)
        {
            velocity.y *= -1;
        }

        // normalize direction vector
        direction = Vector2Normalize(direction);
    }
};

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "";
    const Color SCREEN_BACKGROUND = SKYBLUE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    std::vector<Ball> ball_list;

    for (int i = 0; i < NUMBER_OF_BALLS; i++)
    {
        Ball ball;
        ball.init();
        ball_list.push_back(ball);
    }

    while (!WindowShouldClose())
    {
        for (int i = 0; i < NUMBER_OF_BALLS; i++)
        {
            ball_list[i].update();
        }

        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        for (int i = 0; i < NUMBER_OF_BALLS; i++)
        {
            ball_list[i].draw();
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
