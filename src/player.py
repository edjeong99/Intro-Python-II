# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

    def get_item(self, item):
        print(f'in Player get_item item = {item}')
        print(f'in Player get_item current_room = {self.current_room.name}')
        print(
            f'in Player get_itemself.current_room.items = {self.current_room.items[0].name}')

        self.items.append(item)
        self.current_room.items.remove(item)
