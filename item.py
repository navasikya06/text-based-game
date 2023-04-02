import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, healpower = None, killpower = None, size = None, cost = None):
        self.name = name
        self.desc = desc
        self.size = size
        self.loc = None
        self.healpower = healpower
        self.killpower = killpower
        self.cost = cost
        self.key = None
        self.contain = []

    def describe(self):
        clear()
        print(self.desc)
        if self.size != None:
            print("Size: " + str(self.size))
        if self.healpower != None:
            print("Heal power: " + str(self.healpower))
        if self.killpower != None:
            print("Kill power: " + str(self.killpower))
        if self.cost != None:
            print("Cost: " + str(self.cost))
        print()
        input("Press enter to continue...")

    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

    def putInRoomhidden(self,room):
        self.loc = room
        room.addHiddenItem(self)

    def isHealer(self):
        if self.healpower == None:
            return False
        else:
            return True

    def isWeapon(self):
        if self.killpower == None:
            return False
        else:
            return True

    def iscost(self):
        if self.cost == None:
            return False
        else:
            return True

class Locked(Item):
    def __init__(self, name, desc, key, healpower = None, killpower = None, size = None, cost = None):
        Item.__init__(self, name, desc, healpower, killpower, size, cost)
        self.key = key
        self.inside = []
        self.contain = []

    def putinchest(self,item):
        self.inside.append(item)

    def reveal(self,key):
        clear()
        print("This " + str(self.name) + " contains: ")
        for i in self.inside:
                print(str(i.name))

class Container(Item):
    def __init__(self, name, desc, healpower = None, killpower = None, size = None, cost = None):
        Item.__init__(self, name, desc, healpower, killpower, size, cost)
        self.key = None
        self.contain = []

    def putincontain(self,item):
        self.contain.append(item)

    def print(self):
        clear()
        print("This " + str(self.name) + " contains: ")
        for i in self.contain:
                print(str(i.name))



