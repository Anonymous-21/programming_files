#include <raylib.h>
#include <stdio.h>

#include "bricks.h"
#include "constants.h"

#define TEXT_LENGTH 10

void bricks_init(Bricks *bricks, int brick_level)
{
  for (int i = 0; i < ROWS; i++)
  {
    float width = (GetScreenWidth() - MARGIN * 2) / COLS;
    float height = (GetScreenHeight() - MARGIN * 2) / ROWS;
    float gap = 3;

    for (int j = 0; j < COLS; j++)
    {
      int x = j * (width + gap) + MARGIN;
      int y = i * (height + gap) + MARGIN;

      Brick brick;
      brick.rect = (Rectangle){x, y, width, height};
      brick.active = true;
      brick.thickness = 5.0f;
      brick.color = BLACK;
      brick.level = brick_level;

      bricks->list[i * COLS + j] = brick;
    }
  }
}

void bricks_draw(Bricks *bricks)
{
  char text_str[TEXT_LENGTH];

  for (int i = 0; i < ROWS * COLS; i++)
  {
    // draw level of brick
    snprintf(text_str, TEXT_LENGTH, "%d", bricks->list[i].level);
    float font_size = 30;
    float text_width = MeasureText(text_str, font_size);
    Color text_color = BLACK;

    DrawText(text_str, (bricks->list[i].rect.x + bricks->list[i].rect.width / 2 - text_width / 2),
             (bricks->list[i].rect.y + bricks->list[i].rect.height / 2 - font_size / 2),
             font_size,
             text_color);

    DrawRectangleLinesEx(bricks->list[i].rect, bricks->list[i].thickness, bricks->list[i].color);
  }
}