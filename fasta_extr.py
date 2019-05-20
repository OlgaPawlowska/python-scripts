import sys, os
file= sys.argv[1]
genepath=open(file, "r")

from Bio import SeqIO
records=SeqIO.index(file, "fasta")
print(records["Scf_X_assembled"].format("fasta"))
