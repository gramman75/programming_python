'''
Created on 2013. 1. 18.

@author: stmkmk
'''
def interact():
    while True:
        try:
            reply = input('Enter Number :')
        except EOFError:
            break
        else:
            num = int(reply)
            print('%d squared is %d' %(num, num**2))
        
        num = int(reply)
    print('Bye!')
    
    
if __name__=='__main__':
    interact()    
    
    