#include "raylib.h"
#include <stdio.h>

#define TEXT_SIZE 10

int main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Centered Text Example";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  float width = 150.0f;
  float height = 100.f;
  Rectangle rect =
      (Rectangle){GetScreenWidth() * 0.5f - width / 2,
                  GetScreenHeight() * 0.5f - height / 2, width, height};
  float thickness = 5.0f;
  Color rect_color = BLACK;

  int count = 0;
  char text_str[TEXT_SIZE];

  while (!WindowShouldClose())
  {
    snprintf(text_str, TEXT_SIZE, "%d", count);

    if (IsKeyPressed(KEY_UP))
    {
      count++;
    }
    else if (IsKeyPressed(KEY_DOWN))
    {
      count--;
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    DrawRectangleLinesEx(rect, thickness, rect_color);

    int font_size = 40;
    float text_width = MeasureText(text_str, font_size);
    int text_x = (int)(rect.x + rect.width / 2) - text_width / 2;
    int text_y = (int)(rect.y + rect.height / 2) - font_size / 2;

    DrawText(text_str, text_x, text_y, font_size, BLACK);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}