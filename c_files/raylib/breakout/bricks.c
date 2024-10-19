#include "bricks.h"
#include "raylib.h"

void initBricks(Bricks *bricks) {
  bricks->rows = 5;
  bricks->cols = 10;
  bricks->width = 79;
  bricks->height = 30;
  bricks->gap = 2;
  bricks->color = SKYBLUE;

  genGrid(bricks);
}

void genGrid(Bricks *bricks) {
  bricks->size = 0;
  int count = 0;

  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {
      int x = j * (bricks->width + bricks->gap);
      int y = i * (bricks->height + bricks->gap);

      bricks->grid[count] = (Vector2){x, y};
      bricks->size++;
      count++;
    }
  }
}

void drawBricks(Bricks *bricks) {
  for (int i = 0; i < bricks->size; i++) {
    DrawRectangleRec((Rectangle){bricks->grid[i].x, bricks->grid[i].y,
                                 bricks->width, bricks->height},
                     bricks->color);
  }
}
