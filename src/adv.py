from room import Room
from player import Player
from item import Item

from data import room, item
from functions import p_move, one_word_input, two_word_input

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
p = Player("tom", room['outside'])
# Write a loop that:

while True:
    print(f"\n\nYou are in the {p.current_room.name}\n")
    print(p.current_room.description)
    p.current_room.display_items()
    pinput = input("What do you want to do next? ")

    input_list = pinput.split(' ', 1)
    print(input_list)

    if len(input_list) == 1:
        one_word_input(p, pinput)
    else:
        two_word_input(p, input_list)

        #  elif pinput:

        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
