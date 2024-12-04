#ifndef ENEMY_H
#define ENEMY_H

#include "raylib.h"

typedef struct Player Player;
typedef struct Enemy
{
    double x;
    double y;
    double width;
    double height;
    Color initial_color;
    Color color;
    double speed;
    double damage;
    double health;

} Enemy;

void initEnemy(Enemy *enemy, Player *player);
Vector2 genEnemySpawnCoordinates(Player *player);
void drawEnemy(Enemy *enemy);
void updateEnemy(Enemy *enemy, Player *player);

#endif