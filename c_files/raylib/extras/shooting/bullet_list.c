#include <stdlib.h>
#include <stdio.h>

#include "raylib.h"

#include "bullet_list.h"
#include "bullet.h"
#include "player.h"

void initBulletList(BulletList *bullet_list)
{
    bullet_list->size = 0;
    bullet_list->capacity = 1;
    bullet_list->list = (Bullet *)malloc(bullet_list->capacity * sizeof(Bullet));
    if (bullet_list->list == NULL)
    {
        printf("Memory not allocated\n");
        exit(1);
    }
}

void drawBulletList(BulletList *bullet_list)
{
    for (int i = 0; i < bullet_list->size; i++)
    {
        drawBullet(&bullet_list->list[i]);
    }
}

void updateBulletList(BulletList *bullet_list, Player *player)
{
    if (IsMouseButtonDown(MOUSE_LEFT_BUTTON))
    {
        // reallocated memory if not enough
        if (bullet_list->size >= bullet_list->capacity)
        {
            bullet_list->capacity += 10;
            bullet_list->list = (Bullet *)realloc(bullet_list->list,
                                                  bullet_list->capacity * sizeof(Bullet));
            if (bullet_list->list == NULL)
            {
                printf("Memory not reallocated\n");
                exit(1);
            }
        }

        // add bullet to list
        Bullet bullet;
        initBullet(&bullet,
                   player->x + player->width / 2,
                   player->y + player->height / 2,
                   GetMouseX(),
                   GetMouseY());

        bullet_list->size++;
        bullet_list->list[bullet_list->size - 1] = bullet;
    }

    for (int i = bullet_list->size - 1; i >= 0; i--)
    {
        updateBullet(&bullet_list->list[i]);

        if (bullet_list->list[i].x <= 0 ||
            bullet_list->list[i].x >= GetScreenWidth() ||
            bullet_list->list[i].y <= 0 ||
            bullet_list->list[i].y >= GetScreenHeight())
        {
            for (int j = i; j < bullet_list->size - 1; j++)
            {
                bullet_list->list[j] = bullet_list->list[j + 1];
            }
            
            bullet_list->size--;    
        }
    }
}

void freeBulletList(BulletList *bullet_list)
{
    free(bullet_list->list);
}