# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2 -lm

# Raylib configuration
RAYLIB_FLAGS = -lraylib -lm -ldl -lpthread -lGL -lX11

# Source files and output
SRC = shooting.c 
OBJ = $(SRC:.c=.o)
TARGET = shooting

# Rules
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $@ $(RAYLIB_FLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

.PHONY: all clean

