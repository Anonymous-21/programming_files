import raylib as r

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PLATFORMER"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


def encode(text):
    return text.encode("utf-8")


def main():
    r.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)
    
    player_width = 30
    player_height = 30
    player_x = 10
    player_y = r.GetScreenHeight() - player_width
    player_color = r.RED
    player_speed = 8
    player_position = (player_x, player_y)
    
    camera = 
    
    while not r.WindowShouldClose():
        if r.IsKeyDown(r.KEY_RIGHT):
            player_x += player_speed
        elif r.IsKeyDown(r.KEY_LEFT):
            player_x -= player_speed
        elif r.IsKeyDown(r.KEY_UP):
            player_y -= player_speed
        elif r.IsKeyDown(r.KEY_DOWN):
            player_y += player_speed
            
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        
        # r.BeginMode2D()
        
        r.DrawRectangle(player_x,
                        player_y,
                        player_width,
                        player_height,
                        player_color)
        
        # r.EndMode2D()
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()
    