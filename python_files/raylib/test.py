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
    ground_level = r.GetScreenHeight() - player_height
    player_x = 10
    player_y = ground_level
    player_color = r.BLUE
    player_change_x = 8
    player_change_y = 0
    jump_force = -20
    gravity = 1
    is_jumping = False
    can_jump = True
    
    platform_x = r.GetScreenWidth()//2
    platform_y = r.GetScreenHeight()//2 + 150
    platform_width = 200
    platform_height = 10
    platform_color = r.GRAY
    
    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        
        # draw player
        r.DrawRectangle(player_x,
                        player_y,
                        player_width,
                        player_height,
                        player_color)

        # draw platform
        r.DrawRectangle(platform_x,
                        platform_y,
                        platform_width,
                        platform_height,
                        platform_color)
        
        # player movement and jump
        if r.IsKeyDown(r.KEY_RIGHT) and player_x <= r.GetScreenWidth() - player_width:
            player_x += player_change_x
        elif r.IsKeyDown(r.KEY_LEFT) and player_x >= 0:
            player_x -= player_change_x
        elif r.IsKeyPressed(r.KEY_UP) and can_jump:
            player_change_y = jump_force
            is_jumping = True
        
        if is_jumping:
            player_change_y += gravity
            player_y += player_change_y
            can_jump = False
    
        if player_y >= ground_level:
            player_y = ground_level
            can_jump = True
            
        # platform collision
        if player_y + player_width >= platform_y:
            if r.CheckCollisionRecs((player_x,
                                     player_y,
                                     player_width,
                                     player_height),
                                    (platform_x,
                                     platform_y,
                                     platform_width,
                                     platform_height)):
                can_jump = True
                
                if not (r.IsKeyDown(r.KEY_DOWN) or r.IsKeyPressed(r.KEY_DOWN)) and can_jump:         
                    player_y = platform_y - player_height
                    player_change_y = 0
        
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()
    