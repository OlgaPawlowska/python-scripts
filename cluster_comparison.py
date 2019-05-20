'''This script compares TEs in piRNA clusters'''
from Bio import SeqIO
import pandas as pd
import numpy as np
import sys, os
file=sys.argv[1]
file2=sys.argv[2]

colnames=['query', 'query_start', 'query_end', 'te', 'sw_score', 'strand','column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'repeat_begin', 'repeat_end', 'column8', 'column9']
clusters_dmel=pd.read_csv(file, names = colnames, sep='\t')
clusters_dsim=pd.read_csv(file2, names = colnames, sep='\t')

#print(clusters_dmel.head())
#print(clusters_dsim.head())

clusters_dmel=clusters_dmel[['query','query_start', 'query_end', 'te', 'strand']]
clusters_dsim=clusters_dsim[['query','query_start', 'query_end', 'te', 'strand']]

dsim_5x=clusters_dsim[clusters_dsim['query']=='Cluster_5_X']
#print(dsim_5x.head())
#print(clusters_dmel.head())

'''filtering for - and + strand TEs'''
dmel_minus=clusters_dmel[clusters_dmel['strand']=="-"]
dmel_plus=clusters_dmel[clusters_dmel['strand']=="+"]

dsim_minus=dsim_5x[dsim_5x['strand']=="-"]
dsim_plus=dsim_5x[dsim_5x['strand']=="+"]

dmel_pl=dmel_plus['te'].tolist()
dmel_min=dmel_minus['te'].tolist()

ds_min=dsim_minus['te'].tolist()
ds_pl=dsim_plus['te'].tolist()

print('All TE insertions in D. simulans flamenco on + strand', len(ds_pl))
print('TE families on + strand', len(np.unique(ds_pl)))
print('All TE insertions in D. simulans flamenco on - strand',len(ds_min))
print('TE families on - strand',len(np.unique(ds_min)))

print('All TE insertions in D. melanogaster flamenco on + strand', len(dmel_pl))
print('TE families on + strand', len(np.unique(dmel_pl)))
print('All TE insertions in D. melanogaster flamenco on - strand',len(dmel_min))
print('TE families on - strand',len(np.unique(dmel_min)))

TEs_info=pd.read_csv('/Users/olga/Dropbox/Thesis/PacBio/clusters/TE_info.txt', sep='\t')
#print(TEs_info.head())
TEs_info=TEs_info[['Family', 'Subclass']]
from collections import OrderedDict
TE_dict=OrderedDict(TEs_info.values.tolist())
#print(TE_dict)

for each_te in ds_min: 
	print('D.sim', '-', each_te, TE_dict[each_te])
	
for each_te in ds_pl: 
	print('D.sim', '+', each_te, TE_dict[each_te])
	

for each_te in dmel_min: 
	print('D.mel', '-', each_te, TE_dict[each_te])

	
for each_te in dmel_pl: 
	print('D.mel', '+',each_te, TE_dict[each_te])