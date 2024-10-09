#include "grid.h"
#include "raylib.h"

void initGrid(Grid *grid) {
  grid->rows = 20;
  grid->cols = 20;
  grid->block_size = 30;
  grid->margin = 100;
  grid->color = BLACK;
  grid->line_thickness = 1;
}

void drawGrid(Grid *grid) {
  for (int i = 0; i < grid->rows; i++) {
    for (int j = 0; j < grid->cols; j++) {
      int x = (j * grid->block_size) + grid->margin;
      int y = (i * grid->block_size) + grid->margin;

      DrawRectangleLinesEx(
          (Rectangle){x, y, grid->block_size, grid->block_size},
          grid->line_thickness, grid->color);
    }
  }
}
