# -*- encoding: utf-8-*-
import glob, os, re

def check(line):
    
    if  len(line.strip()) ==0:
        return False
    
    if line.strip().find('--') == 0:
        return False
        
    i = 0
    while 1:
        try:
            a1 = line[i] 
            i = i+1
        
            a2 = line[i]
        except IndexError:
            a1 = ' '
            a2 = ' '
            #print line
            
            
        c1 = hex(ord(a1))
        c2 = hex(ord(a2))
        #print c1
        #print c2
                
            
       
        if (c1 >= '0xb0') and (c1 <= '0xc8') and (c2 >='0xa1') and (c2 <= '0xfe'):
            #w.write(str(lineNum) + ' : '+ origin)  
            #break
            return True
                      
        if i >= (len(line)-1):
            break   
    return False
'''
formList = glob.glob('c:\\formlist\\*.fmb')

for formName in formList:
    command = 'frmcmp.exe batch=yes module_type=form userid=devs/devs@erpprod forms_doc=YES WINDOW_STATE=MINIMIZE module='+formName
    os.system(command)
'''
textList = glob.glob('d:\\check\\*.txt')
#textList = glob.glob('d:\\check\\EWIPF031.txt')

for textName in textList:
    print textName
    i = 0
    lineNum = 0
    f = open(textName,'r')
    w = open(textName+'_result.txt','w')
    lines = f.readlines()
    isComment = False
        
        
    
    
    for line_a in lines:
        
        #print line_a
        line    = line_a
        lineNum = lineNum + 1
        origin  = line        
        comment = line.strip().find('--')
        start   = line.strip().find('/*')
        end     = line.strip().find('*/')

       
                
        #line = line[:pos]
        i = 0 
        #comment1 = line.strip().find('--')
        #comment2 = line.strip().find('/*')
        #comment3 = line.strip().find('**')
        
        #print lineNum
        #print isComment
        #print start
        #print end
        
        if line.find('* Comments') <> -1:    # * Comments 
            continue
        elif line.find('^ Comments') <> -1:    # ^ Comments 
            continue
        elif line.find('Font Name') <> -1:    # o Prompt Font Name
            continue
        elif line.find('- Comments') <> -1:    # o Prompt Font Name
            continue        
        elif line.find('^ Parameter Initial Value') <> -1:
            continue
        elif len(line.strip()) == 0:         
            continue        
        elif isComment==False and comment == 0 and start == -1 and end == -1: 
            continue
        elif isComment==False and comment <> 0 and start == -1 and end == -1:
            
            if comment <> -1:
                line = line[:comment]            
            
            if check(line):                            
                w.write(str(lineNum) + ' : '+ origin)                  
                continue
        elif isComment == True  and start <> -1 and end <> -1:
            isComment = False
            continue
        elif isComment == False and start <> -1 and end <> -1:                  
            
            #pattern = re.compile('/\/\*[.\w\s\*]*\*\//')
            #result = re.match(pattern,line)
            
            if (start == 0 and end == (len(line.strip())-2)):                                
                continue
            else:                                
                before = line.strip()[:start].strip()                
                after  = line.strip()[end+2:].strip() 
                            
                
                if (check(before) or check(after)):
                    w.write(str(lineNum) + ' : '+ origin) 
                    continue
        elif isComment or (start <> -1 and end == -1) or (start == -1 and end <> -1):    #multi-Line
            if isComment == False and start <> - 1 and end == -1:                        # coding /* Multi-Line주석 시작
                
                line = line.strip()[:start]
                isComment = True
                
                if check(line):
                    w.write(str(lineNum) + ' : '+ origin) 
                    continue            
            elif isComment and start == -1 and end == -1:                               # Multi-Line   
                continue
            
            elif isComment and start == -1 and end <> - 1:                              # Multi-Line start   */ Coding
            #elif isComment and end <> - 1:                              # Multi-Line end  */ Coding
                line = line.strip()[end+2:]                
                isComment = False
            
                if check(line):
                    w.write(str(lineNum) + ' : '+ origin) 
                    continue
        else:
            
            if check(line):
                w.write(str(lineNum) + ' : '+ origin) 
                continue
                        
    w.close()
    f.close()
    

