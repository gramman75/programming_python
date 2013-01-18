'''
Created on 2013. 1. 18.

@author: stmkmk
'''
import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines: print(line, end='')