#ifndef UI_H
#define UI_H

#include "raylib.h"
#include "constants.h"

void drawOutline();
void drawScore(char score_str[SCORE_LENGTH]);
void drawMainMenu(bool highlight_play_button,
                  bool highlight_quit_button);
void drawGameOverMenu();
void drawGameWonMenu();

#endif // UI_H