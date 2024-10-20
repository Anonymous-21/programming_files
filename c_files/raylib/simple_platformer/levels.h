#ifndef LEVELS_H
#define LEVELS_H

#include "raylib.h"

#define ROW 20
#define COL 20

typedef struct Levels{

  int current_level;
  int block_size;
  int (*level)[COL];
  int level1[ROW][COL];
  int level2[ROW][COL];
  int level3[ROW][COL];
  int level4[ROW][COL];
  int level5[ROW][COL];

} Levels;

void initLevels(Levels *levels);
void drawLevels(Levels *levels);
void updateLevels(Levels *levels);

#endif // LEVELS_H
