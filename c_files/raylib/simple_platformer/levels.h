#ifndef LEVELS_H
#define LEVELS_H

#include "raylib.h"

#define ROW 20
#define COL 20

typedef struct Levels {
  int block_size;
  int current_level;
  int (*level)[COL];
  int level1[ROW][COL];

} Levels;

void initLevels(Levels *levels);
void drawLevels(Levels *levels);
void updateLevels(Levels *levels);

#endif // LEVELS_H
