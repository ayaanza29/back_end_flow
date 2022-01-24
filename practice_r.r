#fileName <- system.file("extdata", "C:/Users/Zuhayr/Downloads/776 F SP.fcs", package="FlowSOM")
set.seed(42)
library(FlowSOM)

fSOM <- FlowSOM(ff, compensate = FALSE, transform = FALSE, scale = FALSE, colsToUse = c(9, 12, 14:18), xdim = 7, ydim = 7, nClus = 10)

#p <- PlotStars(fSOM, background.values = fSOM$metaclustering)
p <- PlotStars(fSOM)
print(p, newpage = FALSE)

FlowSOMmary(fsom = fSOM, plotFile = "FlowSOMmary.pdf")

head(GetClusters(fSOM))
head(GetMetaclusters(fSOM))


