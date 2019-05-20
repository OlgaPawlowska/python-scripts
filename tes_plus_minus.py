from Bio import SeqIO
import pandas as pd
import numpy as np
import sys, os
file=sys.argv[1]

colnames=['query', 'query_start', 'query_end', 'te', 'sw_score', 'strand','column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'repeat_begin', 'repeat_end', 'column8', 'column9']
clusters_dsim=pd.read_csv(file, names = colnames, sep='\t')
clusters_dsim=clusters_dsim[['query','query_start', 'query_end', 'te', 'strand']]
dsim_5x=clusters_dsim[clusters_dsim['query']=='Cluster_4_SGA26']
dsim_6x=clusters_dsim[clusters_dsim['query']=='Cluster_5_SGA26']
dsim_7x=clusters_dsim[clusters_dsim['query']=='Cluster_6_SGA26']

dsim_minus_5x=dsim_5x[dsim_5x['strand']=="-"]
dsim_plus_5x=dsim_5x[dsim_5x['strand']=="+"]

dsim_minus_6x=dsim_6x[dsim_6x['strand']=="-"]
dsim_plus_6x=dsim_6x[dsim_6x['strand']=="+"]

dsim_minus_7x=dsim_7x[dsim_7x['strand']=="-"]
dsim_plus_7x=dsim_7x[dsim_7x['strand']=="+"]

minus_5x=dsim_minus_5x['te'].tolist()
plus_5x=dsim_plus_5x['te'].tolist()

minus_6x=dsim_minus_6x['te'].tolist()
plus_6x=dsim_plus_6x['te'].tolist()

minus_7x=dsim_minus_7x['te'].tolist()
plus_7x=dsim_plus_7x['te'].tolist()

print('All TE insertions in Lps5 cluster 5 on + strand', len(plus_5x))
print('TE families on + strand', len(np.unique(plus_5x)))

print('All TE insertions in Lps5 cluster 5 on - strand', len(minus_5x))
print('TE families on - strand', len(np.unique(minus_5x)))

print('All TE insertions in Lps5 cluster 6 on + strand', len(plus_6x))
print('TE families on + strand', len(np.unique(plus_6x)))

print('All TE insertions in Lps5 cluster 6 on - strand', len(minus_6x))
print('TE families on - strand', len(np.unique(minus_6x)))

print('All TE insertions in Lps5 cluster 7 on + strand', len(plus_7x))
print('TE families on + strand', len(np.unique(plus_7x)))

print('All TE insertions in Lps5 cluster 7 on - strand', len(minus_7x))
print('TE families on - strand', len(np.unique(minus_7x)))

TEs_info=pd.read_csv('/Users/olga/Dropbox/Thesis/PacBio/clusters/TE_info.txt', sep='\t')

TEs_info=TEs_info[['Family', 'Subclass']]

from collections import OrderedDict
TE_dict=OrderedDict(TEs_info.values.tolist())

for each_te in minus_5x: 
	print('5X', '-', each_te, TE_dict[each_te])
	
for each_te in plus_5x: 
	print('5X', '+', each_te, TE_dict[each_te])
	
for each_te in minus_6x: 
	print('6X', '-', each_te, TE_dict[each_te])
	
for each_te in plus_6x: 
	print('6X', '+', each_te, TE_dict[each_te])	

for each_te in minus_7x: 
	print('7X', '-', each_te, TE_dict[each_te])
	
for each_te in plus_7x: 
	print('7X', '+', each_te, TE_dict[each_te])