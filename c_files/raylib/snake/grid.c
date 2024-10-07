#include "grid.h"
#include "raylib.h"

void initGrid(Grid *grid, int rows, int cols, int block_size, int margin_x,
              int margin_y) {
  grid->rows = rows;
  grid->cols = cols;
  grid->block_size = block_size;
  grid->color = BLACK;
  grid->line_thickness = 1;
  grid->margin_x = margin_x;
  grid->margin_y = margin_y;
}

void drawGrid(Grid *grid) {
  for (int i = 0; i < grid->rows; i++) {
    for (int j = 0; j < grid->cols; j++) {
      int x = j * grid->block_size + grid->margin_x;
      int y = i * grid->block_size + grid->margin_y;

      DrawRectangleLinesEx(
          (Rectangle){x, y, grid->block_size, grid->block_size},
          grid->line_thickness, grid->color);
    }
  }
}
