#ifndef CONSTANTS_H
#define CONSTANTS_H

#include "raylib.h"

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600
#define SCREEN_TITLE "Breakout"
#define SCREEN_BACKGROUND RAYWHITE
#define GAME_FPS 60

#define LIVES_LENGTH 10

#define ROWS 5
#define COLS 10
#define BRICK_WIDTH 79
#define BRICK_HEIGHT 30
#define BRICK_GAP 2

#define BRICKS_LENGTH (ROWS * COLS)

#define COLOR_PALLETE {       \
    DARKGRAY, MAROON, DARKGREEN,      \
    SKYBLUE, BEIGE, BROWN,            \
    DARKBROWN, VIOLET, BLACK          \
}

#endif // CONSTANTS_H