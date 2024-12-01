#ifndef BULLET_LIST_H
#define BULLET_LIST_H

#include "raylib.h"

typedef struct Bullet Bullet;
typedef struct Player Player;

typedef struct BulletList
{
    Bullet *list;
    int size;
    int capacity;

} BulletList;

void initBulletList(BulletList *bullet_list);
void drawBulletList(BulletList *bullet_list);
void updateBulletList(BulletList *bulluet_list, Player *player);
void freeBulletList(BulletList *bullet_list);

#endif // BULLET_LIST_H