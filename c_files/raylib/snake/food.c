#include "raylib.h"
#include "food.h"
#include "snake.h"
#include "constants.h"

void initFood(Food *food, Snake *snake)
{
    Vector2 random_food = genRandomFood(snake);
    food->x = random_food.x;
    food->y = random_food.y;
    food->color = RED;
}

Vector2 genRandomFood(Snake *snake)
{
    while (1)
    {
        int x = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;
        int y = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;

        for (int i = 0; i < snake->snake_array.size; i++)
        {
            if (x != snake->snake_array.list[i].x && y != snake->snake_array.list[i].y)
            {
                return (Vector2){x, y};
            }
        }
    }
}

void drawFood(Food *food)
{
    DrawRectangleRec(
        (Rectangle){
            food->x,
            food->y,
            BLOCK_SIZE,
            BLOCK_SIZE},
        food->color);
}