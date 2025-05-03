#include <raylib.h>
#include <stdio.h>

#define ROWS 5
#define COLS 5
#define SLOT_SIZE 80
#define SLOT_GAP 5

#define iITEMS_SIZE 5

typedef struct Item
{
  int id;
  Rectangle rect;
  Color color;
  Vector2 offset;
  bool dragging;

} Item;

typedef struct Items
{
  Item list[iITEMS_SIZE];
  int used;

} Items;

typedef struct Inventory
{
  Item list[ROWS * COLS];
  int used;
  bool active;

} Inventory;

int main(void)
{
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const char SCREEN_TITLE[] = "Inventory";
  const Color SCREEN_BACKGROUND = RAYWHITE;

  InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE);

  Vector2 pos = (Vector2){10, 10};

  Rectangle slots[ROWS * COLS];
  for (int i = 0; i < ROWS; i++)
  {
    for (int j = 0; j < COLS; j++)
    {
      int x = j * (SLOT_SIZE + SLOT_GAP) + pos.x;
      int y = i * (SLOT_SIZE + SLOT_GAP) + pos.y;

      slots[i * COLS + j] = (Rectangle){x, y, SLOT_SIZE, SLOT_SIZE};
    }
  }

  Inventory inventory;
  inventory.active = true;
  inventory.used = 0;

  Items items;
  items.used = 0;

  for (int i = 0; i < iITEMS_SIZE; i++)
  {
    Item item;
    item.id = i;
    item.rect = (Rectangle){600, (i + 1) * 70, 50, 50};
    item.color = (Color){
        GetRandomValue(0, 255),
        GetRandomValue(0, 255),
        GetRandomValue(0, 255),
        255,
    };
    item.offset = (Vector2){0, 0};
    item.dragging = false;

    items.list[i] = item;
    items.used++;
  }

  float last_current_time = 0.0f;
  float print_interval = 1.0f;

  while (!WindowShouldClose())
  {
    // activate-deactivate inventory
    if (IsKeyPressed(KEY_I))
    {
      inventory.active = !inventory.active;
    }

    Vector2 mouse_pos = GetMousePosition();

    // inventory list
    for (int i = 0; i < inventory.used; i++)
    {
      if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
      {
        if (CheckCollisionPointRec(mouse_pos, inventory.list[i].rect) && !inventory.list[i].dragging)
        {
          inventory.list[i].dragging = true;
          inventory.list[i].offset.x = mouse_pos.x - inventory.list[i].rect.x;
          inventory.list[i].offset.y = mouse_pos.y - inventory.list[i].rect.y;

          // add item to inventory
          if (items.used < iITEMS_SIZE)
          {
            items.list[items.used] = inventory.list[i];
            items.used++;
          }

          // remove item from inventory
          if (inventory.used > 0)
          {
            for (int j = i; j < inventory.used; j++)
            {
              inventory.list[j] = inventory.list[j + 1];
            }
            inventory.used--;
          }
        }
      }
    }

    // handle dragging
    for (int i = 0; i < items.used; i++)
    {
      if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
      {
        if (CheckCollisionPointRec(mouse_pos, items.list[i].rect) && !items.list[i].dragging)
        {
          items.list[i].dragging = true;
          items.list[i].offset.x = mouse_pos.x - items.list[i].rect.x;
          items.list[i].offset.y = mouse_pos.y - items.list[i].rect.y;
        }
      }

      if (items.list[i].dragging)
      {
        items.list[i].rect.x = mouse_pos.x - items.list[i].offset.x;
        items.list[i].rect.y = mouse_pos.y - items.list[i].offset.y;

        if (IsMouseButtonReleased(MOUSE_LEFT_BUTTON))
        {
          items.list[i].dragging = false;

          for (int j = 0; j < ROWS * COLS; j++)
          {
            if (CheckCollisionRecs(items.list[i].rect, slots[j]))
            {
              // snap item to slot
              items.list[i].rect.x = slots[j].x + (slots[j].width - items.list[i].rect.width) / 2;
              items.list[i].rect.y = slots[j].y + (slots[j].height - items.list[i].rect.height) / 2;

              // add item to inventory
              if (inventory.used < ROWS * COLS)
              {
                inventory.list[inventory.used] = items.list[i];
                inventory.used++;
              }

              // remove item from items list
              if (items.used > 0)
              {
                for (int k = i; k < items.used; k++)
                {
                  items.list[k] = items.list[k + 1];
                }
                items.used--;
              }

              break;
            }
          }
        }
      }
    }

    // debug print statements
    float current_time = GetTime();
    if (current_time - last_current_time > print_interval)
    {
      last_current_time = current_time;

      printf("\nTime: %f\n", current_time);
      printf("\nItems: \n");
      for (int i = 0; i < items.used; i++)
      {
        printf("Id: %d\nX: %.2f\nY: %.2f\n", items.list[i].id,
               items.list[i].rect.x,
               items.list[i].rect.y);
      }
      printf("\nInventory: \n");
      for (int i = 0; i < inventory.used; i++)
      {
        printf("Id: %d\nX: %.2f\nY: %.2f\n", inventory.list[i].id,
               inventory.list[i].rect.x,
               inventory.list[i].rect.y);
      }
    }

    BeginDrawing();
    ClearBackground(SCREEN_BACKGROUND);

    for (int i = 0; i < items.used; i++)
    {
      DrawRectangleRec(items.list[i].rect, items.list[i].color);
    }

    if (inventory.active)
    {
      // draw slots
      for (int i = 0; i < ROWS * COLS; i++)
      {
        Color slot_color = CheckCollisionPointRec(mouse_pos, slots[i]) ? RED : BLACK;

        DrawRectangleLinesEx(slots[i], 5, slot_color);
      }

      // draw inventory items
      for (int i = 0; i < inventory.used; i++)
      {
        DrawRectangleRec(inventory.list[i].rect, inventory.list[i].color);
      }
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}