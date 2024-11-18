#include "raylib.h"

#include "constants.h"
#include "bricks.h"

void initBricks(Bricks *bricks)
{
    genBricks(bricks);
}

void genBricks(Bricks *bricks)
{
    Color color_list[] = COLOR_PALLETE;
    int total_colors = sizeof(color_list) / sizeof(color_list[0]);

    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            int random_color_index = GetRandomValue(0, total_colors - 1);

            int x = j * (BRICK_WIDTH + BRICK_GAP);
            int y = i * (BRICK_HEIGHT + BRICK_GAP);

            bricks->list[i][j].position = (Vector2){x, y};
            bricks->list[i][j].active = true;
            bricks->list[i][j].color = color_list[random_color_index];
        }
    }
}

void drawBricks(Bricks *bricks)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            if (bricks->list[i][j].active)
            {
                DrawRectangleRec((Rectangle){bricks->list[i][j].position.x,
                                             bricks->list[i][j].position.y,
                                             BRICK_WIDTH,
                                             BRICK_HEIGHT},
                                 bricks->list[i][j].color);
            }
        }
    }
}