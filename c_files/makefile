# Compiler and linker settings
CC = gcc
CFLAGS = -Wall -std=c11 -O2
LDFLAGS = -lraylib -lm -lpthread -ldl -lrt -lX11

# Directories
SRCDIR = src
BINDIR = bin
OBJDIR = obj
INCDIR = include

# Files
SRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(SRC:$(SRCDIR)/%.c=$(OBJDIR)/%.o)
TARGET = $(BINDIR)/game

# Default target
all: $(TARGET)

# Create necessary directories
$(OBJDIR):
	mkdir -p $(OBJDIR)

$(BINDIR):
	mkdir -p $(BINDIR)

# Link the game executable
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(LDFLAGS)

# Compile each source file to object file
$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -I$(INCDIR) -c $< -o $@

# Clean up generated files
clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)
