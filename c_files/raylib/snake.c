#include "raylib.h"
#include <stdbool.h>

#define ROWS 20
#define COLS 20
#define BLOCK_SIZE 40

//**********************************
// SNAKE
//**********************************

typedef enum Direction {
  RIGHT,
  LEFT,
  UP,
  DOWN

} Direction;

typedef struct Snake {
  int x;
  int y;
  int width;
  int height;
  int speed;
  Direction direction;
  Rectangle list[ROWS * COLS];
  int size;
  float last_current_time;
  float move_interval;

} Snake;

void snake_init(Snake *snake) {
  snake->x = 0;
  snake->y = 0;
  snake->width = BLOCK_SIZE;
  snake->height = BLOCK_SIZE;
  snake->speed = BLOCK_SIZE;
  snake->direction = RIGHT;
  snake->size = 1;
  snake->list[0] = (Rectangle){snake->x, snake->y, snake->width, snake->height};

  snake->last_current_time = 0.0f;
  snake->move_interval = 0.08f;
}

void snake_draw(Snake *snake) {
  for (int i = 0; i < snake->size; i++) {
    Color snake_color = (i == 0) ? BLUE : SKYBLUE;

    DrawRectangle(snake->list[i].x, snake->list[i].y, snake->list[i].width,
                  snake->list[i].height, snake_color);
  }
}

void snake_update(Snake *snake) {
  // get direction input
  if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT) {
    snake->direction = RIGHT;
  }
  if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT) {
    snake->direction = LEFT;
  }
  if (IsKeyPressed(KEY_UP) && snake->direction != DOWN) {
    snake->direction = UP;
  }
  if (IsKeyPressed(KEY_DOWN) && snake->direction != UP) {
    snake->direction = DOWN;
  }

  float current_time = GetTime();
  if (current_time - snake->last_current_time > snake->move_interval) {
    snake->last_current_time = current_time;

    if (snake->size > 1) {
      for (int i = snake->size - 1; i > 0; i--) {
        snake->list[i] = snake->list[i - 1];
      }
    }

    // move snake according to direction
    switch (snake->direction) {
    case RIGHT:
      snake->x += snake->speed;
      break;
    case LEFT:
      snake->x -= snake->speed;
      break;
    case UP:
      snake->y -= snake->speed;
      break;
    case DOWN:
      snake->y += snake->speed;
      break;
    }

    snake->list[0] =
        (Rectangle){snake->x, snake->y, snake->width, snake->height};
  }
}

//**********************************
// FOOD
//**********************************

typedef struct Food {
  int x;
  int y;
  int width;
  int height;
  Color color;

} Food;

void gen_random_food(Food *food, Snake *snake) {
  while (1) {
    bool matched = false;

    int x = GetRandomValue(0, COLS - 1) * food->width;
    int y = GetRandomValue(0, ROWS - 1) * food->height;

    for (int i = 0; i < snake->size; i++) {
      if (x == snake->list[i].x && y == snake->list[i].y) {
        matched = true;
        break;
      }
    }

    if (!matched) {
      food->x = x;
      food->y = y;
      return;
    }
  }
}

void food_init(Food *food, Snake *snake) {
  food->width = BLOCK_SIZE;
  food->height = BLOCK_SIZE;
  food->color = RED;
  gen_random_food(food, snake);
}

void food_draw(Food *food) {
  DrawRectangleRec((Rectangle){food->x, food->y, food->width, food->height},
                   food->color);
}

//**********************************
// GAME MANAGER
//**********************************

typedef struct Game {
  int score;
  bool game_over;

  Snake snake;
  Food food;

} Game;

void game_init(Game *game) {
  game->score = 0;
  game->game_over = false;

  snake_init(&game->snake);
  food_init(&game->food, &game->snake);
}

void draw_grid() {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      int x = j * BLOCK_SIZE;
      int y = i * BLOCK_SIZE;

      DrawLineEx((Vector2){x, 0}, (Vector2){x, GetScreenHeight()}, 2, BLACK);
      DrawLineEx((Vector2){0, y}, (Vector2){GetScreenWidth(), y}, 2, BLACK);
    }
  }
}

void game_draw(Game *game) {
  draw_grid();

  // draw score
  DrawText(TextFormat("Score: %d", game->score), 10, 10, 30, BLACK);

  // draw rest
  snake_draw(&game->snake);
  food_draw(&game->food);
}

void game_update(Game *game) {
  snake_update(&game->snake);

  // food collision snake
  if (CheckCollisionRecs(
          (Rectangle){game->food.x, game->food.x, game->food.x, game->food.x},
          (Rectangle){game->snake.list[0].x, game->snake.list[0].y, BLOCK_SIZE,
                      BLOCK_SIZE})) {
    gen_random_food(&game->food, &game->snake);
    game->snake.size += 1;
  }
}

//**********************************
// MAIN
//**********************************
int main(void) {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 800;
  const char SCREEN_TITLE[] = "Snake";
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
