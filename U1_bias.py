if __name__ == '__main__':
	import sys, os 
	
	samfile = sys.argv[1] 
	
	
	#check that file names are OK
	if not os.path.isfile(samfile):
		print "sam file is not found"
		sys.exit()
		
	names= open(samfile)
	counts=0
	rows=0
	for line in names:
		rows=rows+1
		line_list= line.split()
		read_name=line_list[9]
		if read_name[0]=="T":
			counts=counts+1
	print(counts)
	print(rows)
	