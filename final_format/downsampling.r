library(spade)
library(methods)
library(umap)
library(dplyr)
#library(Seurat)
library(ggplot2)
library(patchwork)
library(flowCore)
#library(flowViz)
library(magrittr)
library(ggnewscale)
library(scales)
library(PeacoQC)

# Not run
## Load two-parameters sample data included in package
data_file_path = paste(installed.packages()["spade","LibPath"],"spade","extdata","SimulatedRawData.fcs",sep=.Platform$file.sep)

output_dir <- tempdir()
#
## Compute and annotate FCS file with density
density_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
SPADE.addDensityToFCS(data_file_path, density_file_path, cols=c("marker1","marker2"))

## Downsample FCS file based on density
downsample_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
SPADE.downsampleFCS(density_file_path, downsample_file_path)

