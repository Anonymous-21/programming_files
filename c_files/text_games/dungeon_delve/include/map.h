#ifndef MAP_H
#define MAP_H

#include "rooms.h"

#define ROWS 10
#define COLS 10

typedef struct Map {
  Room list[ROWS * COLS];

} Map;

void map_init(Map *map);
void map_display(Map *map, Vector2 player_position);
bool map_check_available_room(Map *map, Vector2 room_position);

#endif  // MAP_H