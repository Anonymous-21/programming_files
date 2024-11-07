import pyray as p
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEST WINDOW"
SCREEN_BACKGROUND = p.RAYWHITE
GAME_FPS = 60


p.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
p.set_target_fps(GAME_FPS)

player_x = p.get_mouse_x()
player_y = p.get_mouse_y()
player_width = 30
player_height = 30
player_color = p.BLUE

follower_x = 100
follower_y = 100
follower_width = 20
follower_height = 20
follower_color = p.RED
follower_speed = 3

while not p.window_should_close():
    p.hide_cursor()
    
    player_x = p.get_mouse_x()
    player_y = p.get_mouse_y()
    
    distance_x = player_x - follower_x
    distance_y = player_y - follower_y
    distance = math.sqrt(distance_x**2 + distance_y**2)
    
    if distance > 0:
        distance_x /= distance
        distance_y /= distance
        follower_x += distance_x * follower_speed
        follower_y += distance_y * follower_speed
    
    p.begin_drawing()
    p.clear_background(SCREEN_BACKGROUND)
    
    p.draw_rectangle_rec((player_x, player_y, player_width, player_height), player_color)
    p.draw_rectangle_rec((follower_x, follower_y, follower_width, follower_height), follower_color)
    
    p.end_drawing()
    
p.close_window()