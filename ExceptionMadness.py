class MyException(Exception):
    pass

class MagicError(Exception):

    def __init__(self, message, additional):
        self.message = message
        self.additional = additional

    def __str__(self):
        return "{0}: {1}".format(self.message, self.additional)



class ChadTown:
    
##    _wackyWitches = 0
##    _magicBrooms = 0
##    _sillyMonsters = 0
    
    def __init__(self, name):
        self._wackyWitches = 0
        self._magicBrooms = 0
        self._sillyMonsters = 0
        pass
    
    def AddWitches(self, witchyIncrement):
        self._wackyWitches += witchyIncrement
        pass
    
    def AddMagicBrooms(self, broomIncrement):
        self._magicBrooms += broomIncrement
        pass 
    
    def AddSillMonsters(self, monsterIncrement):
        self._sillyMonsters += monsterIncrement
        pass 
    
    def WitchAction(self):
        i = 0
        if self._wackyWitches == 0 :
            raise MyException("You must have added some Wacky Witches!")
        while i < self._wackyWitches:
            print("Cackle and Howl")
            i+=1
        pass
    
    def MagicBroomAction(self):
        i = 0
        if self._magicBrooms == 0 :
            raise MagicError("You must have added some Magic Brooms!", 42)
        while i < self._magicBrooms:
            print("Swish swoosh swish")
            i+=1
        pass 
    
    def SillyMonsterAction(self):
        i = 0
        if self._sillyMonsters == 0 :
            raise Exception("You must have added some Silly Monsters!")
        
        while i < self._sillyMonsters:
            print("Wiggle and waggle")
            i+=1
        pass
    

