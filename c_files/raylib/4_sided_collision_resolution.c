#include <raylib.h>
#include <raymath.h>

typedef struct Platform
{
  Rectangle rect;
  Color color;
  Vector2 center;

} Platform;

typedef struct Box
{
  Rectangle rect;
  float speed;
  Color color;
  Vector2 direction;
  Vector2 center;

} Box;

int main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "4 Sided Collision Resolution";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  float platform_width = 300.0f;
  float platform_height = 150.0f;
  Platform platform = {
      .rect = (Rectangle){GetScreenWidth() * 0.5f - platform_width / 2,
                          GetScreenHeight() * 0.5f - platform_height / 2,
                          platform_width,
                          platform_height},
      .color = RED,
  };

  Box box = {
      .rect = (Rectangle){10, 10, 60, 60},
      .color = BLUE,
      .speed = 400.0f,
      .direction = (Vector2){0, 0},
  };

  while (!WindowShouldClose())
  {
    // get input and move box
    box.direction.x = (float)(IsKeyDown(KEY_RIGHT) - IsKeyDown(KEY_LEFT));
    box.direction.y = (float)(IsKeyDown(KEY_DOWN) - IsKeyDown(KEY_UP));

    if (box.direction.x != 0 && box.direction.y != 0)
    {
      box.direction = Vector2Normalize(box.direction);
    }

    box.rect.x += box.direction.x * box.speed * GetFrameTime();
    box.rect.y += box.direction.y * box.speed * GetFrameTime();

    box.rect.x = Clamp(box.rect.x, 0, GetScreenWidth() - box.rect.width);
    box.rect.y = Clamp(box.rect.y, 0, GetScreenHeight() - box.rect.height);

    // calculate centers of rects
    box.center.x = box.rect.x + box.rect.width / 2;
    box.center.y = box.rect.y + box.rect.height / 2;

    platform.center.x = platform.rect.x + platform.rect.width / 2;
    platform.center.y = platform.rect.y + platform.rect.height / 2;

    // current distance between rect centers
    Vector2 current_distance = Vector2Subtract(box.center, platform.center);

    // minimum required distance between rects
    Vector2 min_distance;
    min_distance.x = platform.rect.width / 2 + box.rect.width / 2;
    min_distance.y = platform.rect.height / 2 + box.rect.height / 2;

    // collision resolution
    if (CheckCollisionRecs(platform.rect, box.rect))
    {
      Vector2 offset;
      offset.x = min_distance.x - fabsf(current_distance.x);
      offset.y = min_distance.y - fabsf(current_distance.y);

      if (offset.x < offset.y)
      {
        // resolve for x if smaller
        box.rect.x += copysign(offset.x, current_distance.x);
      }
      else
      {
        // else resolve for y
        box.rect.y += copysign(offset.y, current_distance.y);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    DrawRectangleRec(platform.rect, platform.color);
    DrawRectangleRec(box.rect, box.color);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}