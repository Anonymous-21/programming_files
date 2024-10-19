# Variables
CC = gcc
CFLAGS = -Wall -Wextra
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
SRC = main.c player.c obstacles.c
TARGET = endless_runner

# Build rule
build:
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Clean rule
clean:
	rm -f $(TARGET)

# .PHONY targets
.PHONY: build clean

