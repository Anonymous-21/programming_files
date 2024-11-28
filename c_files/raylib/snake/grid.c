#include "grid.h"
#include "constants.h"
#include "raylib.h"

void drawGrid() {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      int x = j * BLOCK_SIZE + MARGIN;
      int y = i * BLOCK_SIZE + MARGIN;

      DrawRectangleLinesEx((Rectangle){x, y, BLOCK_SIZE, BLOCK_SIZE}, 1, BLACK);
    }
  }
}
