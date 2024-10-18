# Variables
CC = gcc
CFLAGS = -Wall
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
SRC = main.c paddle.c ball.c 
TARGET = pong

# Build rule
build:
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Clean rule
clean:
	rm -f $(TARGET)

# .PHONY targets
.PHONY: build clean

