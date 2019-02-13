# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name,):
        self.name = name
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = []

    def addItemToRoom(self, item):
        self.items.append(item)

    def printItems():
        printf("{self.name} has following items : \n")
        for i in range(len(self.items)):
            printf(self.items[i])
