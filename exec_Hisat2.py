import os, sys, shutil

## configuration ##
species_list = ['hg38','mm10','SarSca1.0']
species = species_list[0]

is_paired = 'yes'
is_Rsubread = 'yes'

Hisat2_dir = '/Users/petadimensionlab/ws/apps/Hisat2/'
genome_dir = os.path.join(Hisat2_dir,'idx/'+species)

thread_num = 12 

input_dir = '/Users/petadimensionlab/Downloads/test01/output/SRR5063982_hisat/'
output_dir = '/Users/petadimensionlab/Downloads/test01/output/SRR5063982_hisat/'
#rc_dir = '/Users/petadimensionlab/Downloads/test01/output/SRR5063982_hisat/readcounts/'
files = open( os.path.join(input_dir,'fastq_files.txt') ).readlines()

## options ##
thread = str(thread_num)

## Hisat2 ##
for f in files:
    sID = f.replace('\n','')
    #sID_dir = os.path.join(output_dir,sID)
    #if not os.path.exists(sID_dir):
    #    os.mkdir(sID_dir)
    outsamFile = os.path.join(output_dir,sID+'.')
    if is_paired=='yes':
        fwd_fastq = os.path.join(input_dir,sID+'_R1_trim_paired.fastq.gz') #SRR4888615_R1_trim_paired.fastq.gz
        rev_fastq = os.path.join(input_dir,sID+'_R2_trim_paired.fastq.gz') #SRR4888615_R1_trim_paired.fastq.gz
        cmd = 'hisat2 -x %s -1 %s -2 %s -p %s -S %ssam' % (genome_dir,fwd_fastq,rev_fastq,thread,outsamFile)
        os.system(cmd)

        ## sam to bam ##
        cmd = 'samtools view -@ %s -Sb %ssam > %sbam' % (thread,outsamFile,outsamFile)
        os.system(cmd)
    else:
        fastq_file = os.path.join(input_dir,sID+'.fastq.gz')
        cmd = 'hisat2 -x %s -U %s -p %s -S %ssam' % (genome_dir,fastq_file,thread,outsamFile)
        os.system(cmd)

        ## sam to bam ##
        cmd = 'samtools view -@ 8 -Sb %ssam > %sbam' % (outsamFile,outsamFile)
        os.system(cmd)


    if is_Rsubread=='yes':
        ## extract read count by Rsubread ##
        cmd = 'R --vanilla --slave --args %s %s %s < exec_bam2readcount_gtf_Hisat2.R' % (species,output_dir,sID)
        os.system(cmd)
        ## remove output ##
        #if not os.path.exists(rc_dir):
            #os.mkdir(rc_dir)
        #rc_file_name = sID+'_rc.txt'
        #rc_file = os.path.join(rc_dir,rc_file_name)
        #if os.path.exists(rc_file):
        #    shutil.rmtree(sID_dir)
