#ifndef MAP_H
#define MAP_H

#include "rooms.h"

#define ROWS 10
#define COLS 10

typedef struct Map {
  Room list[ROWS * COLS];

} Map;

void map_init(Map *map);
void map_draw(Map *map);

#endif  // MAP_H