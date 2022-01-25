# library(plateCore)
# data(plateCore)

# # Create the compensation matrix
# comp.mat <- spillover(x=compensationSet,unstained=sampleNames(compensationSet)[5],
# patt=".*H",fsc="FSC-H",ssc="SSC-H",method="median")

# ## Get the lymphocytes
# rectGate <- rectangleGate("FSC-H"=c(300,700),"SSC-H"=c(50,400))
# pbmcPlate <- Subset(pbmcPlate, rectGate)

# # Create a flowPlate from the sample data in plateCore
# fp <- flowPlate(pbmcPlate,wellAnnotation,plateName="P1")

# # apply the compensation matrix
# fp <- compensate(fp,comp.mat)