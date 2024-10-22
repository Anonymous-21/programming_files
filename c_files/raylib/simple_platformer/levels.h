#ifndef LEVELS_H
#define LEVELS_H

#include "raylib.h"

typedef struct Levels {
  int current_level;

} Levels;

void initLevels(Levels *levels);
void drawLevels(Levels *levels);

#endif // LEVELS_H