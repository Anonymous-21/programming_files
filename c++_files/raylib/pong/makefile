# Variables
CXX = g++                # Change the compiler to g++
CXXFLAGS = -Wall -Wextra -std=c++11  # Add C++ specific flags
LDFLAGS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11  # Linking flags
SRC = main.cpp paddle.cpp ball.cpp    # Add your C++ source files here
TARGET = pong # Your desired executable name

# Build rule
build:
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Clean rule
clean:
	rm -f $(TARGET)

# .PHONY targets
.PHONY: build clean

