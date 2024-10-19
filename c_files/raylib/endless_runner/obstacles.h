#ifndef OBSTACLES_H
#define OBSTACLES_H

#include "raylib.h"

#define LIST_LENGTH 5

typedef struct Obstacles {
  float width;
  float height;
  Color color;
  float speed;
  int frames_counter;
  int list_size;
  Vector2 list[LIST_LENGTH];

} Obstacles;

void initObstacles(Obstacles *obstacles);
void drawObstacles(Obstacles *obstacles);
void updateObstacles(Obstacles *obstacles);

#endif // OBATACLES_H
