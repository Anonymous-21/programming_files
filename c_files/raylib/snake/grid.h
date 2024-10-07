#ifndef GRID_H
#define GRID_H

#include "raylib.h"

typedef struct Grid {
  int rows;
  int cols;
  int block_size;
  Color color;
  float line_thickness;
  int margin_x;
  int margin_y;
} Grid;

void initGrid(Grid *grid, int rows, int cols, int block_size, int margin_x,
              int margin_y);
void drawGrid(Grid *grid);

#endif // GRID_H
