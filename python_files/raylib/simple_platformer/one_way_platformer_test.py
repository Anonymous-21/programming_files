import pyray as p


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEST"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


class Game:
    def __init__(self) -> None:
        self.player_width = 30
        self.player_height = 30
        self.ground_level = p.get_screen_height() - self.player_height
        self.player_x = 10
        self.player_y = self.ground_level
        self.player_color = p.BLUE
        self.player_change_x = 8
        self.player_change_y = 0
        self.player_gravity = 1
        self.player_jump_force = -20
        self.player_can_jump = True
        
        self.platform_x = 400
        self.platform_y = 450
        self.platform_width = 200
        self.platform_height = 10
        self.platform_color = p.BLACK
    
    def draw(self):
        p.draw_rectangle_rec((self.player_x, self.player_y, self.player_width, self.player_height), self.player_color)
        
        p.draw_rectangle_rec((self.platform_x, self.platform_y, self.platform_width, self.platform_height), self.platform_color)
        
    def update(self):
        if p.is_key_down(p.KeyboardKey.KEY_RIGHT) and self.player_x <= p.get_screen_width() - self.player_width:
            self.player_x += self.player_change_x
        elif p.is_key_down(p.KeyboardKey.KEY_LEFT) and self.player_x >= 0:
            self.player_x -= self.player_change_x  
            
        # player jump
        if p.is_key_pressed(p.KeyboardKey.KEY_UP) and self.player_can_jump:
            self.player_change_y = self.player_jump_force
            self.player_can_jump = False
            
        self.player_change_y += self.player_gravity
        self.player_y += self.player_change_y
    
        # player collision ground
        if self.player_y >= self.ground_level:
            self.player_y = self.ground_level
            self.player_can_jump = True
            
        # player collision platform
        if self.player_y <= self.platform_y - self.player_height:
            if p.check_collision_recs((self.player_x, self.player_y, self.player_width, self.player_height), (self.platform_x, self.platform_y, self.platform_width, self.platform_height)):
                if self.player_change_y > 0:
                    self.player_change_y = 0
                self.player_y = self.platform_y - self.player_height
                self.player_can_jump = True
            

def main():
    p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    p.set_target_fps(GAME_FPS)
    
    game = Game()
    
    while not p.window_should_close():
        p.begin_drawing()
        p.clear_background(SCREEN_BACKGROUND)
        
        game.draw()
        game.update()
        
        p.end_drawing()
        
    p.close_window()
    

if __name__ == "__main__":
    main()
    