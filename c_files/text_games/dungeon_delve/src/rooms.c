#include "rooms.h"

#include <string.h>

#include "utils.h"

void room_init(Room *room, RoomType room_type) {
  room->room_type = room_type;
  room->visited = false;

  switch (room->room_type) {
    case START:
      strncpy(room->name, "Starting Room", NAME_SIZE);
      strncpy(room->description, "Player starts here", DESCRIPTION_SIZE);
      break;
    case ENEMY:
      strncpy(room->name, "Enemy Room", NAME_SIZE);
      strncpy(room->description, "Enemies spawn here", DESCRIPTION_SIZE);
      break;
    case EMPTY:
      strncpy(room->name, "Empty Room", NAME_SIZE);
      strncpy(room->description, "Empty Room", DESCRIPTION_SIZE);
      break;
    case TRAP:
      strncpy(room->name, "Trap Room", NAME_SIZE);
      strncpy(room->description, "Traps spawn here", DESCRIPTION_SIZE);
      break;
    case TREASURE:
      strncpy(room->name, "Treasure Room", NAME_SIZE);
      strncpy(room->description, "Treasure spawn here", DESCRIPTION_SIZE);
      break;
  }
}
