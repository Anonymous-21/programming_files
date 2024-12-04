#ifndef COLLISION_HANDLER_H
#define COLLISION_HANDLER_H

typedef struct Player Player;
typedef struct BulletList BulletList;
typedef struct EnemyList EnemyList;

void playerCollisionEnemy(EnemyList *enemy_list, Player *player);
void bulletCollisionEnemy(EnemyList *enemy_list, BulletList *bullet_list);

#endif