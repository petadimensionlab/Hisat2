rm( list=ls(all=TRUE) ) # clean up R workspace

library(Rsubread)

core_num <- 24 # core number

gtf_dir <- "/Users/petadimensionlab/ws/apps/sra2rc/gtf/"
species <- commandArgs(trailingOnly=TRUE)[1]
organism_gtf <- paste(gtf_dir,species,".gtf",sep="")
output_dir = commandArgs(trailingOnly=TRUE)[2]
#rc_dir <- paste(output_dir,"readcounts/",sep="")

sID <- commandArgs(trailingOnly=TRUE)[3]
inputfile <- paste(output_dir,sID,".bam",sep="")
x <- featureCounts(files=inputfile,annot.ext=organism_gtf,isGTFAnnotationFile=TRUE,GTF.featureType="exon",GTF.attrType="gene_id",nthreads=core_num)
## save gene-symbol and read cound file ##
sfn <- paste(output_dir,sID,"_rc.txt",sep="")
write.table(x$counts,file=sfn,quote=F,col.names=F,sep="\t")

