// TODO: CORRENT SNAKE BODY PART INITIALIZATION AFTER EATING

#include <stdio.h>
#include "raylib.h"

#define ROWS 20
#define COLS 20
#define BLOCK_SIZE 30
#define MARGIN 100

#define SCORE_LENGTH 10

//********************************
// Snake
//********************************

typedef enum Direction
{
    RIGHT,
    LEFT,
    UP,
    DOWN

} Direction;

typedef struct Snake
{
    int x;
    int y;
    Direction direction;
    Vector2 list[ROWS * COLS];
    int size;

    float last_current_time;
    float move_interval;

} Snake;

void snake_init(Snake *snake)
{
    snake->x = MARGIN;
    snake->y = MARGIN;
    snake->size = 1;
    snake->direction = RIGHT;
    snake->list[0] = (Vector2){snake->x, snake->y};

    snake->last_current_time = 0.0f;
    snake->move_interval = 0.07f;
}

void snake_draw(Snake *snake)
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

void snake_update(Snake *snake)
{
    // get direction input
    if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT)
    {
        snake->direction = RIGHT;
    }
    else if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT)
    {
        snake->direction = LEFT;
    }
    else if (IsKeyPressed(KEY_DOWN) && snake->direction != UP)
    {
        snake->direction = DOWN;
    }
    else if (IsKeyPressed(KEY_UP) && snake->direction != DOWN)
    {
        snake->direction = UP;
    }

    // move snake
    float current_time = GetTime();
    if (current_time - snake->last_current_time > snake->move_interval)
    {
        snake->last_current_time = current_time;

        for (int i = snake->size - 1; i >= 1; i--)
        {
            snake->list[i] = snake->list[i - 1];
        }

        switch (snake->direction)
        {
        case RIGHT:
            snake->x += BLOCK_SIZE;
            break;
        case LEFT:
            snake->x -= BLOCK_SIZE;
            break;
        case DOWN:
            snake->y += BLOCK_SIZE;
            break;
        case UP:
            snake->y -= BLOCK_SIZE;
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
        if (snake->y < MARGIN)
        {
            snake->y = GetScreenHeight() - MARGIN - BLOCK_SIZE;
        }
        else if (snake->y > GetScreenHeight() - MARGIN - BLOCK_SIZE)
        {
            snake->y = MARGIN;
        }

        // update snake list
        snake->list[0] = (Vector2){snake->x, snake->y};
    }
}

//********************************
// Food
//********************************

typedef struct Food
{
    int x;
    int y;
    Color color;

} Food;

void gen_random_food(Food *food, Snake *snake)
{
    int x;
    int y;
    while (1)
    {
        x = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;
        y = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;

        bool collision = false;

        for (int i = 0; i < snake->size; i++)
        {
            if (x == snake->list[i].x && y == snake->list[i].y)
            {
                collision = true;
                break;
            }
        }

        if (!collision)
        {
            break;
        }
    }

    food->x = x;
    food->y = y;
}

void food_init(Food *food, Snake *snake)
{
    gen_random_food(food, snake);
    food->color = RED;
}

void food_draw(Food *food)
{
    DrawRectangle(food->x, food->y, BLOCK_SIZE, BLOCK_SIZE, food->color);
}

//********************************
// Game
//********************************

typedef struct Game
{
    int score;
    char score_str[SCORE_LENGTH];
    bool game_over;
    bool game_won;

    Snake snake;
    Food food;

} Game;

void game_init(Game *game)
{
    game->score = 0;
    game->game_over = false;
    game->game_won = false;

    snake_init(&game->snake);
    food_init(&game->food, &game->snake);
}

void draw_grid()
{
    DrawRectangleLinesEx((Rectangle){MARGIN,
                                     MARGIN,
                                     GetScreenWidth() - (MARGIN * 2),
                                     GetScreenHeight() - (MARGIN * 2)},
                         5,
                         BLACK);

    // vertical lines
    for (int x = MARGIN; x < GetScreenWidth() - MARGIN; x += BLOCK_SIZE)
    {
        DrawLineEx((Vector2){x, MARGIN}, (Vector2){x, GetScreenHeight() - MARGIN}, 2, BLACK);
    }
    // horizontal lines
    for (int y = MARGIN; y < GetScreenHeight() - MARGIN; y += BLOCK_SIZE)
    {
        DrawLineEx((Vector2){MARGIN, y}, (Vector2){GetScreenWidth() - MARGIN, y}, 2, BLACK);
    }

    // for (int i = 0; i < ROWS; i++)
    // {
    //     for (int j = 0; j < COLS; j++)
    //     {
    //         int x = j * BLOCK_SIZE + MARGIN;
    //         int y = i * BLOCK_SIZE + MARGIN;

    //         DrawRectangleLines(x, y, BLOCK_SIZE, BLOCK_SIZE, BLACK);
    //     }
    // }
}

void game_draw(Game *game)
{
    // draw lives
    DrawText(game->score_str, GetScreenWidth() / 2 - 10, 30, 40, BLACK);

    if (game->game_over)
    {
        DrawText(
            "GAME OVER",
            GetScreenWidth() / 2 - 100,
            GetScreenHeight() / 2,
            40,
            BLACK);
        DrawText(
            "Press ENTER to restart",
            GetScreenWidth() / 2 - 170,
            GetScreenHeight() / 2 + 100,
            30,
            BLACK);
    }
    if (game->game_won)
    {
        DrawText("GAME WON",
                 GetScreenWidth() / 2 - 100,
                 GetScreenHeight() / 2,
                 40,
                 BLACK);
        DrawText(
            "Press ENTER to restart",
            GetScreenWidth() / 2 - 170,
            GetScreenHeight() / 2 + 100,
            30,
            BLACK);
    }

    draw_grid();

    if (!game->game_over && !game->game_won)
    {
        snake_draw(&game->snake);
        food_draw(&game->food);
    }
}

void game_update(Game *game)
{
    if (!game->game_over && !game->game_won)
    {
        // convert score to string
        snprintf(game->score_str, SCORE_LENGTH, "%d", game->score);

        // snake eats food
        if (CheckCollisionRecs((Rectangle){game->snake.list[0].x,
                                           game->snake.list[0].y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE},
                               (Rectangle){game->food.x,
                                           game->food.y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE}))
        {
            game->snake.size += 1;
            game->score += 1;
            gen_random_food(&game->food, &game->snake);
        }

        snake_update(&game->snake);

        // snake collision itself
        for (int i = 1; i < game->snake.size; i++)
        {
            if (CheckCollisionRecs((Rectangle){game->snake.list[0].x,
                                               game->snake.list[0].y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE},
                                   (Rectangle){game->snake.list[i].x,
                                               game->snake.list[i].y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE}))
            {
                game->game_over = true;
            }
        }

        // game win condition
        if (game->snake.size >= (ROWS * COLS))
        {
            game->game_won = true;
        }
    }
    else
    {
        if (IsKeyPressed(KEY_ENTER))
        {
            game->score = 0;
            game->game_over = false;
            game->game_won = false;

            snake_init(&game->snake);
            food_init(&game->food, &game->snake);
        }
    }
}

//********************************
// Main
//********************************

int main(void)
{
    const int SCREEN_WIDTH = 800;
    const int SCREEN_HEIGHT = 800;
    const char SCREEN_TITLE[] = "Snake";
    const Color SCREEN_BACKGROUND = LIGHTGRAY;

    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

    Game game;

    game_init(&game);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        game_draw(&game);
        game_update(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}