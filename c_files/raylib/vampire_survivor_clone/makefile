# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2 -lm -g

# Raylib configuration
RAYLIB_FLAGS = -lraylib -lm -ldl -lpthread -lGL -lX11

# Source files and output
SRC = main.c player.c enemy.c enemy_list.c bullet.c bullet_list.c collision_handler.c
OBJ = $(SRC:.c=.o)
TARGET = game

# Rules
all: $(TARGET)
	$(RM) $(OBJ)  # Clean up object files after build

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $@ $(RAYLIB_FLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
