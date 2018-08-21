#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("/mnt/DATA/home4/arc/hb493/GF20/output/b37/BWAMEM/GATK/")
outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF20/output/b37/SV/pindel/")

#indir =os.path.dirname("/mnt/b2/home4/arc/hb493/Rimma_fastq/PICARD/output/")
#outdir = os.path.dirname("/mnt/b2/home4/arc/hb493/Rimma_fastq/CNV/cnvnator")

bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	
	# save the basename  and ending	
	fbasename = file.split(".QC.MAP.s.MDup.RGr.BRec.IReal.bam", 1)[0]
	nn  =  fbasename + ".QC.MAP.s.MDup.RGr.BRec.IReal.bam"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".QC.MAP.s.MDup.RGr.BRec.IReal.bam")



for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
 	print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/pipB37/PINDELscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
 	print "sbatch --partition=MAPR /mnt/DATA/home4/arc/hb493/bin/submit_sbatch10.sh"
 	print "export SBATCH_CMD=\"\""

