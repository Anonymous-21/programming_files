const r = require("raylib");

const screenWidth = 800;
const screenHeight = 600;
const screenTitle = "Pong";
const screenBackground = r.SKYBLUE;
const gameFps = 60;

/*
    PADDLE
*/
class Paddle {
  constructor(x) {
    this.width = 10;
    this.height = 100;
    this.initial_x = x;
    this.initial_y = r.GetScreenHeight() / 2 - this.height / 2;
    this.x = this.initial_x;
    this.y = this.initial_y;
    this.color = r.BLACK;
    this.speed = 5;
    this.ai_speed = 7;
  }

  reset() {
    this.x = this.initial_x;
    this.y = this.initial_y;
  }

  draw() {
    r.DrawRectangle(this.x, this.y, this.width, this.height, this.color);
  }

  update() {
    if (r.IsKeyDown(r.KEY_W) && this.y >= 0) {
      this.y -= this.speed;
    } else if (
      r.IsKeyDown(r.KEY_S) &&
      this.y <= r.GetScreenHeight() - this.height
    ) {
      this.y += this.speed;
    }
  }

  ai_update(ball) {
    if (ball.x > r.GetScreenWidth() / 2) {
      let distance_x = ball.x - (this.x + this.width / 2);
      let distance_y = ball.y - (this.y + this.height / 2);
      let distance = Math.sqrt(distance_x ** 2 + distance_y ** 2);

      if (distance > 0) {
        distance_y /= distance;

        this.y += distance_y * this.ai_speed;
      }
    }
  }
}

/*
    BALL
*/
class ball {
  constructor() {
    this.initial_x = r.GetScreenWidth() / 2;
    this.initial_y = r.GetScreenHeight() / 2;
    this.x = this.initial_x;
    this.y = this.initial_y;
    this.radius = 10;
    this.color = r.RED;
    this.initial_speed_x = 5;
    this.initial_speed_y = 6;
    this.speed_x = this.initial_speed_x;
    this.speed_y = this.initial_speed_y;
    this.speed_interval = 0.005;
    this.frames_counter = 0;
  }

  reset() {
    this.x = this.initial_x;
    this.y = this.initial_y;
    this.speed_x = this.initial_speed_x;
    this.speed_y = this.initial_speed_y;
    this.speed_x *= -1;
    this.frames_counter = 0;
  }

  draw() {
    r.DrawCircleV(r.Vector2(this.x, this.y), this.radius, this.color);
  }

  update() {
    this.frames_counter++;
    if (this.frames_counter >= 60) {
      this.frames_counter = 61;

      this.x += this.speed_x;
      this.y += this.speed_y;

      this.speed_x += this.speed_interval;
      this.speed_y += this.speed_interval;
    }

    if (this.y <= this.radius || this.y >= r.GetScreenHeight() - this.radius) {
      this.speed_y *= -1;
    }
  }
}

/*
    GAME
*/
class Game {
  constructor() {
    this.score_left = 0;
    this.score_right = 0;

    this.paddle_left = new Paddle(10);
    this.ai = new Paddle(r.GetScreenWidth() - this.paddle_left.width - 10);
    this.ball = new ball();
  }

  reset() {
    this.paddle_left.reset();
    this.ai.reset();
    this.ball.reset();
  }

  draw() {
    // draw scores
    r.DrawText(String(this.score_left), 200, 20, 40, r.BLACK);
    r.DrawText(
      String(this.score_right),
      r.GetScreenWidth() - 220,
      20,
      40,
      r.BLACK
    );

    this.paddle_left.draw();
    this.ai.draw();
    this.ball.draw();
  }

  update() {
    this.paddle_left.update();
    this.ai.ai_update(this.ball);
    this.ball.update();

    // ball collision paddle
    if (
      r.CheckCollisionCircleRec(
        r.Vector2(this.ball.x, this.ball.y),
        this.ball.radius,
        r.Rectangle(
          this.paddle_left.x,
          this.paddle_left.y,
          this.paddle_left.width,
          this.paddle_left.height
        )
      )
    ) {
      this.ball.speed_x *= -1;
    } else if (
      r.CheckCollisionCircleRec(
        r.Vector2(this.ball.x, this.ball.y),
        this.ball.radius,
        r.Rectangle(this.ai.x, this.ai.y, this.ai.width, this.ai.height)
      )
    ) {
      this.ball.speed_x *= -1;
    }

    // update score
    if (this.ball.x < 0) {
      this.score_right++;
      this.reset();
    } else if (this.ball.x > r.GetScreenWidth()) {
      this.score_left++;
      this.reset();
    }
  }
}

/*
    RAYLIB WINDOW
*/
function init() {
  r.InitWindow(screenWidth, screenHeight, screenTitle);
  r.SetTargetFPS(gameFps);

  const game = new Game();

  while (!r.WindowShouldClose()) {
    r.BeginDrawing();
    r.ClearBackground(screenBackground);

    game.draw();
    game.update();

    r.EndDrawing();
  }

  r.CloseWindow();
}

init();
