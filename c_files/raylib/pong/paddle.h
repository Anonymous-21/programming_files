#ifndef PLAYER_H
#define PLAYER_H

#include "raylib.h"

void draw_paddle();

void draw_paddle(int x, int y, int width, int height, Color color)
{
  DrawRectangle(x, y, width, height, color);
}

typedef struct Paddle
{
  int x;
  int y;
  int width = 10;
  int height = 100;
  Color color = BLACK;
}Paddle;
