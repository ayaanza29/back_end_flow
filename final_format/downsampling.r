library(spade)
library(methods)
library(umap)
library(dplyr)
library(ggplot2)
library(patchwork)
library(flowCore)
library(magrittr)
library(ggnewscale)
library(scales)
library(PeacoQC)


downsample <- setRefClass("downsample", fields = list(data_file_path = "character", 
                       channels = "vector"), methods = list(
                       spade_downsample = function()
                       {
                            all_channels <- c("Time", "SSC-W", "SSC-H", "SSC-A", "FSC-W", "FSC-H", "FSC-A", "SSC-B-W", "SSC-B-H", "SSC-B-A", "BUV395-A", "LIVE DEAD Blue-A",
                             "BUV563-A", "BUV615-A", "BUV661-A", "BUV805-A", "BV421-A", "eFluor 450-A", "eFluor 506-A", "BV605-A", "BV711-A", "BV785-A",
                             "FITC-A", "PerCP-Cy5.5-A", "PE-A", "PE-Cy5-A", "PE-Cy5.5-A", "PE-Cy7-A", "APC-A", "AF680-A", "APC-Cy7-A", "AF-A")
                            # Not run
                            ## Load two-parameters sample data included in package
                            #data_file_path = paste(installed.packages()["spade","LibPath"],"spade","extdata","SimulatedRawData.fcs",sep=.Platform$file.sep)
                            #data_file_path = "C:/Users/Zuhayr/Downloads/776 F SP.fcs"

                            output_dir <- tempdir()
                            #
                            ## Compute and annotate FCS file with density
                            density_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
                            SPADE.addDensityToFCS(data_file_path, density_file_path, cols=NULL) #Check which two columns should be used
                            #c("FSC-A","SSC-A")

                            ## Downsample FCS file based on density
                            downsample_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
                            SPADE.downsampleFCS(density_file_path, downsample_file_path)
                       },    
                       spade_build_tree = function()
                       {
                            output_dir <- tempdir()

                            cells_file_path <- paste(output_dir,"clusters.fcs",sep="")
                            clust_file_path <- paste(output_dir,"clusters.table",sep="")
                            graph_file_path <- paste(output_dir,"mst.gml",sep="")
                            print(cells_file_path)
                            SPADE.FCSToTree(data_file_path, cells_file_path, graph_file_path, clust_file_path, cols=NULL) #cols = NULL selects all channels
                            #SPADE.FCSToTree(downsample_file_path, cells_file_path, graph_file_path, clust_file_path, cols=c("marker1","marker2"), k = 200, arcsinh_cofactor=NULL, transforms=flowCore::arcsinhTransform(a=0, b=0.2), desired_samples = 50000, comp=TRUE)

                       }
                     ))


downsampling_instance <- downsample(data_file_path = "C:/Users/Zuhayr/Downloads/776 F SP.fcs", channels = c(1, 3, 5:14, 18, 21))
#downsampling_instance$spade_downsample()
downsampling_instance$spade_build_tree()






# # Not run
# ## Load two-parameters sample data included in package
# #data_file_path = paste(installed.packages()["spade","LibPath"],"spade","extdata","SimulatedRawData.fcs",sep=.Platform$file.sep)
# data_file_path = "C:/Users/Zuhayr/Downloads/776 F SP.fcs"

# output_dir <- tempdir()
# #
# channels = c("Time", "SSC-W", "SSC-H", "SSC-A", "FSC-W", "FSC-H", "FSC-A", "SSC-B-W", "SSC-B-H", "SSC-B-A", "BUV395-A", "LIVE DEAD Blue-A",
#                              "BUV563-A", "BUV615-A", "BUV661-A", "BUV805-A", "BV421-A", "eFluor 450-A", "eFluor 506-A", "BV605-A", "BV711-A", "BV785-A",
#                              "FITC-A", "PerCP-Cy5.5-A", "PE-A", "PE-Cy5-A", "PE-Cy5.5-A", "PE-Cy7-A", "APC-A", "AF680-A", "APC-Cy7-A", "AF-A")
# ## Compute and annotate FCS file with density
# density_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
# SPADE.addDensityToFCS(data_file_path, density_file_path, cols=NULL) #Check which two columns should be used

# ## Downsample FCS file based on density
# downsample_file_path <- paste(output_dir,.Platform$file.sep,basename(data_file_path),".density.fcs",sep="")
# SPADE.downsampleFCS(density_file_path, downsample_file_path)




# cells_file_path <- paste(output_dir,"clusters.fcs",sep="")
# clust_file_path <- paste(output_dir,"clusters.table",sep="")
# graph_file_path <- paste(output_dir,"mst.gml",sep="")
# SPADE.FCSToTree(downsample_file_path, cells_file_path, graph_file_path, clust_file_path, cols=c("marker1","marker2"))
# #SPADE.FCSToTree(downsample_file_path, cells_file_path, graph_file_path, clust_file_path, cols=c("marker1","marker2"), k = 200, arcsinh_cofactor=NULL, transforms=flowCore::arcsinhTransform(a=0, b=0.2), desired_samples = 50000, comp=TRUE)









# file <- flowCore::read.FCS("C:/Users/Zuhayr/Downloads/776 F SP.fcs")
# rownames(file)
# markers <- c("Cd(110,111,112,114)","Cell_length","Dy(163.929)-Dual","Er(165.930)-Dual","Er(166.932)-Dual","Er(167.932)-Dual","Er(169.935)-Dual","Eu(150.919)-Dual","Eu(152.921)-Dual","Gd(155.922)-Dual","Gd(157.924)-Dual","Gd(159.927)-Dual","Ho(164.930)-Dual","In(114.903)-Dual","Ir(190.960)-Dual","La(138.906)-Dual","Lu(174.940)-Dual","Nd(141.907)-Dual","Nd(143.910)-Dual","Nd(144.912)-Dual","Nd(145.913)-Dual","Nd(147.916)-Dual","Nd(149.920)-Dual","Pr(140.907)-Dual","Sm(146.914)-Dual","Sm(151.919)-Dual","Sm(153.922)-Dual","Tb(158.925)-Dual","Tm(168.934)-Dual","Yb(170.936)-Dual","Yb(171.936)-Dual","Yb(173.938)-Dual","Yb(175.942)-Dual")

# PANELS <- list(list(panel_files=c(file), median_cols=NULL, reference_files=c(file), fold_cols=c()))

# #SPADE.driver(file, out_dir="output", cluster_cols=markers, panels=PANELS, transforms=flowCore::arcsinhTransform(a=0, b=0.2), layout=SPADE.layout.arch, downsampling_target_percent=0.1, downsampling_target_number=NULL, downsampling_target_pctile=NULL, downsampling_exclude_pctile=0.01, k=200, clustering_samples=50000)

# layout <- read.table(file.path("output","layout.table"))
# mst <- read.graph(file.path("output","mst.gml"),format="gml")
# SPADE.plot.trees(mst,"output",file_pattern="*fcs*Rsave",layout=as.matrix(layout),out_dir=file.path("output","pdf"),size_scale_factor=1.2)








