#include "raylib.h"
#include <math.h>

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Follower";
  const Color screenBackground = RAYWHITE;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  Rectangle rect = (Rectangle){0, 0, 30, 30};
  Color rect_color = BLUE;

  Rectangle follower = (Rectangle){0, 0, 20, 20};
  Color follower_color = RED;
  float follower_speed = 3;

  while (!WindowShouldClose()) {

    // rect follows mouse
    rect.x = GetMouseX();
    rect.y = GetMouseY();

    // calculate distance between rect and follower
    float distance_x = rect.x - follower.x;
    float distance_y = rect.y - follower.y;
    float distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

    // distance 0 will cal division by 0 error
    if (distance > 0) { 
      // vector normalization = calculate unit distance vector
      distance_x /= distance;
      distance_y /= distance;

      // assign coordinates to follower
      follower.x += distance_x * follower_speed;
      follower.y += distance_y * follower_speed;
    }
    BeginDrawing();
    ClearBackground(screenBackground);

    DrawRectangleRec(rect, rect_color);
    DrawRectangleRec(follower, follower_color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
