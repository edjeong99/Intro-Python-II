# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

    def add_item(self, item):
        self.player_items.append(item)
        self.current_room.items.remove(item)
