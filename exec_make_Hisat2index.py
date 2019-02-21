#Set bioconda , conda intall hisat2
import os,sys

## configuration ##
species_list = ['hg38','mm10','SarSca1.0']
species = species_list[2]

Hisat2_dir =  '/Users/petadimensionlab/ws/apps/Hisat2/idx/' 

input_dir = '/Users/petadimensionlab/ws/apps/sra2rc/tools/bowtie2/indexes'

genome_dir = os.path.join(Hisat2_dir,'idx/'+species)

## options ##
genomeFastaFiles = os.path.join(input_dir,species+'.fna')

## build index ##
cmd = 'hisat2-build %s %s' % (genomeFastaFiles,species)
#print cmd
os.system(cmd)

## Change the access permission ##
cmd = 'chmod +x *.ht2'
os.system(cmd)

## move indexes ##
#if not os.path.exists(genome_dir):
       # os.mkdir(genome_dir)
cmd = 'mv ./*.ht2 %s' % (Hisat2_dir)
os.system(cmd)