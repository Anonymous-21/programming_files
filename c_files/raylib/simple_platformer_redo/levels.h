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
  bool level1_unlocked;
  int level2[ROW][COL];
  bool level2_unlocked;
  int level3[ROW][COL];
  bool level3_unlocked;
  int level4[ROW][COL];
  bool level4_unlocked;
  int level5[ROW][COL];
  bool level5_unlocked;

} Levels;

void initLevels(Levels *levels);
void drawLevels(Levels *levels);
void updateLevels(Levels *levels);

#endif // LEVELS_H
