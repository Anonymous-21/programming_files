#include "raylib.h"
#include <stdio.h>

#define ROWS 20
#define COLS 20
#define BLOCK_SIZE 30
#define MARGIN 100

#define SCORE_STR_LENGTH 15

/*
    SNAKE
*/
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
    Vector2 position[ROWS * COLS];
    int size;

    float last_current_time;
    float move_interval;

} Snake;

void initSnake(Snake *snake)
{
    snake->x = MARGIN;
    snake->y = MARGIN;
    snake->direction = RIGHT;
    snake->size = 1;
    snake->position[0] = (Vector2){snake->x, snake->y};

    snake->last_current_time = 0.0f;
    snake->move_interval = 0.05f;
}

void drawSnake(Snake *snake)
{
    Color color;
    for (int i = 0; i < snake->size; i++)
    {
        if (i == 0)
        {
            color = BLUE;
        }
        else
        {
            color = SKYBLUE;
        }

        DrawRectangleRec((Rectangle){snake->position[i].x,
                                     snake->position[i].y,
                                     BLOCK_SIZE,
                                     BLOCK_SIZE},
                         color);
    }
}

void getInput(Snake *snake)
{
    if (IsKeyDown(KEY_LEFT) && snake->direction != RIGHT)
    {
        snake->direction = LEFT;
    }
    else if (IsKeyDown(KEY_RIGHT) && snake->direction != LEFT)
    {
        snake->direction = RIGHT;
    }
    else if (IsKeyDown(KEY_UP) && snake->direction != DOWN)
    {
        snake->direction = UP;
    }
    else if (IsKeyDown(KEY_DOWN) && snake->direction != UP)
    {
        snake->direction = DOWN;
    }
}

void updateSnake(Snake *snake)
{
    getInput(snake);

    float current_time = GetTime();
    if (current_time - snake->last_current_time >= snake->move_interval)
    {
        // move snake based on direction
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

        // snake collision walls
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

        // update snake list
        if (snake->size > 0)
        {
            for (int i = snake->size - 1; i > 0; i--)
            {
                snake->position[i] = snake->position[i - 1];
            }
        }

        snake->position[0] = (Vector2){snake->x, snake->y};

        snake->last_current_time = current_time;
    }
}

/*
    FOOD
*/
typedef struct Food
{
    int x;
    int y;
    Color color;

} Food;

void genRandomFood(Food *food, Snake *snake)
{
    bool is_matched = false;
    while (1)
    {
        int x = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;
        int y = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;

        for (int i = 0; i < snake->size; i++)
        {
            if (x == snake->position[i].x && y == snake->position[i].y)
            {
                is_matched = true;
                break;
            }
        }

        if (!is_matched)
        {
            food->x = x;
            food->y = y;
            return;
        }
    }
}

void initFood(Food *food, Snake *snake)
{
    genRandomFood(food, snake);
    food->color = RED;
}

void drawFood(Food *food)
{
    DrawRectangle(food->x, food->y, BLOCK_SIZE, BLOCK_SIZE, food->color);
}

/*
    GAME
*/
typedef struct Game
{
    int score;
    char score_str[SCORE_STR_LENGTH];
    bool game_over;
    bool game_won;

    Snake snake;
    Food food;

} Game;

void initGame(Game *game)
{
    game->score = 0;
    game->game_over = false;
    game->game_won = false;

    initSnake(&game->snake);
    initFood(&game->food, &game->snake);
}

void drawGrid()
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

void drawGame(Game *game)
{
    if (game->game_over)
    {
        DrawText("GAME OVER",
                 GetScreenWidth() / 2 - 100,
                 GetScreenHeight() / 2,
                 40,
                 BLACK);
    }
    else if (game->game_won)
    {
        DrawText("YOU WIN",
                 GetScreenWidth() / 2 - 80,
                 GetScreenHeight() / 2,
                 40,
                 BLACK);
    }

    // draw score
    DrawText(game->score_str,
             GetScreenWidth() / 2 - 70,
             30,
             30,
             BLACK);

    drawGrid();
    drawSnake(&game->snake);
    drawFood(&game->food);
}

void updateGame(Game *game)
{
    if (game->snake.size >= ROWS * COLS)
    {
        game->game_won = true;
    }

    if (!game->game_over && !game->game_won)
    { // convert score to string
        snprintf(game->score_str, SCORE_STR_LENGTH, "Score: %d\n", game->score);

        updateSnake(&game->snake);

        // snake collision food
        if (CheckCollisionRecs((Rectangle){game->snake.position[0].x,
                                           game->snake.position[0].y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE},
                               (Rectangle){game->food.x,
                                           game->food.y,
                                           BLOCK_SIZE,
                                           BLOCK_SIZE}))
        {
            genRandomFood(&game->food, &game->snake);
            game->snake.size++;
            game->score++;
        }

        // snake collision itself
        for (int i = 1; i < game->snake.size; i++)
        {
            if (CheckCollisionRecs((Rectangle){game->snake.position[0].x,
                                               game->snake.position[0].y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE},
                                   (Rectangle){game->snake.position[i].x,
                                               game->snake.position[i].y,
                                               BLOCK_SIZE,
                                               BLOCK_SIZE}))
            {
                game->game_over = true;
            }
        }
    }
    else
    {
        if (IsKeyPressed(KEY_ENTER))
        {
            game->score = 0;
            game->game_over = false;
            game->game_won = false;

            initSnake(&game->snake);
            initFood(&game->food, &game->snake);
        }
    }
}

/*
    GAME WINDOW
*/
int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 800;
    const char screenTitle[] = "Snake";
    const Color screenBackground = RAYWHITE;
    const int gameFps = 60;

    InitWindow(screenWidth, screenHeight, screenTitle);
    SetTargetFPS(gameFps);

    Game game;

    initGame(&game);

    while (!WindowShouldClose())
    {
        updateGame(&game);

        BeginDrawing();
        ClearBackground(screenBackground);

        drawGame(&game);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}