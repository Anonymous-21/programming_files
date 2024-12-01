# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2

# Raylib configuration
RAYLIB_FLAGS = -lraylib -lm -ldl -lpthread -lGL -lX11

# Source files and output
SRC = main.c 
OBJ = $(SRC:.c=.o)
TARGET = game

# Rules
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $@ $(RAYLIB_FLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

.PHONY: all clean

