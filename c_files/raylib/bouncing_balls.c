#include "raylib.h"
#include "raymath.h"

#define NUMBER_OF_BALLS 200

Color get_color(int num)
{
    Color color;

    switch (num)
    {
        case 1: color = LIGHTGRAY; break;
        case 2: color = GRAY; break;
        case 3: color = DARKGRAY; break;
        case 4: color = YELLOW; break;
        case 5: color = GOLD; break;
        case 6: color = ORANGE; break;
        case 7: color = PINK; break;
        case 8: color = RED; break;
        case 9: color = MAROON; break;
        case 10: color = GREEN; break;
        case 11: color = LIME; break;
        case 12: color = DARKGREEN; break;
        case 13: color = SKYBLUE; break;
        case 14: color = BLUE; break;
        case 15: color = DARKBLUE; break;
        case 16: color = PURPLE; break;
        case 17: color = VIOLET; break;
        case 18: color = DARKPURPLE; break;
        case 19: color = BEIGE; break;
        case 20: color = BROWN; break;
        case 21: color = DARKBROWN; break;
        case 22: color = WHITE; break;
        case 23: color = BLACK; break;
        case 24: color = BLANK; break;
        case 25: color = MAGENTA; break;
        case 26: color = RAYWHITE; break;
        default: color = WHITE; break;
    }

    return color;
}

typedef struct Ball
{
    Vector2 position;
    Vector2 velocity;
    int radius;
    Color color;
} Ball;

void ball_init(Ball *ball, int screenWidth, int screenHeight)
{
    ball->radius = GetRandomValue(5, 30);
    
    // Ensure balls spawn away from edges
    ball->position.x = GetRandomValue(ball->radius + 10, screenWidth - ball->radius - 10);
    ball->position.y = GetRandomValue(ball->radius + 10, screenHeight - ball->radius - 10);
    
    // Generate random direction with minimum speed
    float speed = GetRandomValue(100, 500);
    float angle = GetRandomValue(0, 360) * DEG2RAD;
    ball->velocity.x = cosf(angle) * speed;
    ball->velocity.y = sinf(angle) * speed;
    
    ball->color = get_color(GetRandomValue(1, 26));
}

void ball_update(Ball *ball, int screenWidth, int screenHeight)
{
    // Move ball
    ball->position.x += ball->velocity.x * GetFrameTime();
    ball->position.y += ball->velocity.y * GetFrameTime();

    // Bounce off edges
    if (ball->position.x < ball->radius)
    {
        ball->velocity.x *= -1;
    }
    else if (ball->position.x > screenWidth - ball->radius)
    {
        ball->velocity.x *= -1;
    }

    if (ball->position.y < ball->radius)
    {
        ball->velocity.y *= -1;
    }
    else if (ball->position.y > screenHeight - ball->radius)
    {
        ball->velocity.y *= -1;
    }
}

void ball_draw(Ball *ball)
{
    DrawCircleV(ball->position, ball->radius, ball->color);
}

typedef struct Balls
{
    Ball list[NUMBER_OF_BALLS];
} Balls;

void balls_init(Balls *balls, int screenWidth, int screenHeight)
{
    for (int i = 0; i < NUMBER_OF_BALLS; i++)
    {
        ball_init(&balls->list[i], screenWidth, screenHeight);
    }
}

void balls_update(Balls *balls, int screenWidth, int screenHeight)
{
    for (int i = 0; i < NUMBER_OF_BALLS; i++)
    {
        ball_update(&balls->list[i], screenWidth, screenHeight);
    }
}

void balls_draw(Balls *balls)
{
    for (int i = 0; i < NUMBER_OF_BALLS; i++)
    {
        ball_draw(&balls->list[i]);
    }
}

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 600;
    const char SCREEN_TITLE[] = "Bouncing Balls";
    const Color SCREEN_BACKGROUND = SKYBLUE;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    Balls balls;
    balls_init(&balls, SCREEN_WIDTH, SCREEN_HEIGHT);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        balls_update(&balls, SCREEN_WIDTH, SCREEN_HEIGHT);
        balls_draw(&balls);

        EndDrawing();
    }

    CloseWindow();
    return 0;
}