# Variables
CC = gcc
CFLAGS = -Wall -Wextra
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
SRC = main.c ui.c collision_handler.c snake.c food.c
TARGET = snake

# Build rule
build:
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Clean rule
clean:
	rm -f $(TARGET)

# .PHONY targets
.PHONY: build clean

