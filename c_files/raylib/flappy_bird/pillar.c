#include "pillar.h"
#include "raylib.h"

void initPillar(Pillar *pillar) {
  pillar->width = 100;
  pillar->color = GRAY;
  pillar->speed = 5;
  pillar->list_size = 2;

  // vector3 = x, y, height
  pillar->top_list[0] = (Vector3){GetScreenWidth() + pillar->width, 0, 300};
  pillar->top_list[1] =
      (Vector3){GetScreenWidth() + pillar->width + 500, 0, 300};

  pillar->bottom_list[0] =
      (Vector3){GetScreenWidth() + pillar->width, 500, 300};
  pillar->bottom_list[1] =
      (Vector3){GetScreenWidth() + pillar->width + 500, 500, 300};
}

void drawPillar(Pillar *pillar) {
  for (int i = 0; i < pillar->list_size; i++) {
    DrawRectangleRec((Rectangle){pillar->top_list[i].x, pillar->top_list[i].y,
                                 pillar->width, pillar->top_list[i].z},
                     pillar->color);
    DrawRectangleRec((Rectangle){pillar->bottom_list[i].x,
                                 pillar->bottom_list[i].y, pillar->width,
                                 pillar->bottom_list[i].z},
                     pillar->color);
  }
}

void updatePillar(Pillar *pillar) {
  for (int i = 0; i < pillar->list_size; i++) {
    // add negative speed to pillars
    pillar->top_list[i].x -= pillar->speed;
    pillar->bottom_list[i].x -= pillar->speed;

    // when pillars reach -x, reset position to screen end
    if (pillar->top_list[i].x < -pillar->width) {

      pillar->top_list[i].x = GetScreenWidth() + pillar->width;
      pillar->bottom_list[i].x = GetScreenWidth() + pillar->width;

      int random_top_height = GetRandomValue(0, 400);
      pillar->top_list[i].z = random_top_height; // top pillar height

      pillar->bottom_list[i].y =
          random_top_height +
          200; // y of bottom pillar with gap 200 from top pillar

      pillar->bottom_list[i].z =
          GetScreenHeight() - random_top_height + 200; // bottom pillar height
    }
  }
}
