import os
import updater
import character
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.fightpouch = []
        self.health = 50
        self.killerpower = 0 #new attributes
        self.currency = 100
        self.clock = 0
        self.alive = True
        self.events = []
        updater.register(self)

    def update(self):
        if random.random() < .5:
            self.health -= 0.1
            self.clock += 1

    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)

    def limit(self):
        total = 0
        for i in self.items:
            if i.size != None:
                total += i.size 
        if total > 40:
            return False
        else:
            return True

    def pickup(self, item): #limit on carry amount
        clear()
        if self.limit() == False:
            print("You are carrying more items than you can. Your carry limit is 50 kg.")
            print()
            input("Press enter to continue...")
        else:
            self.items.append(item)
            item.loc = self
            if item in self.location.items:
                self.location.removeItem(item)
            elif item in self.location.hiddenitems:
                self.location.removeHiddenItem(item)

    def buy(self,item):
        if self.currency > item.cost:
            self.pickup(item)
            if self.limit() != False:
                self.currency -= item.cost    

    def inspect(self,item):
        clear()
        print(item.desc)
        if item.size != None:
            print("Size: " + str(item.size))
        if item.healpower != None:
            print("Heal power: " + str(item.healpower))
        if item.killpower != None:
            print("Kill power: " + str(item.killpower))
        if item.cost != None:
            print("Cost: " + str(item.cost))
        print()
        if item.contain != []:
            item.print()
        print()
        input("Press enter to continue...")

    def heal(self,healer):
        clear()
        self.health += healer.healpower
        self.items.remove(healer)
        print("Your current health status is: " + str(int(self.health)) + ".")
        print()
        input("Press enter to continue...")

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    def drop(self,item):
        self.items.remove(item)
        item.putInRoom(self.location)

    def status(self):
        clear()
        print("Your current health status is: " + str(int(self.health)) + ".")
        print("Your current killer power is: " + str(self.killerpower) + ".")
        print("Your current currency level is: " + str(self.currency) + " dollars.")
        print("Your internal clock is: " + str(self.clock) + " mins.")
        print("Your current carrying weight is: " + str(self.weight()) + " kg.")
        print()
        input("Press enter to continue...")

    def addpoint(self,point):
        self.killerpower += point

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    def weight(self):
        total = 0
        for i in self.items:
            if i.size != None:
                total += i.size 
        return total

    def equip(self,weapon):
        clear()
        self.fightpouch.append(weapon)
        print("You are now equipped with " + str(weapon.name) + ".")
        print()
        input("Press enter to continue...")


    def attackMonster(self, mon, weapon = None):
        clear()
        print("You are attacking " + mon.name + ".")
        print()
        print("Your health is " + str(int(self.health)) + ".")
        print(mon.name + "'s health is " + str(int(mon.health)) + ".")
        print()
        self.killerpower += mon.health//5 #gets more kill power
        if weapon != None: #equip many weapons
            for i in weapon:
                mon.health -= i.killpower
                self.fightpouch.remove(i)
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(int(self.health)) + ".")
            print("You will be able to pick up something the " + str(mon.name) + " has left.")
            if mon.isrevive() == False and mon.isdestroy() == False: #normal monster
                mon.die()
            elif mon.isdestroy() == True: #monster that can destroy
                print("This monster can destroy " + str(mon.destroy) + " of your items before dying.")
                for i in range(1, mon.destroy):
                    a = random.choice(self.items)
                    self.items.remove(a)
                mon.die()
            elif mon.isrevive() == True: #monster that can revive
                print("This monster can revive for " + str(mon.lives) + " time(s)." )
                mon.reducelife()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

    def ask(self,character): #character with a conversation set
        clear()
        for i in range(len(character.responseset)-1):
            print("Choose one of the following conversation lines. Be careful, as you have limited number of asking chances:")
            for j in range(len(character.responseset)-1):
                print(str(j+1) + ":" + str(character.responseset[j][0]))
            a = input("Chosen number: ")
            a.strip()
            try: #catch error for values that are not correct
                print(str(character.responseset[int(a)-1][1]))
                print()
                input("Press enter to continue...")
            except:
                print("This is either not a number or the number is not the range.")
                print()
                input("Press enter to continue...")
        print()
        input("Your conversation is over. Press enter to continue...")

    def openchest(self,locked,key): #open a locked chest with the right given key
        clear()
        keygive = input("What do you want to open " + str(locked.name) + " with? ")
        if keygive == key.name.lower():
            locked.reveal(key)
            print()
        else:
            print("This key does not open this object.")
            print()
            input("Press enter to continue...")


