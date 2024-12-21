# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2 -lm -g

# Raylib configuration
RAYLIB_FLAGS = -lraylib -lm -ldl -lpthread -lGL -lX11

# Default source and target
SRC = $(SOURCE)
TARGET = $(OUTPUT)

# Check if SOURCE and OUTPUT are set, otherwise use defaults
ifeq ($(SOURCE),)
    $(error SOURCE variable not set)
endif

ifeq ($(OUTPUT),)
    OUTPUT = $(basename $(SOURCE))
endif

# Object file based on the source file
OBJ = $(SRC:.c=.o)

# Rules
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $@ $(RAYLIB_FLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
