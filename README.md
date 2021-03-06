# NGSpy


Next-Generation Sequencing Data Analysis Pipeline with Python scripts


This repository is aimed to provide the basic scripts of a pipeline of Whole Genome Sequencing Data Analysis. <br>
Most scripts are python wrappers for common  Bioinformatic tools. 

# PIPELINE Structure

The pipeline consists of several stages described as follows.

    0. CONVERT
        - Converting bam files (provided by the sequencing platform/company) into paired-end fastq files
    1. QC
        - Performing the QC on fastqc files
    2. Mapping
        - Mapping the reads to a given reference genome
    3. PICARD
        - Marking the duplicates and adding read groups information
    4. GATK
        - Base Recalibration and Indel Realignment
    5.Variant Calling
        - Single Nucleotide Variant calling
        - Structural Variant calling
        - Copy-Number Variant calling
    6. Variant Filtering and annotation
    

Each of these steps has a dedicated python script meant to be submitted in a high performance computing cluster through SLURM


# REQUIREMENTS


## Software Requirements

The pipeline has several software dependencies which may also have secondary dependencies

Stage |-| Dependencies    | Secondary dependencies
------------ |-| -------------| ---------------
ALL |-| samtools (currently running with Version: 0.1.19)|  -     
0-CONVERT |-| bam2fastx |     -       
1-QC      |-| sickle |       -       
   "     |-| trim-galore | cutadapt
2-Mapping |-| bwa-mem (version 0.6 or higher)|     -       
3-PICARD |-| PICARD tools |     -     
4-GATK |-| Genome Analysis ToolKit (version 3.7-0)|    -    
5-VC |SNV| Genome Analysis ToolKit (version 3.7-0)|    -
  "  | " |VARSCAN (version 2.3)|   -
" | SV | Breakdancer | - 
" | " | Pindel | -
" | " | Delly | -
" | CNV | CNVnator | root
" | " |erds (version 1.1)|-
6-Filtering and Annotation | SNV |Genome Analysis ToolKit (version 3.7-0)|    -
" | " | SNPEff (version 4.3) | - 

## Data Requirements

Many of the stages use external data:


Data file    | Example: current file name | Stage where used
------------ | -------------| -------------
Reference Genome| Ensembl_GRCh37.ordered.fa | 2-Mapping <br> 4-GATK <br> 5-VC <br> 6-Filtering and Annotation <br> 7-CNV <br> 8-SV
Known SNPs | 1000G_phase1.snps.high_confidence.b37.sorted.vcf.gz | 4-GATK <br> 5-VC
Known Indels | Mills_and_1000G_gold_standard.indels.b37.sorted.vcf.gz | 4-GATK <br> 5-VC
ExAC | ExAC.r0.3.1.sites.vep.vcf | 6-Filtering and Annotation 
