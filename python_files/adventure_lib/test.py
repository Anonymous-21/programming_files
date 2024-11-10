from adventurelib import *

room1 = Room("Room 1")
room2 = Room("Room 2")

room1.east = room2
room2.west = room1

current_room = room1

@when("look")
def look():
    print(current_room.description)

@when("go east")
@when("east")
@when("e")
def go_north():
    global current_room
    current_room = current_room.east
    
@when("go west")
@when("west")
@when("w")
def go_west():
    global current_room
    current_room = current_room.west

start()
