# Compiler and linker
CC = gcc
CFLAGS = -Wall -Werror -g -lxml2

# Raylib paths (adjust these if necessary)
RAYLIB_PATH = /usr/local/include
RAYLIB_LIB_PATH = /usr/local/lib
RAYLIB_LIBS = -lraylib -lm -lpthread -ldl -lrt -lX11 -lGL

# Source files
SRCS = main.c player.c bullet.c bullet_list.c enemy.c enemy_list.c

# Output binary name
TARGET = game

# Create object files from source files
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Link object files to create executable
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET) $(CFLAGS) -L$(RAYLIB_LIB_PATH) $(RAYLIB_LIBS)

# Compile .c files into .o files
%.o: %.c
	$(CC) -c $< -o $@ $(CFLAGS) -I$(RAYLIB_PATH)

# Clean object and executable files
clean:
	rm -f $(OBJS) $(TARGET)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Phony targets
.PHONY: all clean run
