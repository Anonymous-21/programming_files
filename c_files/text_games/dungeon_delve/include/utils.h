#ifndef UTILS_H
#define UTILS_H

#include <ctype.h>
#include <string.h>

typedef struct Vector2 {
  int x;
  int y;

} Vector2;

void lstrip(char *str);
void rstrip(char *str);
void strip(char *str);


#endif  // UTILS_H