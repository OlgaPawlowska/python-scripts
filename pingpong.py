import sys, os
from collections import defaultdict
#defines a function
def make_dictionary (data):
	d ={}
	for row in data:
		te, pos, count = row.strip().split()
		d.setdefault(te, {})[int(pos)] = int(count)
	return d


file=sys.argv[1]
file_2=sys.argv[2]
forward = open(file, 'r')
reverse = open(file_2, 'r')
f = make_dictionary(forward) 
r = make_dictionary(reverse)

print f.keys()
print r.keys()

unweighted_out = open("pingpong_counts_unweighted.out",'w')
weighted_out = open("pingpong_counts_weighted.out",'w')
for key in f.keys():
	counts = [0]*20
	weighted_counts = [0.0]*20
	maxpos = max(f[key].keys()) -20

	te_dict = f[key]
	total_counts = sum(te_dict.values())
	print total_counts
	
	for pos, count in f[key].iteritems():
		#print pos, maxpos
		if pos > maxpos:
			break
	
		if total_counts > 0:

			weight = float(count)/float(total_counts)
		#print "pos=", pos, "count=",count, "weight=",weight, "total_counts=",total_counts		
		
			if count > 0: 
				for i in range (0 , 20):
					k = pos + i
					try :
						counts[i] += r[key][k]
						weighted_counts[i] += float(r[key][k])*weight
					except KeyError:
						break
			
	print >> unweighted_out, key, "\t".join([str(x) for x in counts])
	print >> weighted_out,  key, "\t".join([str(x) for x in weighted_counts])

#f = {}
#r={}
# with forward as data_file:
# 	for row in data_file:
# 		te, pos, count = row.strip().split()
# 		#f.setdefault(row[0], {})[int(row[1])] = int(row[2])
# 		f.setdefault(te, {})[int(pos)] = int(count)
# 
# print (f)
# 
# with reverse as data_file2:
# 	for row in data_file2:
# 		row = row.strip().split()
# 		r.setdefault(row[0], {})[int(row[1])] = int(row[2])
# print (r)
# 
# 
# 	