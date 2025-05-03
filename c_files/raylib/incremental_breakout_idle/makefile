# Compiler and flags
CC = gcc
CFLAGS = -Wall -std=c99 -O2
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11

# Source and output
SRC = main.c bricks.c balls.c
OUT = game

# Build target
all: $(OUT)

$(OUT): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(OUT) $(LDFLAGS)

# Clean target
clean:
	rm -f $(OUT)
