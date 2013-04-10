'''
Created on Apr 9, 2013

@author: Chad
'''

import re

prog = re.compile("\d{1,3}")
result = prog.match("132")
result2 = re.match("\d", "1")

