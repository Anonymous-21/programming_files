#include <raylib.h>

#include "constants.h"
#include "balls.h"
#include "bricks.h"

// GAME MANAGER

typedef struct Game
{
  int level;

  Ball ball_normal;
  Bricks bricks;

} Game;

void game_init(Game *game)
{
  game->level = 1;

  ball_normal_init(&game->ball_normal);
  bricks_init(&game->bricks, game->level);
}

void game_draw(Game *game)
{
  ball_normal_draw(&game->ball_normal);
  bricks_draw(&game->bricks);
}

void game_update(Game *game)
{
  ball_normal_update(&game->ball_normal);
}

// MAIN

int main(void)
{

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Game game;

  game_init(&game);

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    game_update(&game);
    game_draw(&game);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}