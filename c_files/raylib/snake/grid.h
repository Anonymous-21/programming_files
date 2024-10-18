#ifndef GRID_H
#define GRID_H

#include "raylib.h"

typedef struct Grid {
  int rows;
  int cols;
  int block_size;
  int margin;
  float line_thickness;
  Color color;

} Grid;

void initGrid(Grid *grid);
void drawGrid(Grid *grid);

#endif // GRID_H
