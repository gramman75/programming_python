'''
Created on 2013. 1. 18.

@author: stmkmk
'''
import sys
numlines = 3
lines = sys.stdin.readlines()
print(lines)
while True:    
    while lines:
        flush = lines[:numlines]
        lines = lines[numlines:]
        for line in flush:
            print(line , end='')
        if lines and input('--More--') not in ('Y','y'):break