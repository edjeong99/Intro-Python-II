# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

    def get_item(self, item):
        self.items.append(item)
        self.current_room.items.remove(item)

    def drop_item(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)
