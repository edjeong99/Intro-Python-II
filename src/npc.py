from player import Player


class Npc(Player):
    def __init__(self, name, description, room, items):
        super().__init__(name, room, items)
        self.description = description
