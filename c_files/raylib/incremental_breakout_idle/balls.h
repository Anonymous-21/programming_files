#ifndef BALLS_h
#define BALLS_H

#include <raylib.h>

typedef enum BallType
{
  BALL_NORMAL,
  BALL_AGILE,
  BALL_HEAVY,
  BALL_SPLITTER,
  BALL_HOMING

} BallType;

typedef struct Ball
{
  Vector2 pos;
  float radius;
  Vector2 direction;
  float speed;
  int damage;
  Color color;
  BallType type;

} Ball;

void ball_init(Ball *ball, float radius, float speed, int damage, Color color, BallType type);
void ball_draw(Ball *ball);
void ball_update(Ball *ball);

void ball_normal_init(Ball *ball);
void ball_normal_draw(Ball *ball);
void ball_normal_update(Ball *ball);

void ball_agile_init(Ball *ball);
void ball_agile_draw(Ball *ball);
void ball_agile_update(Ball *ball);

void ball_heavy_init(Ball *ball);
void ball_heavy_draw(Ball *ball);
void ball_heavy_update(Ball *ball);

void ball_splitter_init(Ball *ball);
void ball_splitter_draw(Ball *ball);
void ball_splitter_update(Ball *ball);

void ball_homing_init(Ball *ball);
void ball_homing_draw(Ball *ball);
void ball_homing_update(Ball *ball);

#endif // BALLS_H