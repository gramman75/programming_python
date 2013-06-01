'''
Created on 2013. 1. 21.

@author: stmkmk
'''
import sys

def filter_file(name,function):
    with open(name, 'r') as input, open(name+'.out','w') as output:
        for line in input:
            output.write(function(line))
            
def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')
    
if __name__=='__main__':
    filter_stream(lambda line:line)    
    
            