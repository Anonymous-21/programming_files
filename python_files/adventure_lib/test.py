from adventurelib import Room, Item, when

# Create rooms
room1 = Room("A small dark room with a single door to the north.")
room2 = Room("A bright hallway with paintings on the walls.")

# Add items attribute to rooms
room1.items = []  # Initialize an empty list of items for room1
room2.items = []  # Initialize an empty list of items for room2

# Define items
sword = Item("sword", "A sharp steel sword.")
shield = Item("shield", "A sturdy wooden shield.")
key = Item("key", "A rusty old key.")

# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []  # The player's inventory will be a list of items
        self.current_room = room1  # The player starts in room1

    def move(self, direction):
        if direction == "north" and hasattr(self.current_room, "north"):
            self.current_room = self.current_room.north
            print(f"You move north to {self.current_room.description}")
        elif direction == "south" and hasattr(self.current_room, "south"):
            self.current_room = self.current_room.south
            print(f"You move south to {self.current_room.description}")
        else:
            print(f"You can't go that way.")

    def take(self, item):
        """Take an item from the room and add it to the player's inventory."""
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You picked up the {item.name}.")
        else:
            print(f"There is no {item.name} here.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    def use(self, item):
        """Use an item from the player's inventory."""
        if item in self.inventory:
            print(f"You use the {item.name}.")
        else:
            print(f"You don't have a {item.name}.")

# Create player
player = Player("Hero")

# Set up inventory
player.inventory.append(sword)
player.inventory.append(shield)

# NPCs are represented as items (or objects)
class NPC(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.is_npc = True
        self.inventory = []  # NPC has its own inventory

    def interact(self):
        print(f"You talk to {self.name}: '{self.description}'")

# Create NPC (Non-Player Character)
goblin = NPC("Goblin", "A small, green goblin with a wicked smile.")
goblin.inventory.append(key)  # Goblin has the rusty key

# Room connections
room1.north = room2
room2.south = room1

# Place items and NPC in room1
room1.items.append(sword)
room1.items.append(shield)
room1.items.append(goblin)  # Add Goblin to room1

# Define the actions
@when("look")
def look():
    print(player.current_room)

@when("move north")
def move_north():
    player.move("north")

@when("move south")
def move_south():
    player.move("south")

@when("take ITEM")
def take(item):
    player.take(item)

@when("inventory")
def show_inventory():
    player.show_inventory()

@when("use ITEM")
def use(item):
    player.use(item)

@when("talk to ITEM")
def talk(item):
    """Interact with an NPC in the current room."""
    if isinstance(item, NPC):  # Check if the item is an NPC
        item.interact()
    else:
        print(f"There is no {item.name} here to talk to.")

# Start the game
print("Welcome to the adventure game!")

# Game loop
while True:
    command = input("> ").lower().strip()
    if command == "quit":
        print("Goodbye!")
        break
    else:
        # Trigger the matching action using the `when` decorator
        try:
            when(command)()  # Automatically trigger the correct function for the command
        except Exception as e:
            print(f"Invalid command: '{command}'. Error: {e}")
