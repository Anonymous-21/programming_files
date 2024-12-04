#include "raylib.h"
#include <math.h>

#include "bullet.h"

void initBullet(Bullet *bullet, double x, double y, double target_x, double target_y)
{
    bullet->x = x;
    bullet->y = y;
    bullet->radius = 5;
    bullet->color = RED;
    bullet->speed = 12;
    bullet->damage = 1;

    double distance_x = target_x - bullet->x;
    double distance_y = target_y - bullet->y;
    double distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));
    bullet->unit_distance_x = distance_x / distance;
    bullet->unit_distance_y = distance_y / distance;
}

void drawBullet(Bullet *bullet)
{
    DrawCircleV((Vector2){bullet->x, bullet->y}, bullet->radius, bullet->color);
}

void updateBullet(Bullet *bullet)
{
    bullet->x += bullet->unit_distance_x * bullet->speed;
    bullet->y += bullet->unit_distance_y * bullet->speed;
}