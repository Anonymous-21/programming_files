#ifndef ROOMS_H
#define ROOMS_H

#include <stdbool.h>

#include "utils.h"

#define NAME_SIZE 20
#define DESCRIPTION_SIZE 500

typedef enum RoomType {
  START,
  ENEMY,
  EMPTY,
  TRAP,
  TREASURE,

} RoomType;

typedef struct Room {
  RoomType room_type;
  char name[NAME_SIZE];
  char description[DESCRIPTION_SIZE];
  Vector2 position;
  bool visited;

} Room;

void room_init(Room *room, RoomType room_type);

#endif  // ROOMS_H;