# CNV calling

The CNV calling step consist on calling CNV variants.

With the emergence of NGS sequencing technologies, CNV detection methods have also evolved. 
Several tools have been developed for the discovery of cNV from NGS data. 
Mainly due to the accumulation of high-coverage NGS data, RD-based methods have recently become a major approach to estimate copy numbers. 
The underlying hypothesis of RD-based methods is that the depth of coverage in a genomic region is correlated with the copy number of the region, e.g., a gain of copy number should have a higher intensity than expected.  
According to the literature, ERDS and CNVnator are the two methods that provide the best performance on whole genome
sequencing data with respect to CNV consistency across families, CNV breakpoint resolution and CNV call specificity. The intersection of the calls from the two tools would be valuable for CNV genotyping pipelines.
We then combine both methods.

This folder contains:
  1. The main scripts:  	CNVNATORscript.py (and ERDSscript.py)
  2. The submission scripts:  	submitCNVNATORscript.py (and submitERDSscript.py)

  

## Dependencies:
This step makes use of the following software(s):
   * cnvnator (https://github.com/abyzovlab/CNVnator)
   * ERDS (http://www.utahresearch.org/mingfuzhu/erds/)

   

