import glob, os, re, time

class Check(object):
	"""Logic"""
	def __init__(self, src, destination, belowdir, convert, directBtn, fileBtn, searchword,
	 searchkor, prefix, suffix, include):
		self.src = src
		self.destination = destination
		self.belowdir = belowdir
		self.convert = convert
		self.directBtn = directBtn
		self.fileBtn = fileBtn 
		self.searchword = searchword
		self.searchkor = searchkor
		self.prefix = prefix
		self.suffix = suffix
		self.include = include

		self.wfname = open(os.path.join(self.destination,'summary.txt'),'w')


	def makeSearchword(self):
		self.checkWord =[]
		if self.directBtn.isChecked():
			self.checkWord = self.searchword.split(';')
		else
			for line in open(self.searchword):
				self.checkWord.append(line[:-1])
	
	def checkKor(program, lineNum, origin, line):

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
	            # try:
	            #     translator = Translator('GSI_CHECK', 'm1ZX2yz3UVbmx7s2TVoaonjIsSqLvNjUtSd0VL1peBw=')
	            #     translate = translator.translate(origin, "en")
	            # except:
	            #     translate =''
	            
	            # try:
	            #     fname_kor.write(program + SEP + str(lineNum) + SEP + origin[:-1] + SEP + translate)
	            # except:
	            #     fname_kor.write(program + SEP + str(lineNum) + SEP + origin)
	            self.wfname.write(str(lineNum) + SEP + 'KOR' + SEP + origin)
	            #break
	            return True
	                      
	        if i >= (len(line)-1):
	            break   
	    return False

   def check(program, lineNum, origin, line):
    	flag = False
    
	    if  len(line) ==0:
	        return False
	     
	    if line.strip().find('--') == 0:
	        return False
	        
	    
	    if check_kor(program, lineNum, origin, line):
	        self.wfname.write(program+SEP+'KOR'+SEP+str(lineNum)+SEP+origin)
	        flag = True
	    
	    
	    #lookup check
	    # if (line.upper().strip().find('LOOKUP_TYPE') <> -1) or line.upper().strip().find('FLEX_VALUE_SET_NAME') <> -1:
	    #     for lookup in check_lookup:
	    #         if line.strip().find(lookup) <> -1:
	    #             w.write(str(lineNum) + SEP + lookup + SEP + origin)
	    #             fname_summary.write(program+SEP+lookup+SEP+str(lineNum)+SEP+origin)
	    #             flag=True
	                
	    #Hardcoding Check
	    for hardcoding in self.checkWord:       
	        p = re.compile(r'\b'+ hardcoding +r'\b')
	        #print re.search(p,line)
	        if re.search(p,line):
	            wfname.write(str(lineNum) + SEP + hardcoding + SEP + origin)
	            flag =  True
	                    
	    return flag 
	def run(object):
		AAAAAAA