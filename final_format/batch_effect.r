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
results <- prcomp(file, scale = TRUE)

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
