import pyray as p

class Bricks:
    def __init__(self) -> None:
        self.rows = 5
        self.cols = 10
        self.width = 50  # Adjust width for visibility
        self.height = 20  # Adjust height for visibility
        self.list = []
        self.color_num = 1
        
        self.update_colors()
        self.gen_grid()  # Initialize the grid once
        
    def update_colors(self):
        match self.color_num:
            case 1:
                self.color = p.RED
            case 2:
                self.color = p.BLUE
            case 3:
                self.color = p.GREEN
            case 4:
                self.color = p.YELLOW
            case 5:
                self.color = p.PURPLE
                
    def gen_grid(self):
        self.list = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                x = j * (self.width + 5)  # Add spacing between bricks
                y = i * (self.height + 5)  # Add spacing between rows
                row.append((x, y))
            self.list.append(row)
            
    def draw(self):
        for row in self.list:
            for brick in row:
                rect = p.Rectangle(brick[0], brick[1], self.width, self.height)
                p.draw_rectangle_rec(rect, self.color)
                
            self.color_num += 1
            if self.color_num > 5:
                self.color_num = 1
            self.update_colors()

# Main game loop
def main():
    p.init_window(800, 600, "Bricks Example")  # Initialize window
    p.set_target_fps(60)  # Set the target frames per second
    
    bricks = Bricks()  # Create a Bricks instance

    while not p.window_should_close():  # Main game loop
        p.begin_drawing()
        p.clear_background(p.WHITE)  # Clear the background
        
        bricks.draw()  # Draw the bricks
        
        p.end_drawing()

    p.close_window()  # Close the window

if __name__ == "__main__":
    main()
