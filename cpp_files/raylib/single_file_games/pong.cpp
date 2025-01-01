#include "raylib.h"
#include <cmath>
#include <string>

// **********************************
// BALL
// **********************************

class Ball
{
public:
    float initial_x;
    float initial_y;
    float x;
    float y;
    float radius;
    Color color;
    float initial_speed_x;
    float initial_speed_y;
    float speed_x;
    float speed_y;
    float speed_increment;
    bool active;

    Ball()
    {
        initial_x = static_cast<float>(GetScreenWidth()) / 2;
        initial_y = static_cast<float>(GetScreenHeight()) / 2;
        x = initial_x;
        y = initial_y;
        radius = 10.0f;
        color = RED;
        initial_speed_x = 4.0f;
        initial_speed_y = 4.0f;
        speed_x = initial_speed_x;
        speed_y = initial_speed_y;
        speed_increment = 0.005f;
        active = false;
    }

    void reset()
    {
        x = initial_x;
        y = initial_y;
        speed_x = initial_speed_x;
        speed_y = initial_speed_y;
        speed_x *= -1;
        active = false;
    }

    void draw() const
    {
        DrawCircleV(Vector2{x, y}, radius, color);
    }

    void update()
    {
        if (IsKeyPressed(KEY_SPACE))
        {
            active = true;
        }

        if (active)
        {
            x += speed_x;
            y += speed_y;

            // increment speed
            if (speed_x > 0)
            {
                speed_x += speed_increment;
            }
            else if (speed_x < 0)
            {
                speed_x -= speed_increment;
            }
            else if (speed_y > 0)
            {
                speed_y += speed_increment;
            }
            else if (speed_y > 0)
            {
                speed_y -= speed_increment;
            }
        }

        if (y <= radius || y >= GetScreenHeight() - radius)
        {
            speed_y *= -1;
        }
    }
};

// **********************************
// PADDLE
// **********************************

class Paddle
{
public:
    float initial_x;
    float initial_y;
    float x;
    float y;
    float width;
    float height;
    Color color;
    float speed;
    float ai_speed;

    Paddle(float x)
    {
        width = 10.0f;
        height = 100.0f;
        initial_x = x;
        initial_y = static_cast<float>(GetScreenHeight()) / 2 - height / 2;
        this->x = initial_x;
        this->y = initial_y;
        color = BLACK;
        speed = 5.0f;
        ai_speed = 7.0f;
    }

    void reset()
    {
        x = initial_x;
        y = initial_y;
    }

    void draw() const
    {
        DrawRectangleRec(Rectangle{x, y, width, height}, color);
    }

    void update_left()
    {
        if (IsKeyDown(KEY_W) && y >= 0)
        {
            y -= speed;
        }
        else if (IsKeyDown(KEY_S) && y <= GetScreenHeight() - height)
        {
            y += speed;
        }
    }

    void update_ai(Ball &ball)
    {
        if (ball.x > GetScreenWidth() / 2)
        {
            float distance_x = ball.x - (x + width / 2);
            float distance_y = ball.y - (y + height / 2);
            float distance = std::sqrt(std::pow(distance_x, 2) + std::pow(distance_y, 2));
            if (distance > 0)
            {
                distance_y /= distance;

                y += distance_y * ai_speed;
            }

            if (y <= 0)
            {
                y = 0;
            }
            else if (y >= GetScreenHeight() - height)
            {
                y = GetScreenHeight() - height;
            }
        }
    }
};

// **********************************
// GAME
// **********************************

class Game
{
public:
    int score_left;
    int score_right;

    Paddle paddle_left;
    Paddle paddle_ai;
    Ball ball;

    Game() : paddle_left(10),
             paddle_ai(GetScreenWidth() - paddle_left.width - 10),
             ball()
    {
        score_left = 0;
        score_right = 0;
    }

    void draw() const
    {
        // draw scores
        DrawText((std::to_string(score_left).c_str()), 200, 30, 40, BLACK);
        DrawText((std::to_string(score_right).c_str()), GetScreenWidth() - 220, 30, 40, BLACK);

        paddle_left.draw();
        paddle_ai.draw();
        ball.draw();
    }

    void update()
    {
        paddle_left.update_left();
        paddle_ai.update_ai(ball);
        ball.update();

        // ball collision paddle
        if (CheckCollisionCircleRec(Vector2{ball.x, ball.y},
                                    ball.radius,
                                    Rectangle{paddle_left.x,
                                              paddle_left.y,
                                              paddle_left.width,
                                              paddle_left.height}))
        {
            ball.speed_x *= -1;
        }
        else if (CheckCollisionCircleRec(Vector2{ball.x, ball.y},
                                         ball.radius,
                                         Rectangle{paddle_ai.x,
                                                   paddle_ai.y,
                                                   paddle_ai.width,
                                                   paddle_ai.height}))
        {
            ball.speed_x *= -1;
        }

        // update scores
        if (ball.x < 0)
        {
            score_right++;
            ball.reset();
            paddle_left.reset();
            paddle_ai.reset();
        }
        else if (ball.x > GetScreenWidth())
        {
            score_left++;
            ball.reset();
            paddle_left.reset();
            paddle_ai.reset();
        }
    }
};

// **********************************
// MAIN
// **********************************

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 600;
    const char screenTitle[] = "Pong";
    const Color screenBackground = SKYBLUE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Game game;

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(screenBackground);

        game.draw();
        game.update();

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
