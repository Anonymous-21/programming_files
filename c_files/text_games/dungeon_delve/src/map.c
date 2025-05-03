#include "map.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "rooms.h"
#include "utils.h"

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

        if (random_num > 95) {
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

void map_draw(Map *map) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
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
    printf("\n");
  }
}