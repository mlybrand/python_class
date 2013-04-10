class ChadTown:
    
    _wackyWitches = 0
    _magicBrooms = 0
    _sillyMonsters = 0
    
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
            raise Exception("You must have added some Magic Brooms!")
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
    

class MyException(Exception):
    pass

