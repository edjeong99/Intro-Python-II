from room import Room
from item import Item
from npc import Npc


# Items
item = {
    'sword': Item("sword", "it is a long sword"),
    'lamp': Item("lamp", "Lamp that illuminate"),
    'rock': Item("rock", "Rock.  You can throw it"),
    'bread': Item("bread", "You can eat this bread"),
}

# Items
npc = {
    'zombie': Npc("zombie", "it is a Zombie.  It will eat you", '', []),
    'helper': Npc("helper", "Helper will give you strength", '', [])
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['sword'], item['lamp']], True, []),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [item['rock']], True, [npc['zombie'], npc['helper']]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [], True, []),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", [], True, []),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! ", [item['bread']], True, []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
