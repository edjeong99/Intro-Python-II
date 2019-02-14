# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items, lighted, npcs):
        self.name = name
        self.description = description
        self.items = items
        self.lighted = lighted
        self.npcs = npcs

    def display_items(self):
        print(f"{self.name} has {len(self.items)} items : ")

        for i in range(len(self.items)):
            print(f"  item #{i+1} : {self.items[i].name}")

    def display_npcs(self):
        print(f"{self.name} has {len(self.npcs)} NPCs : ")

        for i in range(len(self.npcs)):
            print(f"{self.npcs[i].name} :  {self.npcs[i].description}")

    def remove_item(self, item):
        self.items.remove(item)
