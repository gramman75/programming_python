# -*- encoding:utf-8-*-
import glob, os, re

def check(line):
    if  len(line.strip()) ==0 or len(line.strip()) == 1:
        return False
    
    if line.strip().find('--') == 0:
        return False
    
    i = 0
    while 1:
        a1 = line[i] 
        i = i+1
        a2 = line[i]
        # 16진수로 변환     
        c1 = hex(ord(a1))
        c2 = hex(ord(a2))
        ''' 
        print 'a1 ' + a1
        print 'a2 ' + a2
        
        print 'c1 ' + c1
        print 'c2 ' + c2
        '''    
        #해당 문자가 한글 코드set에 포함되는지 확인
        if (c1 >= '0xb0') and (c1 <= '0xc8') and (c2 >='0xa1') and (c2 <= '0xfe'):
            #w.write(str(lineNum) + ' : '+ origin) # 포함이 되면 해당 Line위치와 원문을 출력 
            #break
            return True
                      
        if i == (len(line)-1):
            break   
    return False


textList = glob.glob('D:\\source_db_0328\\EBOM*.*')
target_dir = 'd:\\result\\'
suffix = ''

for textName in textList:
    
    file_name = textName.split(os.path.sep)[-1]
    print textName

    i = 0
    lineNum = 0
    f = open(textName,'r')
    w = open(target_dir+suffix+file_name+'.txt','w')
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
        
        if line.upper().find('COMMENT ON') <> -1:    # * comment on 
            continue                
        if line.upper().strip().find('IS') == 0:
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
    

