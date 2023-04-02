class Character:
    def __init__(self,name,room,access,responseset):
        self.name = name
        self.room = room
        self.access = access
        self.responseset = responseset
        room.addCharacter(self)


