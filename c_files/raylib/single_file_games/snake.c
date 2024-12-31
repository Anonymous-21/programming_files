#include "raylib.h"
#include <stdio.h>

#define ROWS 20
#define COLS 20
#define BLOCK_SIZE 30
#define MARGIN 100
#define SCORE_STR_LENGTH 10

// **************************************
// SNAKE
// **************************************

typedef enum Direction
{
    RIGHT,
    LEFT,
    UP,
    DOWN,

} Direction;

typedef struct Snake
{
    int x;
    int y;
    Direction direction;
    Vector2 list[ROWS * COLS];
    int size;

    // float last_current_time;
    // float move_interval;
    int frames_counter;

} Snake;

void init_snake(Snake *snake)
{
    snake->x = MARGIN;
    snake->y = MARGIN;
    snake->direction = RIGHT;
    snake->list[0] = (Vector2){snake->x, snake->y};
    snake->size = 1;

    snake->frames_counter = 0;
}

void draw_snake(Snake *snake)
{
    for (int i = 0; i < snake->size; i++)
    {
        Color color = (i == 0) ? BLUE : SKYBLUE;

        DrawRectangleRec((Rectangle){snake->list[i].x,
                                     snake->list[i].y,
                                     BLOCK_SIZE,
                                     BLOCK_SIZE},
                         color);
    }
}

void update_snake(Snake *snake)
{
    // get direction
    if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT)
    {
        snake->direction = LEFT;
    }
    else if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT)
    {
        snake->direction = RIGHT;
    }
    else if (IsKeyPressed(KEY_UP) && snake->direction != DOWN)
    {
        snake->direction = UP;
    }
    else if (IsKeyPressed(KEY_DOWN) && snake->direction != UP)
    {
        snake->direction = DOWN;
    }

    snake->frames_counter++;
    if (snake->frames_counter % 3 == 0)
    { 
        // move according to direction
        switch (snake->direction)
        {
        case RIGHT:
            snake->x += BLOCK_SIZE;
            break;
        case LEFT:
            snake->x -= BLOCK_SIZE;
            break;
        case UP:
            snake->y -= BLOCK_SIZE;
            break;
        case DOWN:
            snake->y += BLOCK_SIZE;
            break;
        }

        // snake bounds
        if (snake->x < MARGIN)
        {
            snake->x = GetScreenWidth() - MARGIN - BLOCK_SIZE;
        }
        else if (snake->x > GetScreenWidth() - MARGIN - BLOCK_SIZE)
        {
            snake->x = MARGIN;
        }
        else if (snake->y < MARGIN)
        {
            snake->y = GetScreenHeight() - MARGIN - BLOCK_SIZE;
        }
        else if (snake->y > GetScreenHeight() - MARGIN - BLOCK_SIZE)
        {
            snake->y = MARGIN;
        }

        // update snake list - move every block to right except head
        for (int i = snake->size - 1; i > 0; i--)
        {
            snake->list[i] = snake->list[i - 1];
        }

        // update snake head
        snake->list[0] = (Vector2){snake->x, snake->y};
    }
}

// **************************************
// GRID FUNCTION
// **************************************

void draw_grid()
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            int x = j * BLOCK_SIZE + MARGIN;
            int y = i * BLOCK_SIZE + MARGIN;

            DrawRectangleLinesEx((Rectangle){x, y, BLOCK_SIZE, BLOCK_SIZE}, 1, BLACK);
        }
    }
}

// **************************************
// MAIN LOOP
// **************************************

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 800;
    const char screenTitle[] = "Snake";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    int score = 0;
    char score_str[SCORE_STR_LENGTH];
    bool game_over = false;

    Snake snake;

    init_snake(&snake);

    while (!WindowShouldClose())
    {
        if (!game_over)
        {
            // convert score to string
            snprintf(score_str, SCORE_STR_LENGTH, "%d\n", score);

            update_snake(&snake);
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        draw_grid();
        draw_snake(&snake);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
