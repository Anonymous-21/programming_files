#include "bricks.h"
#include "raylib.h"

void initBricks(Bricks *bricks) {
  bricks->rows = 5;
  bricks->cols = 10;
  bricks->width = 79;
  bricks->height = 30;
  bricks->color = GRAY;
  bricks->gap = 2;

  genGrid(bricks);
}

void genGrid(Bricks *bricks) {

  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {

      int x = j * (bricks->width + bricks->gap);
      int y = i * (bricks->height + bricks->gap);

      bricks->grid[i][j] = (Vector2){x, y};
    }
  }
}

void drawBricks(Bricks *bricks) {

  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {

      DrawRectangleRec((Rectangle){bricks->grid[i][j].x, bricks->grid[i][j].y,
                                   bricks->width, bricks->height},
                       bricks->color);
    }
  }
}
