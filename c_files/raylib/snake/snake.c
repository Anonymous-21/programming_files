#include "raylib.h"
#include "snake.h"
#include "constants.h"
#include <stdlib.h>
#include <stdio.h>

void initSnake(Snake *snake)
{
    snake->x = MARGIN;
    snake->y = MARGIN;
    snake->color = BLUE;
    snake->frames_counter = 0;
    snake->direction = RIGHT;
    snake->snake_array.size = 1;
    snake->snake_array.capacity = 1;
    snake->snake_array.list = (Vector2 *)malloc(snake->snake_array.capacity * sizeof(Vector2));
    if (snake->snake_array.list == NULL)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }
    snake->snake_array.list[0] = (Vector2){snake->x, snake->y};
}

void drawSnake(Snake *snake)
{
    for (int i = 0; i < snake->snake_array.size; i++)
    {
        DrawRectangleRec(
            (Rectangle){
                snake->snake_array.list[i].x,
                snake->snake_array.list[i].y,
                BLOCK_SIZE,
                BLOCK_SIZE},
            snake->color);
    }
}

void updateSnakeList(Snake *snake)
{
    if (snake->snake_array.size >= snake->snake_array.capacity)
    {
        snake->snake_array.capacity *= 2;
        Vector2 *new_list = (Vector2 *)realloc(
            snake->snake_array.list,
            snake->snake_array.capacity * sizeof(Vector2));
        if (new_list == NULL)
        {
            printf("Memory not reallocated\n");
            exit(1);
        }
        snake->snake_array.list = new_list;
    }
}

void getDirection(Snake *snake)
{
    if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT)
    {
        snake->direction = RIGHT;
    }
    else if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT)
    {
        snake->direction = LEFT;
    }
    else if (IsKeyPressed(KEY_UP) && snake->direction != DOWN)
    {
        snake->direction = UP;
    }
    else if (IsKeyPressed(KEY_DOWN) && snake->direction != UP)
    {
        snake->direction = DOWN;
    }
}

void moveSnake(Snake *snake)
{
    snake->frames_counter++;
    if (snake->frames_counter % 5 == 0)
    {
        if (snake->snake_array.size > 1)
        {
            for (int i = snake->snake_array.size; i > 0; i--)
            {
                snake->snake_array.list[i] = snake->snake_array.list[i - 1];
            }
        }

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

        snake->snake_array.list[0] = (Vector2){snake->x, snake->y};
    }
}

void freeSnakeList(Snake *snake)
{
    free(snake->snake_array.list);
}