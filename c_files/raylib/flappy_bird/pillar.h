#ifndef PILLAR_H
#define PILLAR_H

#include "raylib.h"

#define LIST_LENGTH 5

typedef struct Pillar
{
  float width;
  Color color;
  float speed;
  int list_size;
  Vector3 top_list[LIST_LENGTH];
  Vector3 bottom_list[LIST_LENGTH];

}Pillar;

void initPillar(Pillar *pillar);
void drawPillar(Pillar *pillar);
void updatePillar(Pillar *pillar);

#endif // PILLAR_H
