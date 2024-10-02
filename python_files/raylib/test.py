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
    
    while not r.WindowShouldClose():
        r.BeginDrawing()
        r.ClearBackground(SCREEN_BACKGROUND)
        r.EndDrawing()
        
    r.CloseWindow()
    

if __name__ == "__main__":
    main()
    