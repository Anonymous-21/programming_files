#include "raylib.h"
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SNOWFLAKES 50

typedef struct {
  double x;
  double y;
  double radius;
  double speed;
  double angle;

} Snowflake;

typedef struct {
  Snowflake list[MAX_SNOWFLAKES];
  Color color;

} SnowList;

double randomDoubleValue(double min, double max) {
  srand(time(NULL));

  double random_value = (double)rand() / RAND_MAX;

  return min + random_value * (max - min);
}

void resetSnowflake(Snowflake *snowflake) {
  snowflake->x = GetRandomValue(0, GetScreenWidth());
  snowflake->y = GetRandomValue(-200, 0);
  snowflake->radius = GetRandomValue(1, 3);
  snowflake->speed = GetRandomValue(20, 40);
  snowflake->angle = randomDoubleValue(PI, PI * 2);
}

int main(void) {
  const int screenWidth = 800;
  const int screenHeight = 600;
  const char screenTitle[] = "Falling Snow";
  const Color screenBackground = BLACK;
  const int gameFps = 60;

  InitWindow(screenWidth, screenHeight, screenTitle);
  SetTargetFPS(gameFps);

  SnowList snow_list;
  snow_list.color = WHITE;

  for (int i = 0; i < MAX_SNOWFLAKES; i++) {
    Snowflake snowflake;
    snow_list.list[i] = snowflake;
    resetSnowflake(&snow_list.list[i]);
  }

  while (!WindowShouldClose()) {

    for (int i = 0; i < MAX_SNOWFLAKES; i++) {
      snow_list.list[i].y += snow_list.list[i].speed * GetFrameTime();
      if (snow_list.list[i].y > GetScreenHeight()) {
        resetSnowflake(&snow_list.list[i]);
      }

      snow_list.list[i].x += snow_list.list[i].speed *
                             cos(snow_list.list[i].angle) * GetFrameTime();
      snow_list.list[i].angle += 1 * GetFrameTime();
    }

    BeginDrawing();
    ClearBackground(screenBackground);

    for (int i = 0; i < MAX_SNOWFLAKES; i++) {
      DrawCircleV((Vector2){snow_list.list[i].x, snow_list.list[i].y},
                  snow_list.list[i].radius, snow_list.color);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}
