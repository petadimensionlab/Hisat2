## 01: Install parallel-fastq-dump, fastqc, trimmomatic, samtools, hisat2
## 02: conda install -c bioconda -y parallel-fastq-dump
## 03: conda install -c bioconda fastqc
## 04: conda install -c bioconda fastp
## 05: conda install -c bioconda samtools
# if encountered the following error during executing samtools, update conda: ##
# dyld: Library not loaded: @rpath/libcrypto.1.0.0.dylib ##
# conda update --all ##
# see also https://github.com/conda-forge/conda-forge.github.io/issues/701 ##
## 06: conda install -c bioconda hisat2
## 07: brew install pbzip2 or apt-get install pbzip2

import os

is_sra = 'yes'
is_paired = 'yes'
is_qualitycheck = 'yes'
is_delete_FASTQ = 'no'
thread_num = 12 # thread number
species = 'hg38'
annotation_file = species+'.gtf'
annotation = os.path.join('/Users/petadimensionlab/ws/ref/annotation',annotation_file)

root_dir = os.getcwd()+'/'
input_dir = os.path.join(root_dir,'input')
output_dir = os.path.join(root_dir,'output')

fr = open('fastq_files.txt','r').readlines()
for line in fr:
    line = line.replace('\n','')
    lst = line.split(',')
    filename = lst[0]
    samplename = filename
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    msg = '%s is now processing...' % (samplename)
    print( msg )
    cmd = 'python exec_sra2readcount_Hisat2.py %s %s %s %s %d %s %s %s %s %s' % (is_sra,is_paired,is_qualitycheck,is_delete_FASTQ,thread_num,samplename,species,annotation,input_dir,output_dir)
    print( cmd )
    os.system(cmd)

