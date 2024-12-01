#include "bullet.h"
#include "math.h"
#include "raylib.h"

void initBullet(Bullet *bullet, double x, double y, double target_x,
                double target_y)
{
    bullet->width = 10;
    bullet->height = 10;
    bullet->x = x;
    bullet->y = y;
    bullet->color = RED;
    bullet->speed = 5;

    double distance_x = target_x - bullet->x;
    double distance_y = target_y - bullet->y;
    double distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));
    bullet->direction_x = distance_x / distance;
    bullet->direction_y = distance_y / distance;
}

void drawBullet(Bullet *bullet)
{
    DrawRectangleRec(
        (Rectangle){bullet->x, bullet->y, bullet->width, bullet->height},
        bullet->color);
}

void updateBullet(Bullet *bullet)
{
    bullet->x += bullet->direction_x * bullet->speed;
    bullet->y += bullet->direction_y * bullet->speed;
}