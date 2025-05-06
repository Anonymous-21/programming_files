#include "utils.h"

// strip whitespaces left
void lstrip(char *str) {
  char *start = str;

  while (isspace((unsigned char)*start)) {
    start++;
  }

  if (start != str) {
    memmove(str, start, strlen(start) + 1);
  }
}

// strip whitespaces right
void rstrip(char *str) {
  char *end = str + strlen(str) - 1;
  while (end >= str && isspace((unsigned char)*end)) {
    *end = '\0';
    end--;
  }
}

// strip whitespaces left + right
void strip(char *str) {
  lstrip(str);
  rstrip(str);
}