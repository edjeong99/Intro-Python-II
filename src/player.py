# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def getItem(self, item):
        result = list(filter(lambda x: x == item, self.room.items))
        if len(result) > 0:
            self.items.append(item)
