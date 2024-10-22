#ifndef LEVELS_H
#define LEVELS_H

#include "raylib.h"

#define ROW 20
#define COL 20

typedef struct Levels {

  int current_level;
  int block_size;
  int (*level)[COL];
  int level1_locked[ROW][COL];
  int level1_unlocked[ROW][COL];
  bool level1_pass;
  int level2_locked[ROW][COL];
  int level2_unlocked[ROW][COL];
  bool level2_pass;
  int level3_locked[ROW][COL];
  int level3_unlocked[ROW][COL];
  bool level3_pass;
  int level4_locked[ROW][COL];
  int level4_unlocked[ROW][COL];
  bool level4_pass;
  int level5_locked[ROW][COL];
  int level5_unlocked[ROW][COL];
  bool level5_pass;

} Levels;

void initLevels(Levels *levels);
void drawLevels(Levels *levels);
void updateLevels(Levels *levels);

#endif // LEVELS_H
