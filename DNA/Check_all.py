#-*- encoding:euc-kr -*-
#-*- encoding:euc-kr -*-
import glob, os, re, time
#from microsofttranslator import Translator


#translator = Translator('GSI_CHECK', 'm1ZX2yz3UVbmx7s2TVoaonjIsSqLvNjUtSd0VL1peBw=')


ROOT_DIR = r'D:\rollin-check'
SEP = '\t'

check_lookup = []
check_hardcoding =[]
exception_list =[]

# for line in  open(os.path.join(ROOT_DIR,'basis','audit_lookup.txt')):
    # check_lookup.append(line[:-1])

for line in  open(os.path.join(ROOT_DIR,'basis','audit_hardcoding.txt')):
    check_hardcoding.append(line[:-1])        

#for line in open(os.path.join(ROOT_DIR,'basis','exception_list.txt')):
#    exception_list.append(line[:-1])
#    print exception_list

fname_kor = open(os.path.join(ROOT_DIR,'kor_list.txt'),'w')
fname_kor.write('Program' + SEP + 'Line' + SEP + 'Source'+SEP+'Translate'+'\r')
fname_summary = open(os.path.join(ROOT_DIR,'summary.txt'),'w')
fname_summary.write('Pragram'+SEP+'Type'+SEP+'Line'+SEP+'Source'+'\r')
    
def check_kor(program, w, lineNum, origin, line):
    
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
            try:
                translator = Translator('GSI_CHECK', 'm1ZX2yz3UVbmx7s2TVoaonjIsSqLvNjUtSd0VL1peBw=')
                translate = translator.translate(origin, "en")
            except:
                translate =''
            
            try:
                fname_kor.write(program + SEP + str(lineNum) + SEP + origin[:-1] + SEP + translate)
            except:
                fname_kor.write(program + SEP + str(lineNum) + SEP + origin)
            w.write(str(lineNum) + SEP + 'KOR' + SEP + origin)
            #break
            return True
                      
        if i >= (len(line)-1):
            break   
    return False

def check(w, program, lineNum, origin, line):
    flag = False
    
    if  len(line) ==0:
        return False
     
    if line.strip().find('--') == 0:
        return False
        
    
    #if check_kor(program, w, lineNum, origin, line):
    #    fname_summary.write(program+SEP+'KOR'+SEP+str(lineNum)+SEP+origin)
    #    flag = True
    
    
    #lookup check
    if (line.upper().strip().find('LOOKUP_TYPE') <> -1) or line.upper().strip().find('FLEX_VALUE_SET_NAME') <> -1:
        for lookup in check_lookup:
            if line.strip().find(lookup) <> -1:
                w.write(str(lineNum) + SEP + lookup + SEP + origin)
                fname_summary.write(program+SEP+lookup+SEP+str(lineNum)+SEP+origin)
                flag=True
                
    #Hardcoding Check
    for hardcoding in check_hardcoding:       
        p = re.compile(r'\b'+ hardcoding +r'\b')
        #print re.search(p,line)
        if re.search(p,line):
            w.write(str(lineNum) + SEP + hardcoding + SEP + origin)
            fname_summary.write(program+SEP+hardcoding+SEP+str(lineNum)+SEP+origin)
            flag =  True
                    
    return flag

#formList = glob.glob('c:\\formlist\\*.fmb')

#for formName in formList:
#    command = 'frmcmp.exe batch=yes module_type=form userid=devs/devs@erpprod forms_doc=YES WINDOW_STATE=MINIMIZE module='+formName
#    os.system(command)

textList = glob.glob(os.path.join(ROOT_DIR,'04.Dynamic Query','*.*'))
target_dir = os.path.join(ROOT_DIR,'temp')
suffix = ''

startTime = time.time()

for textName in textList:
    file_name = textName.split(os.path.sep)[-1]
    print textName
    
    if file_name.split('.')[0] not in exception_list:
        i = 0
        lineNum = 0
        f = open(textName,'r')
        w = open(os.path.join(ROOT_DIR,target_dir,suffix+file_name+'.txt'),'w')
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
                
                if check(w, file_name, lineNum, origin, line):                            
                    #w.write(str(lineNum) + ' : '+ origin)                  
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
                                
                    
                    if (check(w, file_name,lineNum, origin, before) or check(w, file_name,lineNum, origin, after)):
                        #w.write(str(lineNum) + ' : '+ origin) 
                        continue
            elif isComment or (start <> -1 and end == -1) or (start == -1 and end <> -1):    #multi-Line
                if isComment == False and start <> - 1 and end == -1:                        # coding /* Multi-Line
                    
                    line = line.strip()[:start]
                    isComment = True
                    
                    if check(w, file_name,lineNum, origin, line):
                        #w.write(str(lineNum) + ' : '+ origin) 
                        continue            
                elif isComment and start == -1 and end == -1:                               # Multi-Line   
                    continue
                
                elif isComment and start == -1 and end <> - 1:                              # Multi-Line start   */ Coding
                #elif isComment and end <> - 1:                              # Multi-Line end  */ Coding
                    line = line.strip()[end+2:]                
                    isComment = False
                
                    if check(w, file_name,lineNum, origin, line):
                        #w.write(str(lineNum) + ' : '+ origin) 
                        continue
            else:
                
                if check(w, file_name,lineNum, origin, line):
                    #w.write(str(lineNum) + ' : '+ origin) 
                    continue
                            
        w.close()
        f.close()
        #fname_kor.close()
    
print time.time()-startTime
