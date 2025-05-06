# Compiler and flags
CXX := g++
CXXFLAGS := -Wall -Wextra -std=c++17 -Iinclude

# Directories
SRC_DIR := src
OBJ_DIR := obj
INC_DIR := include
BIN := program

# Find all .cpp files and corresponding .o files
SRCS := $(wildcard $(SRC_DIR)/*.cpp)
OBJS := $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRCS))

# Default target
all: $(BIN)

# Link object files into the final binary
$(BIN): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files into object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean target
clean:
	rm -rf $(OBJ_DIR)/*.o $(BIN)

.PHONY: all clean
