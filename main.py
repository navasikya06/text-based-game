from room import Room
from player import Player
from item import Item
from item import Locked
from item import Container
from monster import Monster
from monster import Guard
from event import Event
from character import Character
import random
import os
import updater

player = Player()

def createWorld():
    a = Room("You are inside your hostel room.", None, None, None, "Use the key to open the drawer. And pay attention to the sticky note if you get stuck with a little word puzzle.")
    a1 = Room("You are outside of the hostel. The city is to the east.")
    a2 = Room("You are at the entrance of the city. You cannot get through without giving the right response. The prompt is: \"Nine to seven\".", None, None, None, "Look at the help menu to find a helpful command. And take what fits with the prompt from the message you found in your room.")
    b = Room("You are in front of a chemical factory. It is open and it seems that they make graphene here.")
    bb = Room("You are inside of the chemical factory. There are some scientists and engineers arguing in one corner.")
    b1 = Room("You are in front of a weapon store.")
    b11 = Room("You are inside the weapon store. There are a lot of useful tools around, and many of them deadly.")
    b2 = Room("You are in front of a jewelry workshop.")
    b22 = Room("You are inside the jewelry workshop. There is a small counter where they showcase all the finished works.")
    b3 = Room("You are in front of a bar. There is a flyer on the door saying that they are hiring musicians to play on the night show.")
    b33 = Room("You are inside the bar. It looks like they have a decent selection of liquor.", None, None, None, "If you lost something valuable during a fight with a destroyer, next time you should drop that item before fighting it.")
    b4 = Room("You are in front of a grocery store.")
    b44 = Room("You are inside the grocery store. Exciting!")
    c = Room("You are in city. There are few people around. Trees line along the street, but there is one particularly big oak tree to to the north.", "seven to five")
    c1 = Room("You are on the streets.")
    c2 = Room("You are at the oak tree. It looks like you can climb it.")
    c3 = Room("You are on the oak tree. There is a bird nest on the tree, inside it you see a few curious objects.")
    d = Room("You are in front of an abandoned pharmacy at the end of an alley. The place looks unoccupied and the door is askew.")
    d1 = Room("You are inside the pharmacy. There is a big periodic table on one side of the room, with the Hydrogen placed above Carbon instead of Lithium.", None, None, None, "Try inspecting something and try unlocking it with something you found from the tree.")
    e = Room("You are in front of the Samarium office building. There are many security guards in front of it.", None, None, None, "Look the the help menu to find a helpful command. Also, if you have lost something essential during a fight with some destroyer, next time you should drop the item before attacking the monster.")
    e1 = Room("You are in front of the second floor.", None, "Climbing gears", 30)
    e2 = Room("You are in front of the third floor.", None, "Climbing gears", None, "Use a strong weapon you have to break in.")
    e3 = Room("You are in front of the fourth floor.", None, "Climbing gears")
    e4 = Room("You are in front of the fifth floor.", None, "Climbing gears")
    e5 = Room("You are inside James Mortimer's office. Finally, this is when you can complete your mission.", "Pro laser cutter", None, None, "You should have talked to a character to know which USB to pick because you will not be able to carry them all. They are very heavy because they are full of secrets. Also, you will not open the USB with any key, but having it on you can help you opening it with a password!")

    Room.connectRooms(a, "east", a1, "west")
    Room.connectRooms(a1, "east", a2, "west")
    Room.connectRooms(a2, "north", c, "south")
    Room.connectRooms(c, "north", c2, "south")
    Room.connectRooms(c, "east", b, "west")
    Room.connectRooms(b, "north", bb, "south")
    Room.connectRooms(c, "west", c1, "east")

    Room.connectRooms(c2, "up", c3, "down")
    Room.connectRooms(c1, "west", b1, "east")
    Room.connectRooms(b1, "northeast", b11, "southwest")
    Room.connectRooms(b1, "north", b2, "south")
    Room.connectRooms(b2, "west", b22, "east")
    Room.connectRooms(b1, "west", b3, "east")
    Room.connectRooms(b3, "southeast", b33, "northwest")
    Room.connectRooms(b3, "west", e, "east")
    Room.connectRooms(b3, "north", b4, "south")
    Room.connectRooms(b4, "west", b44, "east")

    Room.connectRooms(e, "up", e1, "down")
    Room.connectRooms(e1, "up", e2, "down")
    Room.connectRooms(e2, "up", e3, "down")
    Room.connectRooms(e3, "up", e4, "down")

    Room.connectRooms(e2, "in", e5, "out")

    Room.connectRooms(b2, "north", d, "south")
    Room.connectRooms(d, "east", d1, "west")

    h = Item("Pro laser cutter", "This is a laser cutter, it can easily blind your opponent, and can also cut through most window glass easily.", None, 4, 4, 20)
    h.putInRoom(b11)
    hh = Item("Sulfuric acid spray", "This is a solutiont of concentrated sulfuric acid, it can severely burn your opponent.", None, 3, 3, 10)
    hh.putInRoom(b11)
    hhh = Item("Laser reflect glasses", "This is a filter glass that prevents you from being blinded by laser, either yours or your opponent's, and also reflect it towards any direction you desire.", None, 5, 3, 15)
    hhh.putInRoom(b11)
    hhhh = Item("Biochemistry text book", "This is a textbook, it is very heavy. It can be used to hurt people.", None, 5, 2, 5)
    hhhh.putInRoom(b11)
    i = Container("Backpack", "This is a backpack. There is a sandwich, a bottle of water and a key.", None, None, 10, None)
    i.putInRoom(a)
    ii = Container("Desk", "This is a desk. There is a notebook with a sticky note on it, and a drawer on the side.", None, None, None, None)
    ii.putInRoom(a)
    iii = Item("Sticky note", "This is a sticky note. It reads: Every fourth!!!", None, None, 0.5, None)
    iii.putInRoomhidden(a)
    ii.putincontain(iii)
    iiii = Item("Key", "This is an old rusty key.", None, None, 1, None)
    iiii.putInRoomhidden(a)
    i.putincontain(iiii)
    iiiii = Locked("Drawer", "This is a drawer. It is locked.", iiii, None, None, None, None)
    iiiii.putInRoomhidden(a)
    ii.putincontain(iiiii)
    iiiiii = Item("Message", "This is a message. It reads: Seven hen in to dances from five without rest, and your handsome pharmacy is much third hen squire floor.", None, None, 0.5, None)
    iiiiii.putInRoomhidden(a)
    iiiii.putinchest(iiiiii)
    iiiiiii = Item("Sandwich", "This is a sandwich. It is French style and has some pate in it.", 3, None, 2, None)
    iiiiiii.putInRoomhidden(a)
    i.putincontain(iiiiiii)
    iiiiiiii = Item("Bottle of water", "This is a bottle of water, drinking it gives you 3 health points.", 3, None, 2, None)
    iiiiiiii.putInRoomhidden(a)
    i.putincontain(iiiiiiii)
    j = Item("Gun", "This is a gun. It is also magical because there will be as many bullets as the player wants.", None, 5, 4, None)
    j.putInRoom(c3)
    jj = Item("Wooden letter", "This is a wooden letter H. It is a bit bigger than a normal toy letter.", None, None, 3, None)
    jj.putInRoom(c3)
    k = Item("Medicine", "This is a health potion. It will help you gain 5 in health.", 5, None, 2, None)
    k.putInRoom(d1)
    kk = Item("Photo", "This is an old black and white photo. It is of a man standing in front of an office building named \"Samarium\". He looks a lot like Abraham Lincoln. On the back of the photo reads \"August 1941.\"", None, None, 0.5, None)
    kk.putInRoomhidden(d1)
    kkk = Item("Climbing gears", "These are climbing gears. The rope is about twenty meters.", None, None, 20, None)
    kkk.putInRoomhidden(d1)
    kkkk = Locked("Periodic table", "Each letter is a hollow cut out, and there are many wooden letters in a box nearby. It is also easy to recognize that Hydrogen is placed above Carbon instead of Lithium. How strange!", jj, None, None, None, None)
    kkkk.putInRoomhidden(d1)
    kkkk.putinchest(kk)
    kkkk.putinchest(kkk)
    l = Locked("USB 1", "This is a USB. On it is carved: \"The mind palace\"", "August 1940", None, 10, None)
    l.putInRoom(e5)
    ll = Locked("USB 2", "This is a USB. On it is carved: \"The pink lady\"", "August 1941", None, 10, None)
    ll.putInRoom(e5)
    lll = Locked("USB 3", "This is a USB. On it is carved: \"The speckled band\"", "August 1942", None, 10, None)
    lll.putInRoom(e5)
    llll = Locked("USB 4", "This is a USB. On it is carved: \"The empty house\"", "August 1943", None, 10, None)
    llll.putInRoom(e5)
    lllll = Locked("USB 5", "This is a USB. On it is carved: \"The good-humored professor\"", "August 1944", None, 10, None)
    lllll.putInRoom(e5)
    l1 = Item("Message", "You have found the wrong USB.")
    l2 = Item("Message", "Congratulations! You found the right USB. All secrets immediately get erased and your mission is successful.")
    l3 = Item("Message", "You have found the wrong USB.")
    l4 = Item("Message", "You have found the wrong USB.")
    l5 = Item("Message", "You have found the wrong USB.")
    l1.putInRoomhidden(e5)
    l2.putInRoomhidden(e5)
    l3.putInRoomhidden(e5)
    l4.putInRoomhidden(e5)
    l5.putInRoomhidden(e5)
    l.putinchest(l1)
    ll.putinchest(l2)
    lll.putinchest(l3)
    llll.putinchest(l4)
    lllll.putinchest(l5)
    m = Item("Love letter", "This is a love letter.", None, None, 0.5, None)
    mm = Item("Bota bag", "This is a bota bag half full with alcohol.", None, -3, 2, None)
    mmm = Item("Knife", "This is a small double edged dagger. On it is carved \"The Sword of Gryffindor\"", None, 3, 2, None)
    mmmm = Item("iPhone", "This is a functioning iPhone. However it is password locked and of no use.", None, None, 2, None)
    mmmmm = Item("Revolver", "This is a handy revolver.", None, 6, 2, None)
    player.location = a
    n = Monster("Drunkard (destroyer)", 10, e, 1, 0)
    n.addItem(m)
    n.addItem(mm)
    nn = Monster("Thief", 10, b2, 0, 0)
    nn.addItem(mmm)
    nn.addItem(mmmm)
    o = Guard("Security", 20, e, 0, 2)
    o.addItem(mmmmm)

    p = Event("The LED screen across the street changed from a normal ad to a video of a man speaking. He looks like Abraham Lincoln, and obviously an authority within the city. He introduced himself as James Mortimer.", 20)
    player.events.append(p)

    q = Character("Bartender", b33, kk, [["Hi","Hullo"], ["Do you know how I can know more about him?", "You should go to the building in that photo. You will get more answers there."],["Do you know who the man in this photo is?", "That is James Mortimer, also known as the keeper of secrets. This city is filled with people whose reputation and very likely, whose own life is at his peril. He has a way of finding out about people's secrets and uses them to control their lives."], ["Do you know any weapon store around here?", "Wow hey stranger, I don't think I have any business to do with weapons. You should find that out yourself."], ["Would you guys take a singer and pianist for a night show musician? I can play", "Oh sure. You should come back to audition for our boss in the evening."]])
    q1 = Character("Old lady", b4, None, [["Excuse me", "I know what you are looking for. All I can tell you is to remember the pink lady."], ["Wait can you tell me more about this city?", "Sorry I cannot say anymore."], ["What is your name?", "It does not matter. Just remember the pink lady."]])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following enemies:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasCharacters():
        print("This room contains the following characters:")
        for k in player.location.characters:
            print(k.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("exit -- exit the game")
    print()
    print("status -- shows your status")
    print("wait <number of minutes> -- waits a number of minutes")
    print("hint -- gives you a hint for the puzzle if you are stuck")
    print()
    print("go <direction> -- moves you in the given direction")
    print("enter <direction> -- prompts to enter a locked area")
    print("climb <direction> -- climbs in a given direction")
    print()
    print("inspect <item> -- looks at the item, including ones hidden inside other objects")
    print("open <item> -- opens a locked object")
    print("pickup <item> -- picks up the item (you need to pick up hidden items separately from their container)")
    print("drop <item> -- drops the item")
    print("buy <item> -- buys the item")
    print("healwith <item> -- uses your health potion")
    print("inventory -- opens your inventory")
    print()
    print("equip <item> -- equips a weapon")
    print("attack <character> -- attacks a character")
    print("ask <character> -- starts a conversation with a character")
    print()
    input("Press enter to continue...")

#game start

a = input("What is your name? ")
print()
input(str(a)+", welcome to this text-based adventure game. You are a spy with a mission, but because you have lost part of your memory, you will act more like a detective trying to find clues and solve puzzles hidden in your surroundings to figure out what your original mission was and to carry it out successfully. The city is only large enough to accommodate a reasonable amount of distraction, but have fun exploring and stay alert. Bon voyage!")
print()
input("A hint to start off: typing help will bring up the menu of commands you can do.")

createWorld()

playing = True

while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        for j in player.events: #display event at the right time
            if player.clock >= j.time:
                print()
                print("An event just happened:")
                print(j.description)
                player.events.remove(j)
                input("Press enter to continue...")
        if commandWords == []: #error for no command
            print("Not a valid command")
            commandSuccess = False
        elif commandWords[0].lower() == "hint":
            if player.location.hint == None:
                print("There is no hint in this room.")
                commandSuccess = False
            else:
                print(player.location.hint)
                input("Press enter to continue...")
        elif commandWords[0].lower() == "go": #go unless the room has special features
            if len(commandWords) == 2:
                target = commandWords[1].lower()
                if target not in player.location.exitNames():
                    print("You cannot go in that direction.")
                    commandSuccess = False
                else:
                    destination = player.location.getDestination(target)
                    if destination.islocked() == True:
                        print("You cannot go in that direction because it is locked.")
                        commandSuccess = False
                    elif destination.isclimb() == True:
                        print("You cannot use go command in that direction because you need climbing tools.")
                        commandSuccess = False
                    elif destination.istimer(player) == True:
                        print("You cannot go in that direction because it is not the right time yet. Your internal clock has to be at " + str(player.location.timer) + " mins.")
                        commandSuccess = False
                    elif target in player.location.exitNames():
                        player.goDirection(target) 
                    else:
                        print("Not a valid command")
                        commandSuccess = False
                    timePasses = True
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "climb": #same as go but has to have tools
            if len(commandWords) == 2:
                target = commandWords[1].lower()
                if target not in player.location.exitNames():
                    print("You cannot go in that direction.")
                    commandSuccess = False
                else:
                    destination = player.location.getDestination(target)
                    if destination.istimer(player) == True:
                        print("You cannot go in that direction because it is not the right time yet. Your internal clock has to be more than " + str(player.location.timer) + " mins.")
                        commandSuccess = False
                    elif destination.isclimb() == True and destination.istimer(player) == False:
                        code = input("What do you want to climb with? ")
                        gear = player.getItemByName(code)
                        if code.lower() == destination.climb.lower() and gear != False:
                            player.goDirection(target)
                        elif code != destination.climb.lower():
                            print("You do not have the right equipment.")
                            commandSuccess = False
                        elif gear == False:
                            print("You do not have this equipment.")
                            commandSuccess = False
                    elif destination.isclimb() == False:
                        print("The destination is not climbable. Try \"go\".")
                        commandSuccess = False
                    else:
                        print("Not a valid command")
                        commandSuccess = False
                    timePasses = True
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "enter": #same as go but with code
            if len(commandWords) == 2:
                target = commandWords[1].lower()
                if target not in player.location.exitNames():
                    print("Not a valid command")
                    commandSuccess = False
                else:
                    destination = player.location.getDestination(target)
                    if destination.islocked() == True:
                        code = input("What is the code, or what do you want to use to enter? ")
                        if code.lower() == destination.key.lower():
                            destination.key = None
                        else:
                            print("You have the wrong code. Try again.")
                            commandSuccess = False
                    elif destination.islocked() == False:
                        print("This place is not locked.")
                        commandSuccess = False
                    else:
                        print("Not a valid command")
                        commandSuccess = False
                    timePasses = True
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "wait":
            targetTime = command[5:]
            try:
                i = 0
                while i <= int(targetTime):    
                    updater.updateAll()
                    i += 1
            except:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "pickup": #pickup when there is no hinder is cost or unmoveable object
            targetName = command[7:].lower()
            target = player.location.getItemByName(targetName)
            target2 = player.getItemByName(targetName)
            if target == False and target2 in player.items:
                print("You already have this item.")
                commandSuccess = False
            elif target == False:
                print("No such item.")
                commandSuccess = False
            elif target.size == None:
                print("You cannot pick up this item.")
                commandSuccess = False
            elif target.iscost() == True:
                print("You have to buy this item.")
                commandSuccess = False
            elif target != False and target.iscost() == False:
                player.pickup(target)
        elif commandWords[0].lower() == "buy": #buy item
            targetName = command[4:].lower()
            target = player.location.getItemByName(targetName)
            if target == False:
                print("No such item.")
                commandSuccess = False
            elif target != False and target.iscost() == True:
                player.buy(target)
            elif target.iscost() == False:
                print("This item does not cost.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "open": #open locked chest, with functions within the chest as it gets opened
            targetName = command[5:].lower()
            target = player.location.getItemByName(targetName)
            target2 = player.getItemByName(targetName)
            if target == False:
                print("No such item.")
                commandSuccess = False
            elif target.key == None:
                print("This item cannot be opened.")
                commandSuccess = False
            elif target2 != False: #if the item is on the player, it is the password kind of locked chest
                key = input("What is the password? ")
                if key.lower() == target2.key.lower():
                    target2.reveal(key)
                    opencommand = input("What now? ")
                    opencommandWords = opencommand.split()
                    if opencommandWords == []:
                        input("Press enter to continue...")
                        commandSuccess = False
                    elif opencommandWords[0].lower() == "inspect":
                        targetName = opencommand[8:].lower()
                        target = player.location.getItemByName(targetName)
                        target2 = player.getItemByName(targetName)
                        if target != False:
                            player.inspect(target)
                        elif target2 != False:
                            player.inspect(target2)
                        elif target == False and target2 == False:
                            print("No such item.")
                            commandSuccess = False
                        else:
                            print("Not a valid command")
                            commandSuccess = False
                    else:
                        print("You can only inspect here.")
                        commandSuccess = False
                else:
                    print("That is not the right code.")
                    print()
                    input("Press enter to continue...")
                    commandSuccess = False
            elif target != False and target.key in player.items: #if the item is in the room and the player has the key, the item is the key kind of locked chest
                player.openchest(target,target.key)
                opencommand = input("What now? ")
                opencommandWords = opencommand.split()
                if opencommandWords == []:
                    input("Enter \"help\" to prompt to continue") #to get out of the inside function
                    commandSuccess = False
                elif opencommandWords[0].lower() == "inspect": #you can either inspect or pick up inside
                    targetName = opencommand[8:].lower()
                    target = player.location.getItemByName(targetName)
                    target2 = player.getItemByName(targetName)
                    if target != False:
                        player.inspect(target)
                    elif target2 != False:
                        player.inspect(target2)
                    elif target == False and target2 == False:
                        print("No such item.")
                        commandSuccess = False
                    else:
                        print("Not a valid command")
                        commandSuccess = False
                elif opencommandWords[0].lower() == "pickup":
                    targetName = opencommand[7:].lower()
                    target = player.location.getItemByName(targetName)
                    if target in player.items:
                        print("You already have this item.")
                        commandSuccess = False
                    elif target == False:
                        print("No such item.")
                        commandSuccess = False
                    elif target.size == None:
                        print("You cannot pick up this item.")
                        commandSuccess = False
                    elif target != False and target.iscost() == False:
                        player.pickup(target)
                    elif target.iscost() == True:
                        print("You have to buy this item before picking it up.")
                        commandSuccess = False
                    else:
                        print("Not a valid command")
                        commandSuccess = False
                else:
                    print("You can only inspect or pick up within a container. Press enter to continue.")
                    commandSuccess = False
            elif target.key not in player.items:
                print("You do not have the key to open this item.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":
            targetName = command[5:].lower()
            target = player.getItemByName(targetName)
            if target != False:
                player.drop(target)
            elif target == False:
                print("No such item.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:].lower()
            target = player.location.getItemByName(targetName)
            target2 = player.getItemByName(targetName)
            if target != False:
                player.inspect(target)
            elif target2 != False:
                player.inspect(target2)
            elif target == False and target2 == False:
                print("No such item.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "healwith":
            targetName = command[9:].lower()
            target = player.getItemByName(targetName)
            if target == False:
                print("No such item in your inventory.")
                commandSuccess = False
            elif target != False and target.isHealer() != False:
                player.heal(target)
            elif target.isHealer() == False:
                print("You cannot heal with this item.")
                commandSuccess = False         
            else:
                print("Not a valid command")
                commandSuccess = False       
        elif commandWords[0].lower() == "status":
            player.status()
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "attack": #attack with or without weapon, and monster's random object appearing
            targetName = command[7:].lower()
            target = player.location.getMonsterByName(targetName)
            if target != False and player.fightpouch == []:
                player.attackMonster(target)
                x = random.choice(target.items)
                player.location.addItem(x)
                printSituation()
            elif target != False and player.fightpouch != []:
                player.attackMonster(target,player.fightpouch)
                x = random.choice(target.items)
                player.location.addItem(x)
                printSituation()
            elif target == False:
                print("No such monster.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "ask": #talk to character with the right access, unless the character has no access key
            targetName = command[4:].lower()
            target = player.location.getCharacterByName(targetName)
            if target == False:
                print("No such character.")
                commandSuccess = False
            elif target != False and target.access in player.items:
                player.ask(target)
            elif target != False and target.access == None:
                player.ask(target)
            elif target != False and target.access not in player.items:
                print("You do not have anything to ask this character yet.")
                commandSuccess = False  
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "equip": #equipping weapons
            targetName = command[6:].lower()
            target = player.getItemByName(targetName)
            if target == False:
                print("No such item.")
                commandSuccess = False 
            elif target != False and target.isWeapon() != False:
                player.equip(target)
            elif target.isWeapon() == False:
                print("You cannot equip this item to fight.")
                commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    


