#include <stdio.h>
#include <stdbool.h>
#include "raylib.h"

typedef struct grid
{
    int rows;
    int cols;
    int block_size;
    float line_thickness;
    Color color;
}grid;

typedef struct snake
{
    int x;
    int y;
    int width;
    int height;
    Color color;
}snake;

typedef struct food
{
    int x;
    int y;
    int width;
    int height;
    Color color;
}food;

// functions declaration (prototype)
void draw_grid(struct grid Grid);
int gen_random_food(struct food Food);

// functions
void draw_grid(struct grid Grid)
{
    for (int i = 0; i < Grid.rows; i++)
    {
        for (int j = 0; j < Grid.cols; j++)
        {
            int x = j * Grid.block_size;
            int y = i * Grid.block_size;

            DrawRectangleLinesEx((Rectangle){x, y, Grid.block_size, Grid.block_size}, Grid.line_thickness, Grid.color);
        }
    }
}

int gen_random_food(struct food Food)
{
    
}

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 800;
    const char screenTitle[] = "Snake";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    bool game_over = false;

    grid Grid;
    snake Snake;
    food Food;

    Grid.rows = 20;
    Grid.cols = 20;
    Grid.block_size = 40;
    Grid.line_thickness = 0.5;
    Grid.color = BLACK;
    
    Snake.width = Grid.block_size;
    Snake.height = Grid.block_size;
    Snake.x = 0;
    Snake.y = 0;
    Snake.color = BLUE;


    while (!WindowShouldClose())
    {
        BeginDrawing();

            ClearBackground(screenBackground);

            draw_grid(Grid);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
