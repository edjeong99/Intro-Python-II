from room import Room
from player import Player
from item import Item
from data import room, item

#
# Main
#


def p_move(p, direction):
    direction = direction + "_to"
    if hasattr(p.current_room, direction):
        p.current_room = getattr(p.current_room, direction)
    else:
        print("You can not move to that direction")


    # Make a new player object that is currently in the 'outside' room.
p = Player("tom", room['outside'])
# Write a loop that:

while True:
    print(f"\n\nYou are in the {p.current_room.name}\n")
    print(p.current_room.description)
    p.current_room.display_items()
    pinput = input("What do you want to do next? ")

    if pinput == 'n' or pinput == 's' or pinput == 'e' or pinput == 'w':
        p_move(p, pinput)

 # * Prints the current room name
 # * Prints the current description (the textwrap module might be useful here).
 # * Waits for user input and decides what to do.
 #
 # If the user enters a cardinal direction, attempt to move to the room there.
 # Print an error message if the movement isn't allowed.
 #
 # If the user enters "q", quit the game.
