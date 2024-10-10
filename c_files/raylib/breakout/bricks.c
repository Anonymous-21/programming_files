#include "bricks.h"
#include "ball.h"
#include "raylib.h"

void initBricks(Bricks *bricks) {
  bricks->rows = LIST_ROW_LENGTH;
  bricks->cols = LIST_COL_LENGTH;
  bricks->width = 78;
  bricks->height = 30;
  bricks->color_num = 1;
  bricks->gap = 2;

  genGrid(bricks);
  updateBrickColor(bricks);
}

void genGrid(Bricks *bricks) {
  for (int i = 0; i < bricks->rows; i++) {
    int x = 0;
    for (int j = 0; j < bricks->cols; j++) {
      x = j * (bricks->width + bricks->gap);
      int y = i * (bricks->height + bricks->gap);

      bricks->grid[i][j] = (Vector2){x, y};
    }
  }
}

void updateBrickColor(Bricks *bricks) {
  switch (bricks->color_num) {
  case 1:
    bricks->color = RED;
    break;
  case 2:
    bricks->color = BLUE;
    break;
  case 3:
    bricks->color = GREEN;
    break;
  case 4:
    bricks->color = ORANGE;
    break;
  case 5:
    bricks->color = PURPLE;
    break;
  }
}

void drawBricks(Bricks *bricks) {
  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {
      if (bricks->grid[i][j].x != -1 && bricks->grid[i][j].y != -1) {
        DrawRectangleRec((Rectangle){bricks->grid[i][j].x, bricks->grid[i][j].y,
                                     bricks->width, bricks->height},
                         bricks->color);
      }
    }
    bricks->color_num++;
    if (bricks->color_num > 5) {
      bricks->color_num = 1;
    }
    updateBrickColor(bricks);
  }
}

void bricksCollisionBall(Bricks *bricks, Ball *ball) {
  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {
      if (CheckCollisionCircleRec((Vector2){ball->x, ball->y}, ball->radius,
                                  (Rectangle){bricks->grid[i][j].x,
                                              bricks->grid[i][j].y,
                                              bricks->width, bricks->height})) {
        bricks->grid[i][j] = (Vector2){-1, -1};
        ball->change_y *= -1;
      }
    }
  }
}

bool checkWinCondition(Bricks *bricks, bool game_won) {
  for (int i = 0; i < bricks->rows; i++) {
    for (int j = 0; j < bricks->cols; j++) {
      if (bricks->grid[i][j].x != -1 && bricks->grid[i][j].y != -1) {
        break;
      } else {
        game_won = true;
      }
    }
  }

  return game_won;
}
