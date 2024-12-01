#ifndef BULLET_H
#define BULLET_H

#include "raylib.h"

typedef struct Bullet
{
    double x;
    double y;
    double width;
    double height;
    Color color;
    double speed;
    double direction_x;
    double direction_y;

} Bullet;

void initBullet(Bullet *bullet, double x, double y, double target_x,
                double target_y);
void drawBullet(Bullet *bullet);
void updateBullet(Bullet *bullet);

#endif // BULLET_H