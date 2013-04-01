# -*- encoding:utf-8-*-
import glob, os, re

def check(line):
    if  len(line) ==0:
        return False
     
    if line.strip().find('--') == 0:
        return False
    
    hard_code = ['glgc_get_time_gap_func']
    
    
    for a in hard_code:
        p = re.compile(r'\b'+a+r'\b')
        if re.search(p,line.upper()):
            return True        
    return False

#formList = glob.glob('c:\\formlist\\*.fmb')

#for formName in formList:
#    command = 'frmcmp.exe batch=yes module_type=form userid=devs/devs@erpprod forms_doc=YES WINDOW_STATE=MINIMIZE module='+formName
#    os.system(command)

textList = glob.glob('D:\\check_form_source\\*.*')
target_dir = 'd:\\result1\\'
suffix = ''

for textName in textList:
    file_name = textName[21:]
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
        
        if line.find('* Comments') <> -1:    # * Comments 
            continue
        elif line.find('^ Comments') <> -1:    # ^ Comments 
            continue
        elif line.find('Font Name') <> -1:    # o Prompt Font Name
            continue
        elif line.find('- Comments') <> -1:    # o Prompt Font Name
            continue
        elif line.find('Position') <> -1:    # o Prompt Font Name
            continue
        elif line.find('Width') <> -1:    # o Prompt Font Name
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
    

