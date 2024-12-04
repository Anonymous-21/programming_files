#ifndef BULLET_LIST_H
#define BULLET_LIST_H

#include "raylib.h"

typedef struct Player Player;
typedef struct Bullet Bullet;

typedef struct BulletList
{
    Bullet *list;
    int size;
    int capacity;

} BulletList;

void initBulletList(BulletList *bullet_list);
void drawBulletList(BulletList *bullet_list);
void updateBulletList(BulletList *bullet_list, Player *player);

void reallocateMemoryBulletList(BulletList *bullet_list);
void freeMemoryBulletList(BulletList *bullet_list);

#endif