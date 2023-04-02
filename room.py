import random
import player

class Room:
    def __init__(self, description, key = None, climb = None, timer = None, hint = None):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.hiddenitems = [] #new attributes
        self.characters = []
        self.key = key
        self.climb = climb
        self.timer = timer
        self.hint = hint

    def addCharacter(self,character):
        self.characters.append(character)

    def hasCharacters(self):
        return self.characters != []

    def getCharacterByName(self, name):
        for i in self.characters:
            if i.name.lower() == name.lower():
                return i
        return False

    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])

    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]

    def randomNeighbor(self):
        return random.choice(self.exits)[1]

    def exitNames(self):
        return [x[0] for x in self.exits] 

    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)

    def addItem(self, item):
        self.items.append(item)

    def addHiddenItem(self, item):
        self.hiddenitems.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def removeHiddenItem(self, item):
        self.hiddenitems.remove(item)

    def hasItems(self):
        return self.items != []

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        for k in self.hiddenitems:
            if k.name.lower() == name.lower():
                return k
        return False

    def addMonster(self, monster):
        self.monsters.append(monster)

    def removeMonster(self, monster):
        self.monsters.remove(monster)

    def hasMonsters(self):
        return self.monsters != []

    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False

    def islocked(self):
        if self.key == None:
            return False
        else:
            return True

    def isclimb(self):
        if self.climb == None:
            return False
        else:
            return True

    def istimer(self,player):
        if self.timer == None or player.clock >= self.timer:
            return False
        elif self.timer != None:
            return True


    