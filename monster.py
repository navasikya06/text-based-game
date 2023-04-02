import random
import updater

class Monster:
    def __init__(self, name, health, room, destroy = 0, lives = 0):
        self.name = name
        self.health = health
        self.room = room
        self.lives = lives #new attributes
        self.destroy = destroy
        self.items = []
        room.addMonster(self)
        updater.register(self)

    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
        
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)

    def isrevive(self):
        if self.lives == 0:
            return False
        else:
            return True

    def isdestroy(self):
        if self.destroy == 0:
            return False
        else:
            return True

    def addItem(self,item):
        self.items.append(item)

class Guard(Monster): #monster that does not get registered into update
    def __init__(self, name, health, room, destroy = 0, lives = 0):
        self.name = name
        self.health = health
        self.room = room
        self.lives = lives
        self.destroy = destroy
        self.items = []
        room.addMonster(self)

    def reducelife(self): #monster that has multiple lives
        self.lives -= 1

    def die(self):
        self.room.removeMonster(self)



