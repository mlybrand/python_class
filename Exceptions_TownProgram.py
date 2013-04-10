'''
Created on Apr 10, 2013

@author: Chad
'''
import ExceptionMadness as eM
from ExceptionMadness import MyException

cTown = eM.ChadTown("Olympia")
#cTown.AddWitches(1)
#cTown.AddSillMonsters(4)

try:
    cTown.WitchAction()
    #cTown.SillyMonsterAction()
except MyException as m:
    print(m)
except Exception:
    print("Oops!")


