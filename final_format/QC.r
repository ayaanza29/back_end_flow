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


things <- function(stuff) {
    print(5)
}



  
movies <- setRefClass("movies", fields = list(name = "character", 
                       leadActor = "character", rating = "numeric"), methods = list(
                       increment_rating = function()
                       {
                           rating <<- rating + 1
                       },
                       decrement_rating = function()
                       {
                           rating <<- rating - 1
                       }
                     ))





# General pipeline for preprocessing and quality control with PeacoQC
fcsFile <- "C:/Users/Zuhayr/Downloads/776 F SP.fcs"
# Read in raw fcs file
#fileName <- system.file("C:/Users/Zuhayr/Downloads/776 F SP.fcs")
fileName <- "C:/Users/Zuhayr/Downloads/776 F SP.fcs"
#ff <- flowCore::read.FCS(fileName)
ff <- flowCore::read.FCS("C:/Users/Zuhayr/Downloads/776 F SP.fcs")

# Define channels where the margin events should be removed
# and on which the quality control should be done
channels <- c(1, 3, 5:14, 18, 21)

#ff <- RemoveMargins(ff=ff, channels=channels, output="frame")

# Compensate and transform the data

# ff <- flowCore::compensate(ff, flowCore::keyword(ff)$SPILL)


# ff <- flowCore::transform(ff,
#                             flowCore::estimateLogicle(ff,
#                             colnames(flowCore::keyword(ff)$SPILL)))


#Run PeacoQC
PeacoQC_res <- PeacoQC(ff, channels,
                        determine_good_cells="all",
                        save_fcs=TRUE)





