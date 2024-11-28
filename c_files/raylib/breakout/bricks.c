#include "bricks.h"
#include "constants.h"
#include "raylib.h"

void initBricks(Bricks *bricks) {
  bricks->color = GRAY;

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      int x = j * (BRICK_WIDTH + BRICK_GAP);
      int y = i * (BRICK_HEIGHT + BRICK_GAP);

      bricks->list[i * 10 + j].coordinates = (Vector2){x, y};
      bricks->list[i * 10 + j].is_active = true;
    }
  }
}

void drawBricks(Bricks *bricks) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (bricks->list[i * 10 + j].is_active) {
        DrawRectangleRec((Rectangle){bricks->list[i * 10 + j].coordinates.x,
                                     bricks->list[i * 10 + j].coordinates.y,
                                     BRICK_WIDTH, BRICK_HEIGHT},
                         bricks->color);
      }
    }
  }
}
