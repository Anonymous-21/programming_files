
#include "map.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "rooms.h"

void map_init(Map *map) {
  srand(time(0));

  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      Room room;
      room.position.x = j;
      room.position.y = i;

      if (i == 0 && j == 0) {
        room_init(&room, START);
      } else {
        int random_num = (rand() % 100) + 1;

        if (random_num > 98) {
          room_init(&room, TREASURE);
        } else {
          int random_room = (rand() % 3) + 1;

          if (random_room == 1) {
            room_init(&room, ENEMY);
          } else if (random_room == 2) {
            room_init(&room, EMPTY);
          } else if (random_room == 3) {
            room_init(&room, TRAP);
          }
        }
      }

      map->list[i * COLS + j] = room;
    }
  }
}

void map_display(Map *map, Vector2 player_position) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (player_position.x == j && player_position.y == i) {
        printf("P ");
      } else {
        switch (map->list[i * COLS + j].room_type) {
          case START:
            printf("S ");
            break;
          case TREASURE:
            printf("T ");
            break;
          default:
            printf(". ");
            break;
        }
      }
    }
    printf("\n");
  }
}

bool map_check_available_room(Map *map, Vector2 room_position) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (map->list[i * COLS + j].position.x == room_position.x &&
          map->list[i * COLS + j].position.y == room_position.y) {
        return true;
      }
    }
  }
  return false;
}