#include "raylib.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

// Strut declaration
typedef struct grid {
  int rows;
  int cols;
  int block_size;
  float line_thickness;
  int margin_x;
  int margin_y;
  Color color;
} grid;

typedef struct snake {
  int x;
  int y;
  int width;
  int height;
  Color color;
} snake;

typedef struct food {
  int x;
  int y;
  int width;
  int height;
  Color color;
} food;

// functions declaration (prototype)
void draw_grid(struct grid Grid);
void gen_random_food(struct food *Food, struct grid Grid, struct snake Snake);

// functions
void draw_grid(struct grid Grid) {
  for (int i = 0; i < Grid.rows; i++) {
    for (int j = 0; j < Grid.cols; j++) {
      int x = j * Grid.block_size;
      int y = i * Grid.block_size;

      DrawRectangleLinesEx((Rectangle){x, y, Grid.block_size, Grid.block_size},
                           Grid.line_thickness, Grid.color);
    }
  }
}

void gen_random_food(struct food *Food, struct grid Grid, struct snake Snake) {
  while (1) {
    int x = GetRandomValue(0, Grid.cols - 1) * Grid.block_size;
    int y = GetRandomValue(0, Grid.rows - 1) * Grid.block_size;

    for (size_t i = 0; i < strlen(Snake.list); i++) {
      if (x != Snake.list[i] && y != Snake.list[i]) {
        Food->x = x;
        Food->y = y;
        break;
      }
    }
  }
}

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 800;
  const char screenTitle[] = "Snake";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  bool game_over = false;

  grid Grid;
  snake Snake;
  food Food;

  Grid.rows = 20;
  Grid.cols = 20;
  Grid.block_size = 40;
  Grid.line_thickness = 0.5;
  Grid.margin_x = GetScreenWidth() - (Grid.cols * Grid.block_size);
  Grid.margin_y = GetScreenHeight() - (Grid.rows * Grid.block_size);
  Grid.color = BLACK;

  Snake.width = Grid.block_size;
  Snake.height = Grid.block_size;
  Snake.x = Grid.margin_x;
  Snake.y = Grid.margin_y;
  Snake.color = BLUE;

  Food.width = Grid.block_size;
  Food.height = Grid.block_size;
  // gen_random_food(&Food, Grid);
  Food.color = RED;

  while (!WindowShouldClose()) {
    BeginDrawing();

    ClearBackground(screenBackground);

    draw_grid(Grid);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
