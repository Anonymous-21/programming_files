import raylib as r

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PLATFORMER"
SCREEN_BACKGROUND = r.RAYWHITE
GAME_FPS = 60


def encode(text):
    return text.encode("utf-8")


class Camera:
    def __init__(self, target, offset, rotation, zoom) -> None:
        self.target = target
        self.offset = offset
        self.rotation = rotation
        self.zoom = zoom
        

def main():
    r.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, encode(SCREEN_TITLE))
    r.SetTargetFPS(GAME_FPS)
    
    player_width = 30
    player_height = 30
    player_x = 0
    player_y = 0
    player_color = r.RED
    player_speed = 8
    
    camera = Camera(target=[player_x + 20, player_y +20],
                      offset=[SCREEN_WIDTH/2, SCREEN_HEIGHT/2],
                      rotation=0,
                      zoom=1)
            
    while not r.WindowShouldClose():
        
        if r.IsKeyDown(r.KEY_UP):
            player_y -= player_speed
        elif r.IsKeyDown(r.KEY_DOWN):
            player_y += player_speed
        elif r.IsKeyDown(r.KEY_RIGHT):
            player_x += player_speed
        elif r.IsKeyDown(r.KEY_LEFT):
            player_x -= player_speed
            
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        
        r.BeginMode2D(camera)
        
        r.DrawRectangle(player_x,
                        player_y,
                        player_width,
                        player_height,
                        player_color)
        
        r.EndMode2D()
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()
    