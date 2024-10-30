# /// script
# dependencies = [
#     "cffi",
#     "raylib"
# ]
# ///

import asyncio
from pyray import *

async def main():  # You must have an async main function
    init_window(500, 500, "Hello")
    set_target_fps(60)  # Set the target frames per second
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        end_drawing()
        await asyncio.sleep(0)  # You must call this in your main loop
    close_window()

asyncio.run(main())
