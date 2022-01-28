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
library(xfun)
library(Rtsne)


# #perform PCA
# results <- prcomp(USArrests, scale = TRUE)

# #calculate total variance explained by each principal component
# var_explained = results$sdev^2 / sum(results$sdev^2)

# #create scree plot
# library(ggplot2)

# qplot(c(1:4), var_explained) + 
#   geom_line() + 
#   xlab("Principal Component") + 
#   ylab("Variance Explained") +
#   ggtitle("Scree Plot") +
#   ylim(0, 1)

# print(var_explained)


#perform PCA
file = "C:/Users/Zuhayr/Downloads/776 F SP.fcs"

# file.name <- system.file("extdata", file,
# package="flowCore")
# print(file.name)
x <- read.FCS(file, transformation=FALSE)
summary(x)

#tail(mylist, -2

# count_file <- file[-1,]
# count_file <- file[,-c(1,2, 3, 4, 5, 6, 7, 8)]
#needs to have a count only matrix input\
# file <- flowCore::read.FCS(file)
# matrix1 <- matrix(file)

# matrix2 <- matrix1[1:2, 1:2]
# print(matrix2)
results <- prcomp(count_file, scale = TRUE)

#calculate total variance explained by each principal component
var_explained = results$sdev^2 / sum(results$sdev^2)

#create scree plot
library(ggplot2)

qplot(c(1:4), var_explained) + 
  geom_line() + 
  xlab("Principal Component") + 
  ylab("Variance Explained") +
  ggtitle("Scree Plot") +
  ylim(0, 1)

print(var_explained)




#############################################################################
#tSNE
#############################################################################

iris_unique <- unique(iris) # Remove duplicates
set.seed(42) # Sets seed for reproducibility
tsne_out <- Rtsne(as.matrix(iris_unique[,1:4])) # Run TSNE
#plot(tsne_out$Y,col=iris_unique$Species,asp=1) # Plot the result