#include <stdio.h>
#include <stdlib.h>
#include "raylib.h"

#include "constants.h"
#include "snake.h"
#include "food.h"
#include "collision_handler.h"
#include "ui.h"

int main(void)
{
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);
    SetTargetFPS(GAME_FPS);

    int score = 0;
    char score_str[SCORE_LENGTH];
    bool main_menu = true;
    bool game_active = false;
    bool game_over = false;
    bool game_won = false;

    bool highlight_play_button = false;
    bool highlight_quit_button = false;

    Snake snake;
    Food food;

    initSnake(&snake);
    initFood(&food, &snake);

    while (!WindowShouldClose())
    {
        // convert score to string
        snprintf(score_str, SCORE_LENGTH, "Score: %d\n", score);

        // game win condition
        if (snake.snake_array.size >= 600)
        {
            game_won = true;
        }

        // Handle game over or win
        if (game_over || game_won)
        {
            game_active = false;
            if (IsKeyPressed(KEY_ENTER))
            {
                main_menu = true;
                game_active = false;
                game_over = false;
                game_won = false;
            }
        }

        // highlight main menu buttons
        highlight_play_button = false;
        highlight_quit_button = false;

        Vector2 mouse_pos = GetMousePosition();

        if (CheckCollisionPointRec(mouse_pos,
                                   (Rectangle){
                                       (float)GetScreenWidth() / 2 - 70,
                                       (float)GetScreenHeight() / 2 - 100,
                                       150,
                                       50}))
        {
            highlight_play_button = true;

            if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
            {
                main_menu = false;
                score = 0;
                initSnake(&snake);
                initFood(&food, &snake);
                game_active = true;
                game_over = false;
                game_won = false;
            }
        }

        if (CheckCollisionPointRec(mouse_pos,
                                   (Rectangle){
                                       (float)GetScreenWidth() / 2 - 70,
                                       (float)GetScreenHeight() / 2,
                                       150,
                                       50}))
        {
            highlight_quit_button = true;

            if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
            {
                exit(0);
            }
        }

        // after main menu
        if (game_active)
        {
            // move and update snake
            updateSnakeList(&snake);
            getDirection(&snake);
            moveSnake(&snake);

            // collisions
            snakeCollisionWalls(&snake, &game_over);
            snakeCollisionFood(&snake, &food);
            snakeCollisionItself(&snake, &game_over);
        }

        // begin drawing program
        BeginDrawing();
        ClearBackground(SCREEN_BACKGROUND);

        // draw starting menu
        if (main_menu)
        {
            drawMainMenu(highlight_play_button,
                         highlight_quit_button);
        }
        // draw game
        else if (game_active)
        {
            // draw window outline
            drawOutline();

            // draw score
            drawScore(score_str);

            // draw snake
            drawSnake(&snake);
            // draw food
            drawFood(&food);
        }
        // draw game over menu
        else if (game_over)
        {
            drawGameOverMenu();
        }
        // draw game won menu
        else if (game_won)
        {
            drawGameWonMenu();
        }

        EndDrawing();
    }

    freeSnakeList(&snake);
    CloseWindow();

    return 0;
}
