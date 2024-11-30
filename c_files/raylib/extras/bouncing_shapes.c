#include "raylib.h"

#define NUMBER_OF_SHAPES 500
#define COLOR_LIST_LENGTH 21

typedef struct {
  char type;
  int x;
  int y;
  int width;
  int height;
  int radius1;
  int radius2;
  int change_x;
  int change_y;
  int rotation;
  Color color;
  int origin_x;
  int origin_y;

} Shape;

typedef struct {
  Shape list[NUMBER_OF_SHAPES];

} ShapesList;

typedef struct {
  Color list[COLOR_LIST_LENGTH];

} ColorList;

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Bouncing Shapes";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  ColorList color_list = {
      DARKGRAY,  MAROON, ORANGE, DARKGREEN, DARKBLUE, DARKPURPLE, DARKBROWN,
      GRAY,      RED,    GOLD,   LIME,      BLUE,     VIOLET,     BROWN,
      LIGHTGRAY, PINK,   YELLOW, GREEN,     SKYBLUE,  PURPLE,     BEIGE,
  };

  ShapesList shapes_list;

  for (int i = 0; i < NUMBER_OF_SHAPES; i++) {
    int x = GetRandomValue(0, GetScreenWidth());
    int y = GetRandomValue(0, GetScreenHeight());

    int width = GetRandomValue(10, 40);
    int height = GetRandomValue(10, 40);

    int radius1 = GetRandomValue(5, 20);
    int radius2 = GetRandomValue(5, 20);

    int change_x = GetRandomValue(1, 3);
    int change_y = GetRandomValue(1, 3);

    int rotation = GetRandomValue(0, 360);

    int color_index = GetRandomValue(0, COLOR_LIST_LENGTH - 1);
    Color color = color_list.list[color_index];

    int shape_type = GetRandomValue(0, 2);

    switch (shape_type) {
    case 0:
      shapes_list.list[i].type = 'r';
      shapes_list.list[i].x = x;
      shapes_list.list[i].y = y;
      shapes_list.list[i].width = width;
      shapes_list.list[i].height = height;
      shapes_list.list[i].rotation = rotation;
      shapes_list.list[i].color = color;
      shapes_list.list[i].change_x = change_x;
      shapes_list.list[i].change_y = change_y;
      shapes_list.list[i].origin_x =
          shapes_list.list[i].x + shapes_list.list[i].width / 2;
      shapes_list.list[i].origin_y =
          shapes_list.list[i].y + shapes_list.list[i].height / 2;
      break;
    case 1:
      shapes_list.list[i].type = 'c';
      shapes_list.list[i].x = x;
      shapes_list.list[i].y = y;
      shapes_list.list[i].radius1 = radius1;
      shapes_list.list[i].color = color;
      shapes_list.list[i].change_x = change_x;
      shapes_list.list[i].change_y = change_y;
      break;
    case 2:
      shapes_list.list[i].type = 'e';
      shapes_list.list[i].x = x;
      shapes_list.list[i].y = y;
      shapes_list.list[i].radius1 = radius1;
      shapes_list.list[i].radius2 = radius2;
      shapes_list.list[i].color = color;
      shapes_list.list[i].change_x = change_x;
      shapes_list.list[i].change_y = change_y;
      break;
    }
  }

  while (!WindowShouldClose()) {

    for (int i = 0; i < NUMBER_OF_SHAPES; i++) {
      shapes_list.list[i].x += shapes_list.list[i].change_x;
      shapes_list.list[i].y += shapes_list.list[i].change_y;

      if (shapes_list.list[i].type == 'r') {
        if (shapes_list.list[i].x <= 0 ||
            shapes_list.list[i].x >=
                GetScreenWidth() - shapes_list.list[i].width) {
          shapes_list.list[i].change_x *= -1;
        } else if (shapes_list.list[i].y <= 0 ||
                   shapes_list.list[i].y >=
                       GetScreenHeight() - shapes_list.list[i].height) {
          shapes_list.list[i].change_y *= -1;
        }
      } else if (shapes_list.list[i].type == 'c') {
        if (shapes_list.list[i].x <= 0 ||
            shapes_list.list[i].x >=
                GetScreenWidth() - shapes_list.list[i].radius1) {
          shapes_list.list[i].change_x *= -1;
        } else if (shapes_list.list[i].y <= 0 ||
                   shapes_list.list[i].y >=
                       GetScreenHeight() - shapes_list.list[i].radius1) {
          shapes_list.list[i].change_y *= -1;
        }
      } else if (shapes_list.list[i].type == 'e') {
        if (shapes_list.list[i].x <= 0 ||
            shapes_list.list[i].x >=
                GetScreenWidth() - shapes_list.list[i].radius1) {
          shapes_list.list[i].change_x *= -1;
        } else if (shapes_list.list[i].y <= 0 ||
                   shapes_list.list[i].y >=
                       GetScreenHeight() - shapes_list.list[i].radius2) {
          shapes_list.list[i].change_y *= -1;
        }
      }
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    for (int i = 0; i < NUMBER_OF_SHAPES; i++) {
      if (shapes_list.list[i].type == 'r') {
        DrawRectanglePro(
            (Rectangle){shapes_list.list[i].x, shapes_list.list[i].y,
                        shapes_list.list[i].width, shapes_list.list[i].height},
            (Vector2){shapes_list.list[i].origin_x,
                      shapes_list.list[i].origin_y},
            shapes_list.list[i].rotation, shapes_list.list[i].color);
      } else if (shapes_list.list[i].type == 'c') {
        DrawCircle(shapes_list.list[i].x, shapes_list.list[i].y,
                   shapes_list.list[i].radius1, shapes_list.list[i].color);
      } else if (shapes_list.list[i].type == 'e') {
        DrawEllipse(shapes_list.list[i].x, shapes_list.list[i].y,
                    shapes_list.list[i].radius1, shapes_list.list[i].radius2,
                    shapes_list.list[i].color);
      }
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
