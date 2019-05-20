from Bio import SeqIO
import sys, os
file= sys.argv[1]
a=[6000,23008,859966,866477,19208449,19231954,19736655,19783874,20177515,20255476,20113427,20300014,20707375,20829444]
from Bio import SeqIO
for record in SeqIO.parse(file, 'fasta'):
	if record.id == 'Scf_X':
		cluster1=record.seq[a[0]:a[1]]
		cluster2=record.seq[a[2]:a[3]]
		cluster3=record.seq[a[4]:a[5]]
		cluster4=record.seq[a[6]:a[7]]
		cluster5=record.seq[a[8]:a[9]]
		cluster6=record.seq[a[10]:a[11]]
		cluster7=record.seq[a[12]:a[13]]
		
print(">Cluster_1_ref")
for i in range(0, len(cluster1), 80):
	print (cluster1[i:(i+80)])
print(">Cluster_2_ref")
for i in range(0, len(cluster2), 80):
	print (cluster2[i:(i+80)])
print(">Cluster_3_ref")
for i in range(0, len(cluster3), 80):
	print (cluster3[i:(i+80)])
print(">Cluster_4_ref")
for i in range(0, len(cluster4), 80):
	print (cluster4[i:(i+80)])
print(">Cluster_5_ref")
for i in range(0, len(cluster5), 80):
	print (cluster5[i:(i+80)])
print(">Cluster_6_ref")
for i in range(0, len(cluster6), 80):
	print (cluster6[i:(i+80)])
print(">Cluster_7_ref")
for i in range(0, len(cluster7), 80):
	print (cluster7[i:(i+80)])
