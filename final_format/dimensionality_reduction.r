#jpeg("user_plot.jpeg", quality = 75)
#plot(iris)
#dev.off()
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


#p <- ggplot(iris, aes(x=Sepal.Length, y=Sepal.Width)) + geom_point()
#p
#ggsave("temporary_images/user_plot.jpeg")

set.seed(42)

fcsFile <- "C:/Users/Zuhayr/Downloads/776 F SP.fcs"

x  <- read.FCS(filename = fcsFile, truncate_max_range = FALSE)
x
matrixFormat <- exprs(x)
matrixShort <- head(matrixFormat, -1429593)
#matrixShort

umapStuff <- umap(matrixShort, init = "pca")
#umapStuff
umapStuff_df <- data.frame(umapStuff$layout)
#umapStuff_df #
# umapStuff_df <- cbind.data.frame(
#    setNames(as.data.frame(umapStuff_df), c("x", "y")),
#    matrixShort,
#    color = rgb(
#      rescale(matrixShort["SSC-W"]),
#      rescale(matrixShort["SSC-H"]),
#      rescale(matrixShort["FSC-W"]),
#      maxColorValue = 255
#    )
#  )


thing <- ggplot(umapStuff_df, aes(x = X1, y = X2, color = "red")) + 
        geom_point() + #
        scale_color_identity() +
        new_scale_color() +
        #shape = NA --> invisible layers +
        geom_point(aes(color = SSC-W), shape = NA) +
        scale_color_gradient(low = "black", high = "red") +
        new_scale_color() +
        geom_point(aes(color = SSC-H), shape = NA) +
        scale_color_gradient(low = "black", high = "green") +
        new_scale_color() +
        geom_point(aes(color = FSC-W), shape = NA) +
        scale_color_gradient(low = "black", high = "blue")

thing
ggsave("temporary_images/actual_plot.png")