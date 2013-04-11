'''
Created on Apr 10, 2013

@author: Chad
'''
import ExceptionMadness as eM
from ExceptionMadness import MyException, MagicError

cTown = eM.ChadTown("Olympia")
cTown.AddWitches(1)
cTown.AddSillMonsters(4)

try:
    cTown.WitchAction()
    cTown.SillyMonsterAction()
    cTown.MagicBroomAction()
except MyException as m:
    print(m)
except MagicError as magic:
    print(magic)
except Exception as e:
    print(e)


