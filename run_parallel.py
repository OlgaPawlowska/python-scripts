from Queue import Queue
from threading import Thread
import subprocess
import os 

class Worker(Thread):
	"""Thread executing tasks from a given tasks queue"""
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()
	
	def run(self):
		while True:
			func, args = self.tasks.get()
			try: func(*args)
			except Exception, e: print e
			self.tasks.task_done()

class ThreadPool:
	"""Pool of threads consuming tasks from a queue"""
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args):
		"""Add a task to the queue"""
		self.tasks.put((func, args))
		#print "added"

	def wait_completion(self):
		"""Wait for completion of all the tasks in the queue"""
		self.tasks.join()

if __name__ == '__main__':
	import time, os
	
	def run(passed_args):
		# prog ="bwa aln "
		prog = "/Volumes/Temp/olga/bin/bwa aln "
		cmmd = prog +passed_args
		print cmmd
		subprocess.call(cmmd, shell=True)
		time.sleep(10)


	filenames='''/home/olga/no_adapt/no_adapt/Lps3_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Lps5_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Lps6_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Hin17_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA02_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA12_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA14_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA18_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA20_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA26_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA27_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA34_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Lps3-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Lps5-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Lps6-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/Hin17-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA02-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA12-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA14-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA18-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA20-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA26-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA27-2_no_adapt.fastq.gz
/home/olga/no_adapt/no_adapt/SGA34-2_no_adapt.fastq.gz
'''
	filenames = filenames.strip().split('\n')
	print filenames
	outpath = "/home/olga/dsim_miRNA/mapping"
	ref_genome_masked = "/home/olga/dsim_miRNA/dsim-all-miRNA-r2.02.fasta"
	
	#bwa aln -I -m 100000 -o 1 -n 0.01 -l 70 -e 1 -d 1 -t 2 reference_genome_TE/transposon_sequence_set.fasta DGRP/piRNA/RAL303.fastq.fq > RAL303.sai
	
	# 1) Init a Thread pool with the desired number of threads/number of processes you want to run at the same time
	pool = ThreadPool(4)
	counter =0
	args_same="-l 40 -n 1 -t 3"

	for filename in filenames:
		outname = os.path.split(filename)[-1]
		outname = outname.rstrip('fq')+'.sai'
		outname = os.path.join(outpath, outname)
		print "Outfile is named", outname
		cmmd = args_same+" "+ref_genome_masked+" "+filename + " > "+outname
		# 2) Add the task to the queue
		#print cmmd 
		
		
		
		pool.add_task(run,cmmd)

	# 3) Wait for completion
	pool.wait_completion()


