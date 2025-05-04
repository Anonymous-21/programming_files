# Compiler and linker settings
CC = gcc
CFLAGS = -Wall -g -Iinclude  # -Iinclude to specify the directory for header files

# Target executable
TARGET = game

# Directories for source, object files, and headers
SRC_DIR = src
INCLUDE_DIR = include
OBJ_DIR = obj

# Find all .c files in the src directory
SRC = $(wildcard $(SRC_DIR)/*.c)

# Object files (change extension to .obj and store them in the obj folder)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Default target
all: $(TARGET)

# Rule to create the executable
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET)

# Rule to compile .c files into .obj (object files)
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)  # Ensure the obj directory exists
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up compiled files
clean:
	rm -rf $(OBJ_DIR) $(TARGET)

