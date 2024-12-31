# Compiler and linker settings
CXX = g++
CXXFLAGS = -std=c++17 -Wall
LDFLAGS = -lraylib -lm -lpthread -ldl -lrt -lX11

# Source files and output
SRC = main.cpp
OBJ = $(SRC:.cpp=.o)
OUT = game

# Default target
all: $(OUT)

# Linking step
$(OUT): $(OBJ)
	$(CXX) $(OBJ) -o $(OUT) $(LDFLAGS)

# Compiling step
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up
clean:
	rm -f $(OBJ) $(OUT)

# Run the game
run: $(OUT)
	./$(OUT)
