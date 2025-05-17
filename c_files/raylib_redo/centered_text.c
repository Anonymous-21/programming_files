#include <raylib.h>

void
center_and_draw_text(int num, Rectangle rect)
{
  const char* text = TextFormat("%d", num);
  int font_size = 40;
  int text_width = MeasureText(text, font_size);
  int pos_x = rect.x + rect.width / 2 - text_width / 2;
  int pos_y = rect.y + rect.height / 2 - font_size / 2;
  Color color = BLACK;

  DrawText(text, pos_x, pos_y, font_size, color);
}

int
main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Centered Text";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  float width = 400.0f;
  float height = 200.0f;
  Rectangle rect = (Rectangle){ (float)GetScreenWidth() / 2 - width / 2,
                                (float)GetScreenHeight() / 2 - height / 2,
                                width,
                                height };
  Color color = BLACK;
  float thickness = 5.0f;

  int num = 0;

  while (!WindowShouldClose()) {
    if (IsKeyPressed(KEY_UP)) {
      num++;
    }
    if (IsKeyPressed(KEY_DOWN)) {
      num--;
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    DrawRectangleLinesEx(rect, thickness, color);
    center_and_draw_text(num, rect);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
