#include "obstacles.h"
#include "raylib.h"

void initObstacles(Obstacles *obstacles) {
  obstacles->width = 20;
  obstacles->height = 30;
  obstacles->color = GRAY;
  obstacles->speed = 5;
  obstacles->frames_counter = 0;
  obstacles->list_size = 2;
  obstacles->list[0] = (Vector2){GetScreenWidth() + obstacles->width,
                                 GetScreenHeight() - obstacles->height};
  obstacles->list[1] = (Vector2){GetScreenWidth() + obstacles->width + 400,
                                 GetScreenHeight() - obstacles->height};
  // obstacles->list[2] = (Vector2){GetScreenWidth() + obstacles->width + 600,
  //                                GetScreenHeight() - obstacles->height};
}

void drawObstacles(Obstacles *obstacles) {
  for (int i = 0; i < obstacles->list_size; i++) {
    DrawRectangleRec((Rectangle){obstacles->list[i].x, obstacles->list[i].y,
                                 obstacles->width, obstacles->height},
                     obstacles->color);
  }
}

void updateObstacles(Obstacles *obstacles) {
  for (int i = 0; i < obstacles->list_size; i++) {
    obstacles->list[i].x -= obstacles->speed;

    if (obstacles->list[i].x < -obstacles->width) {
      obstacles->list[i].x = GetScreenWidth() + obstacles->width;
    }
  }

  if (obstacles->frames_counter  % 100000 == 0) {
    obstacles->speed += 0.01;
    obstacles->frames_counter = 0;
  }
}
