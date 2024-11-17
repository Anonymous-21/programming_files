#include "collision_handler.h"
#include "raylib.h"
#include "snake.h"
#include "food.h"
#include "constants.h"

void snakeCollisionWalls(Snake *snake, bool *game_over)
{
  if (*game_over) return;

  if (snake->snake_array.list[0].x < MARGIN ||
      snake->snake_array.list[0].x > GetScreenWidth() - MARGIN - BLOCK_SIZE)
  {
    *game_over = true;
  }

  if (snake->snake_array.list[0].y < MARGIN ||
      snake->snake_array.list[0].y > GetScreenHeight() - MARGIN - BLOCK_SIZE)
  {
    *game_over = true;
  }
}

void snakeCollisionFood(Snake *snake, Food *food)
{
  if (CheckCollisionRecs(
          (Rectangle){
              snake->snake_array.list[0].x,
              snake->snake_array.list[0].y,
              BLOCK_SIZE,
              BLOCK_SIZE},

          (Rectangle){
              food->x,
              food->y,
              BLOCK_SIZE,
              BLOCK_SIZE}))
  {
    snake->snake_array.size++;
    Vector2 random_food = genRandomFood(snake);
    food->x = random_food.x;
    food->y = random_food.y;
  }
}

void snakeCollisionItself(Snake *snake, bool *game_over)
{
  if (*game_over) return;

  for (int i = 1; i < snake->snake_array.size; i++)
  {
    if (CheckCollisionRecs(
            (Rectangle){
                snake->snake_array.list[0].x,
                snake->snake_array.list[0].y,
                BLOCK_SIZE,
                BLOCK_SIZE},
            (Rectangle){
                snake->snake_array.list[i].x,
                snake->snake_array.list[i].y,
                BLOCK_SIZE,
                BLOCK_SIZE}))
    {
      *game_over = true;
    }
  }
}
