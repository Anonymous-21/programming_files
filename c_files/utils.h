#ifndef UTILS_H
#define UTILS_H

static inline float max_float(float x, float y)
{
    return (x > y) ? x : y;
}
static inline float min_float(float x, float y)
{
    return (x < y) ? x : y;
}
static inline int max_int(int x, int y)
{
    return (x > y) ? x : y;
}
static inline int min_int(int x, int y)
{
    return (x < y) ? x : y;
}

#endif // UTILS_H