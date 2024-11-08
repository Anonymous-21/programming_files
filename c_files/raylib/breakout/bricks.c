#include "bricks.h"
#include "raylib.h"

void initBricks(Bricks *bricks) {
  bricks->rows = ROWS;
  bricks->cols = COLS;
  bricks->width = 79;
  bricks->height = 30;
  bricks->color = GRAY;
  bricks->gap = 2;

  // initialize list with coordinates
  genBricks(bricks);
}

void genBricks(Bricks *bricks) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      int x = j * (bricks->width + bricks->gap);
      bricks->height = 30;
      int y = i * (bricks->height + bricks->gap);
      bricks->height = 30;

      bricks->list[i][j] = (Vector2){x, y};
    }
  }
}

void drawBricks(Bricks *bricks) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      DrawRectangleRec((Rectangle){bricks->list[i][j].x, bricks->list[i][j].y,
                                   bricks->width, bricks->height},
                       bricks->color);
    }
  }
}
