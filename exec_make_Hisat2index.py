#### conda config --add channels defaults ####
#### conda config --add channels bioconda ####
#### conda config --add channels conda-forge ####
#### conda intall hisat2 ####
#### conda install samtools ####
import os
import glob

## configuration ##
species_list = ['hg38','mm10','sarsca1.0']
species = species_list[2]

root_dir = os.getcwd()
Hisat2idx_dir =  os.path.join('/Users/petadimensionlab/ws/ref/Hisat2idx/'+species)
genome_dir = '/Users/petadimensionlab/ws/ref/genome/'

if not os.path.exists(Hisat2idx_dir):
	cmd = 'mkdir %s' % (idx_dir)
	os.system(cmd)

## options ##
genomeFastaFile = os.path.join(genome_dir,species+'.fna')

## build index ##
cmd = 'hisat2-build %s %s' % (genomeFastaFile,species)
#print(cmd)
os.system(cmd)

## Change the access permission ##
items = glob.glob('*.ht2')
for item in items:
    cmd = 'chmod +x %s' % (item)
    os.system(cmd)
    srcf = os.path.join(root_dir,item)
    destf = os.path.join(Hisat2idx_dir,item)
    cmd = 'mv %s %s' % (srcf,destf)
    os.system(cmd)
