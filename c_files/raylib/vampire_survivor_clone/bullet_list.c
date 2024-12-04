#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>

#include "bullet_list.h"
#include "bullet.h"
#include "player.h"

void initBulletList(BulletList *bullet_list)
{
    bullet_list->size = 0;
    bullet_list->capacity = 10;
    bullet_list->list = (Bullet *)malloc(bullet_list->capacity * sizeof(Bullet));
    if (bullet_list->list == NULL)
    {
        printf("Bullet list memory not allocated\n");
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
    reallocateMemoryBulletList(bullet_list);

    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
    {
        Bullet bullet;
        initBullet(&bullet,
                   player->x + player->width / 2,
                   player->y + player->height / 2,
                   GetMouseX(),
                   GetMouseY());

        if (bullet_list->list != NULL)
        {
            bullet_list->size++;
            bullet_list->list[bullet_list->size - 1] = bullet;
        }
    }

    for (int i = bullet_list->size - 1; i >= 0; i--)
    {
        updateBullet(&bullet_list->list[i]);

        if (bullet_list->list[i].x < 0 ||
            bullet_list->list[i].x > GetScreenWidth() ||
            bullet_list->list[i].y < 0 ||
            bullet_list->list[i].y > GetScreenHeight())
        {
            for (int j = i; j < bullet_list->size - 1; j++)
            {
                bullet_list->list[j] = bullet_list->list[j + 1];
            }

            bullet_list->list[bullet_list->size - 1] = (Bullet){0};
            bullet_list->size--;
        }
    }
}

void reallocateMemoryBulletList(BulletList *bullet_list)
{
    if (bullet_list->size >= bullet_list->capacity)
    {
        bullet_list->capacity += 10;
        Bullet *new_list = (Bullet *)realloc(bullet_list->list, bullet_list->capacity * sizeof(Bullet));
        if (new_list == NULL)
        {
            printf("Bullet list memory not reallocated\n");
            exit(1);
        }

        bullet_list->list = new_list;
    }
}

void freeMemoryBulletList(BulletList *bullet_list)
{
    free(bullet_list->list);
    bullet_list->list = NULL;
}