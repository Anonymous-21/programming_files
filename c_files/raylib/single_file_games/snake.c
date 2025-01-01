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

        DrawRectangle(snake->list[i].x,
                      snake->list[i].y,
                      BLOCK_SIZE,
                      BLOCK_SIZE,
                      color);
    }
}

void get_direction_snake(Snake *snake)
{
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
}

void move_snake(Snake *snake)
{
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
}

void check_snake_bounds(Snake *snake)
{
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
}

void snake_collision_itself(Snake *snake, bool *game_over)
{
    for (int i = 1; i < snake->size; i++)
    {
        if (CheckCollisionRecs((Rectangle){snake->list[0].x,
                                           snake->list[0].y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE},
                               (Rectangle){snake->list[i].x,
                                           snake->list[i].y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE}))
        {
            *game_over = true;
        }
    }
}

void update_snake(Snake *snake, bool *game_over)
{
    get_direction_snake(snake);

    snake->frames_counter++;
    if (snake->frames_counter % 3 == 0)
    {
        // move according to direction
        move_snake(snake);

        // snake bounds
        check_snake_bounds(snake);

        // update snake list - move every block to right except head
        for (int i = snake->size - 1; i > 0; i--)
        {
            snake->list[i] = snake->list[i - 1];
        }

        // update snake head
        snake->list[0] = (Vector2){snake->x, snake->y};
    }

    snake_collision_itself(snake, game_over);
}

// **************************************
// FOOD
// **************************************

typedef struct Food
{
    int x;
    int y;
    Color color;

} Food;

void gen_random_food(Food *food, Snake *snake)
{
    bool value_in_list = false;
    while (1)
    {
        int x = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;
        int y = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;

        for (int i = 0; i < snake->size; i++)
        {
            if (x == snake->list[i].x && y == snake->list[i].y)
            {
                value_in_list = true;
                break;
            }
        }

        if (!value_in_list)
        {
            food->x = x;
            food->y = y;
            return;
        }
    }
}

void init_food(Food *food, Snake *snake)
{
    food->color = RED;
    gen_random_food(food, snake);
}

void draw_food(Food *food)
{
    DrawRectangle(food->x, food->y, BLOCK_SIZE, BLOCK_SIZE, food->color);
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
    Food food;

    init_snake(&snake);
    init_food(&food, &snake);

    while (!WindowShouldClose())
    {
        if (!game_over)
        {
            // convert score to string
            snprintf(score_str, SCORE_STR_LENGTH, "%d\n", score);

            update_snake(&snake, &game_over);

            // snake collision food
            if (CheckCollisionRecs((Rectangle){food.x,
                                               food.y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE},
                                   (Rectangle){snake.list[0].x,
                                               snake.list[0].y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE}))
            {
                snake.size++;
                score++;
                gen_random_food(&food, &snake);
            }
        }
        else
        {
            if (IsKeyPressed(KEY_ENTER))
            {
                score = 0;
                game_over = false;
                init_snake(&snake);
                init_food(&food, &snake);
            }
        }

        BeginDrawing();
        ClearBackground(screenBackground);

        if (game_over)
        {
            DrawText("Game Over",
                     GetScreenWidth() / 2 - 70,
                     GetScreenHeight() / 2 + 100,
                     30,
                     GRAY);
        }

        // draw score
        DrawText(score_str, GetScreenWidth() / 2 - 10, 30, 40, BLACK);

        draw_grid();
        draw_snake(&snake);
        draw_food(&food);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}
