'''
Created on Apr 9, 2013

@author: Chad
'''

import re

crazyString = "This is a really funny story about the # 54. It is fun... because I say it is!"

prog = re.compile("\d{1,3}")
result = prog.match("132")


result2 = re.match("\d", "1")


print(re.findall("\d+\D$","1236xty"))
print("Oops! That '$' sign didn't match up with my results")
print(re.findall("\d+\D","1236xty"))
print("Aaaaah. That's better")


if re.match("...$", crazyString):
    print("There was a match!")
else:
    print("No match... bummer.")
    
mySearchMatches = re.search("\d{3}", crazyString, re.M | re.I)
if mySearchMatches:
    print(mySearchMatches.group())
else:
    print("No match... again! Sheesh!")

print("A 'look-ahead' example of a regular expression:")
print(re.findall("fun", crazyString))
print(re.findall("(?<=y )fun", crazyString))
