#include <raylib.h>

#define ROWS 20
#define COLS 20
#define BLOCK_SIZE 30
#define MARGIN 100

// BRICKS
void
draw_grid()
{
  // rectangle outline
  DrawRectangleLinesEx((Rectangle){ MARGIN,
                                    MARGIN,
                                    GetScreenWidth() - MARGIN * 2,
                                    GetScreenHeight() - MARGIN * 2 },
                       5.0f,
                       BLACK);

  // vertical lines
  for (int x = MARGIN + BLOCK_SIZE; x < GetScreenWidth() - MARGIN;
       x += BLOCK_SIZE) {
    DrawLineEx((Vector2){ x, MARGIN },
               (Vector2){ x, GetScreenHeight() - MARGIN },
               2.0f,
               BLACK);
  }

  // horizontal lines
  for (int y = MARGIN + BLOCK_SIZE; y < GetScreenHeight() - MARGIN;
       y += BLOCK_SIZE) {
    DrawLineEx((Vector2){ MARGIN, y },
               (Vector2){ GetScreenWidth() - MARGIN, y },
               2.0f,
               BLACK);
  }
}

// SNAKE
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
  int size;
  Vector2 list[ROWS * COLS];
  Direction direction;
  Color color;

  float last_current_time;
  float movement_interval;

} Snake;

void
snake_init(Snake* snake)
{
  snake->x = MARGIN;
  snake->y = MARGIN;
  snake->size = 1;
  snake->list[0] = (Vector2){ snake->x, snake->y };
  snake->direction = RIGHT;

  snake->last_current_time = 0.0f;
  snake->movement_interval = 0.08f;
}

void
snake_draw(Snake* snake)
{
  for (int i = 0; i < snake->size; i++) {
    snake->color = (i == 0) ? BLUE : SKYBLUE;

    DrawRectangle(
      snake->list[i].x, snake->list[i].y, BLOCK_SIZE, BLOCK_SIZE, snake->color);
  }
}

void
get_user_input(Snake* snake)
{
  if (IsKeyPressed(KEY_RIGHT) && snake->direction != LEFT) {
    snake->direction = RIGHT;
  }
  if (IsKeyPressed(KEY_LEFT) && snake->direction != RIGHT) {
    snake->direction = LEFT;
  }
  if (IsKeyPressed(KEY_DOWN) && snake->direction != UP) {
    snake->direction = DOWN;
  }
  if (IsKeyPressed(KEY_UP) && snake->direction != DOWN) {
    snake->direction = UP;
  }
}

void
snake_move(Snake* snake)
{
  switch (snake->direction) {
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
}

void
snake_collision_walls(Snake* snake, bool* game_over)
{
  if (snake->list[0].x < MARGIN ||
      snake->list[0].x > GetScreenWidth() - MARGIN - BLOCK_SIZE) {
    *game_over = true;
  }
  if (snake->list[0].y < MARGIN ||
      snake->list[0].y > GetScreenHeight() - MARGIN - BLOCK_SIZE) {
    *game_over = true;
  }
}

void
snake_collision_itself(Snake* snake, bool* game_over)
{
  for (int i = 1; i < snake->size; i++) {
    if (CheckCollisionRecs(
          (Rectangle){
            snake->list[0].x, snake->list[0].y, BLOCK_SIZE, BLOCK_SIZE },
          (Rectangle){
            snake->list[i].x, snake->list[i].y, BLOCK_SIZE, BLOCK_SIZE })) {
      *game_over = true;
    }
  }
}

void
snake_update(Snake* snake, bool* game_over)
{
  get_user_input(snake);

  float current_time = GetTime();
  if (current_time - snake->last_current_time > snake->movement_interval) {
    snake->last_current_time = current_time;

    if (snake->size > 1) {
      for (int i = snake->size - 1; i > 0; i--) {
        snake->list[i] = snake->list[i - 1];
      }
    }

    snake_move(snake);
    // snake_collision_walls(snake, game_over);

    snake->list[0] = (Vector2){ snake->x, snake->y };
  }
}

void
snake_grow(Snake* snake)
{
  Vector2 new_segment = snake->list[snake->size - 1];
  // move segment to the opposite direction of snake movement
  // away from tail
  switch (snake->direction) {
    case RIGHT:
      new_segment.x -= BLOCK_SIZE;
      break;
    case LEFT:
      new_segment.x += BLOCK_SIZE;
      break;
    case DOWN:
      new_segment.y -= BLOCK_SIZE;
      break;
    case UP:
      new_segment.y += BLOCK_SIZE;
      break;
  }

  snake->list[snake->size] = new_segment;
  snake->size += 1;
}

// FOOD
typedef struct Food
{
  int x;
  int y;
  Color color;

} Food;

void
gen_random_food(Food* food, Snake* snake)
{
  while (1) {
    bool in_list = false;

    int x = GetRandomValue(0, COLS - 1) * BLOCK_SIZE + MARGIN;
    int y = GetRandomValue(0, ROWS - 1) * BLOCK_SIZE + MARGIN;

    for (int i = 0; i < snake->size; i++) {
      if (snake->list[i].x == x && snake->list[i].y == y) {
        in_list = true;
        break;
      }
    }

    if (!in_list) {
      food->x = x;
      food->y = y;
      return;
    }
  }
}

void
food_init(Food* food, Snake* snake)
{
  gen_random_food(food, snake);
  food->color = RED;
}

void
food_draw(Food* food)
{
  DrawRectangle(food->x, food->y, BLOCK_SIZE, BLOCK_SIZE, food->color);
}

// MAIN
void
center_and_draw_text(char* text,
                     int font_size,
                     int rect_x,
                     int rect_y,
                     int rect_width,
                     int rect_height)
{
  int text_width = MeasureText(text, font_size);
  int text_x = rect_x + rect_width / 2 - text_width / 2;
  int text_y = rect_y + rect_height / 2 - font_size / 2;
  Color color = BLACK;

  DrawText(text, text_x, text_y, font_size, color);
}

int
main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 800;
  const char SCREEN_TITLE[] = "Snake";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  int score = 0;
  bool game_over = false;

  Snake snake;
  Food food;

  snake_init(&snake);
  food_init(&food, &snake);

  while (!WindowShouldClose()) {
    // UPDATES
    if (!game_over) {
      snake_update(&snake, &game_over);

      // snake collision food
      if (CheckCollisionRecs(
            (Rectangle){
              snake.list[0].x, snake.list[0].y, BLOCK_SIZE, BLOCK_SIZE },
            (Rectangle){ food.x, food.y, BLOCK_SIZE, BLOCK_SIZE })) {

        gen_random_food(&food, &snake);
        snake_grow(&snake);
        score++;
      }

      snake_collision_itself(&snake, &game_over);
      snake_collision_walls(&snake, &game_over);
    } else {
      if (IsKeyPressed(KEY_ENTER)) {
        score = 0;
        game_over = false;

        snake_init(&snake);
        food_init(&food, &snake);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    // DRAW
    DrawText(TextFormat("%d", score), GetScreenWidth() / 2 - 10, 30, 40, BLACK);

    snake_draw(&snake);
    food_draw(&food);

    draw_grid();

    if (game_over) {
      center_and_draw_text(
        "GAME OVER", 40, 0, 0, GetScreenWidth(), GetScreenHeight());
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}