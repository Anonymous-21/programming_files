#include "raylib.h"
#include "raymath.h"

#define NUM_OF_BALLS 200

typedef struct Ball
{
    float x;
    float y;
    float radius;
    Vector2 direction;
    float speed;
    Color color;

} Ball;

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Bouncing Ball";
    const Color screenBackground = SKYBLUE;

    InitWindow(screenWidth, screenHeight, screenTitle);

    Ball balls[NUM_OF_BALLS] = {0};

    for (int i = 0; i < NUM_OF_BALLS; i++)
    {
        Ball ball;
        ball.radius = GetRandomValue(5, 30);
        ball.x = GetRandomValue(ball.radius, GetScreenWidth() - ball.radius);
        ball.y = GetRandomValue(ball.radius, GetScreenHeight() - ball.radius);
        ball.direction.x = GetRandomValue(0, 1) == 0 ? -1 : 1;
        ball.direction.y = GetRandomValue(0, 1) == 0 ? -1 : 1;
        ball.speed = GetRandomValue(100, 300);
        ball.color = (Color){
            GetRandomValue(0, 255),
            GetRandomValue(0, 255),
            GetRandomValue(0, 255),
            255};

        balls[i] = ball;
    }

    while (!WindowShouldClose())
    {
        for (int i = 0; i < NUM_OF_BALLS; i++)
        {
            balls[i].x += balls[i].direction.x * balls[i].speed * GetFrameTime();
            balls[i].y += balls[i].direction.y * balls[i].speed * GetFrameTime();

            if (balls[i].x < balls[i].radius || balls[i].x > GetScreenWidth() - balls[i].radius)
            {
                balls[i].direction.x *= -1;
            }
            else if (balls[i].y < balls[i].radius || balls[i].y > GetScreenHeight() - balls[i].radius)
            {
                balls[i].direction.y *= -1;
            }

            balls[i].direction = Vector2Normalize(balls[i].direction);
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        for (int i = 0; i < NUM_OF_BALLS; i++)
        {
            DrawCircleV((Vector2){balls[i].x, balls[i].y}, balls[i].radius, balls[i].color);
        }

        EndDrawing();
    }

    CloseWindow();

    return 0;
}