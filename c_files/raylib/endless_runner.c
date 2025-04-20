#include "raylib.h"
#include "utils.h"

#define NUM_OF_ENEMIES 10

// PLAYER

typedef struct Player {
  Rectangle rect;
  Color color;
  float change_y;
  float gravity;
  float jump_strength;

} Player;

void player_init(Player *player) {
  player->rect = (Rectangle){100, GetScreenHeight() - 50, 20, 50};
  player->change_y = 0.0f;
  player->gravity = 1500.0f;
  player->jump_strength = -500;
  player->color = DARKGREEN;
}

void player_draw(Player *player) {
  DrawRectangleRec(player->rect, player->color);
}

void player_update(Player *player) {
  if (IsKeyPressed(KEY_UP)) {
    player->change_y = player->jump_strength;
  }

  player->change_y += player->gravity * GetFrameTime();
  player->rect.y += player->change_y * GetFrameTime();

  player->rect.y = max_float(
      0.0f, min_float(player->rect.y, GetScreenHeight() - player->rect.height));
}

// ENEMIES

typedef struct Enemy {
  Rectangle rect;
  Color color;
  float speed;
  float horizontal_distance;

} Enemy;

typedef struct Enemies {
  Enemy list[NUM_OF_ENEMIES];
  int size;

} Enemies;

void enemies_init(Enemies *enemies) { enemies->size = 0; }

void enemies_draw(Enemies *enemies) {
  if (enemies->size > 0) {
    for (int i = 0; i < enemies->size; i++) {
      DrawRectangleRec(enemies->list[i].rect, enemies->list[i].color);
    }
  }
}

void enemies_update(Enemies *enemies) {
  // add enemy
  if (enemies->size <= 0 ||
      GetScreenWidth() - enemies->list[enemies->size - 1].horizontal_distance >
          enemies->list[enemies->size - 1].rect.x +
              enemies->list[enemies->size - 1].rect.width) {

    float random_height = (float)GetRandomValue(20, 80);
    Enemy enemy = {
        .rect = (GetScreenWidth(), GetScreenHeight() - random_height,
                 GetRandomValue(10, 30), random_height),
        .color = BLACK,
        .horizontal_distance = GetRandomValue(100, 200),
        .speed = 300.0f,

    };

    enemies->list[enemies->size] = enemy;
    enemies->size += 1;
  }

  // move and remove enemy
  if (enemies->size > 0) {
    for (int i = 0; i < enemies->size; i++) {
      enemies->list[i].rect.x -= enemies->list[i].speed * GetFrameTime();

      // remove
      if (enemies->list[i].rect.x + enemies->list[i].rect.width +
              enemies->list[i].horizontal_distance <
          0) {
        enemies->size -= 1;
      }
    }
  }
}

// GAME

typedef struct Game {
  int score;
  bool game_over;

  Player player;
  Enemies enemies;

} Game;

void game_init(Game *game) {
  game->score = 0;
  game->game_over = false;

  player_init(&game->player);
  enemies_init(&game->enemies);
}

void game_draw(Game *game) {
  // draw score
  DrawText(TextFormat("Score: %d", game->score), 10, 10, 30, BLACK);

  // draw rest
  player_draw(&game->player);
  enemies_draw(&game->enemies);
}

void game_update(Game *game) {
  if (!game->game_over) {
    player_update(&game->player);
    enemies_update(&game->enemies);
  }
}

// MAIN

int main(void) {
  const int SCREEN_WIDTH = 1000;
  const int SCREEN_HEIGHT = 200;
  const char SCREEN_TITLE[] = "Endless Runner";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Game game;

  game_init(&game);

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    game_draw(&game);
    game_update(&game);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}