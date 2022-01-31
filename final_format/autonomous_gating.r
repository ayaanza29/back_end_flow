# # library(plateCore)
# # data(plateCore)

# # # Create the compensation matrix
# # comp.mat <- spillover(x=compensationSet,unstained=sampleNames(compensationSet)[5],
# # patt=".*H",fsc="FSC-H",ssc="SSC-H",method="median")

# # ## Get the lymphocytes
# # rectGate <- rectangleGate("FSC-H"=c(300,700),"SSC-H"=c(50,400))
# # pbmcPlate <- Subset(pbmcPlate, rectGate)

# # # Create a flowPlate from the sample data in plateCore
# # fp <- flowPlate(pbmcPlate,wellAnnotation,plateName="P1")

# # # apply the compensation matrix
# # fp <- compensate(fp,comp.mat)



# library(flowClust)

# library(flowCore)
# data(rituximab)

# ### cluster the data using FSC.H and SSC.H
# res1 <- flowClust(rituximab, varNames=c("FSC.H", "SSC.H"), K=1)

# ### remove outliers before proceeding to the second stage
# # %in% operator returns a logical vector indicating whether each
# # of the observations lies within the cluster boundary or not
# rituximab2 <- rituximab[rituximab %in% res1,]
# # a shorthand for the above line
# rituximab2 <- rituximab[res1,]
# # this can also be done using the Subset method
# rituximab2 <- Subset(rituximab, res1)

# ### cluster the data using FL1.H and FL3.H (with 3 clusters)
# res2 <- flowClust(rituximab2, varNames=c("FL1.H", "FL3.H"), K=3)
# show(res2)
# summary(res2)

# # to demonstrate the use of the split method
# split(rituximab2, res2)
# split(rituximab2, res2, population=list(sc1=c(1,2), sc2=3))

# # to show the cluster assignment of observations
# table(Map(res2))

# # to show the cluster centres (i.e., the mean parameter estimates
# # transformed back to the original scale)
# getEstimates(res2)$locations

# ### demonstrate the use of various plotting methods
# # a scatterplot
# plot(res2, data=rituximab2, level=0.8)
# # plot(res2, data=rituximab2, level=0.8, include=c(1,2), grayscale=TRUE,
# #     pch.outliers=2)
# # # a contour / image plot
# # res2.den <- density(res2, data=rituximab2)
# # plot(res2.den)
# # plot(res2.den, scale="sqrt", drawlabels=FALSE)
# # plot(res2.den, type="image", nlevels=100)
# # plot(density(res2, include=c(1,2), from=c(0,0), to=c(400,600)))
# # # a histogram (1-D density) plot
# # hist(res2, data=rituximab2, subset="FL1.H")

# # ### to demonstrate the use of the ruleOutliers method
# # summary(res2)
# # # change the rule to call outliers
# # ruleOutliers(res2) <- list(level=0.95)
# # # augmented cluster boundaries lead to fewer outliers
# # summary(res2)

# # the following line illustrates how to select a subset of data 
# # to perform cluster analysis through the min and max arguments;
# # also note the use of level to specify a rule to call outliers
# # other than the default
# flowClust(rituximab2, varNames=c("FL1.H", "FL3.H"), K=3, B=100, 
#     min=c(0,0), max=c(400,800), level=0.95, z.cutoff=0.5)


##############    DASH library

library(ggplot2)
library(plotly)
library(gapminder)
library(grappolo)
library(CytoDx)
library(Biobase)

p <- gapminder %>%
  filter(year==1977) %>%
  ggplot( aes(gdpPercap, lifeExp, size = pop, color=continent)) +
  geom_point() +
  theme_bw()

ggplotly(p)



file_path <- "C:/Users/Zuhayr/Downloads/776 F SP.fcs"
file <- flowCore::read.FCS(file_path)
#convert_fcs(file)
#fcs2DF(file)
#file <- as.data.frame(file)
file <- exprs(file)
typeof(file)
# p <- file %>%
#   ggplot(aes("FSC-A", "FSC-H")) +
#   geom_point() +
#   theme_bw()

# ggplotly(p)
