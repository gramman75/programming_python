import os,sys

file_loc = r'd:\temp\dq1.txt' #sys.argv[0]
desc_loc = r'c:\temp' #sys.argv[1]
temp_query_id = -1




for line in open(file_loc):
	cols = line.split('\t')
	print cols
	if temp_query_id == -1:
		new_file = open(os.path.join(desc_loc,cols[1]),'w')
		new_text = 'select {0} '.format(cols[2])+'\n'
		try:
			from_clause = cols[3]
		except IndexError:
			from_clause = ''

		try:	
			where_clause = cols[4]
		except IndexError:
			where_clause = ''

		try:
			order_by_cluase = cols[5]
		except IndexError:
			order_by_cluase = ''

		temp_query_id = cols[0]
	if cols[0] <> temp_query_id:
		new_text = new_text+' \n'+from_clause+' \n' +where_clause+' \n'+order_by_cluase
		temp_query_id = cols[0]
		new_file.write(new_text)
		new_file.close()
		print cols
		new_file = open(os.path.join(desc_loc,cols[1]),'w')
		new_text = 'select {0} '.format(cols[1])
		try:
			from_clause = cols[3]
		except IndexError:
			from_clause = ''

		try:	
			where_clause = cols[4]
		except IndexError:
			where_clause = ''

		try:
			order_by_cluase = cols[5]
		except IndexError:
			order_by_cluase = ''
	elif cols[0] == temp_query_id:
		new_text = new_text + ' , '+cols[2]+'\n'

new_file.close()
