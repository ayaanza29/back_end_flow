library(methods)

source("final_format/autonomous_gating.r")
source("final_format/QC.r")
source("final_format/downsampling.r")
source("final_format/batch_effect.r")
source("final_format/dimensionality_reduction.r")
source("final_format/clustering.r")
source("final_format/data_visualizations.r")


movieList <- movies(name = "Iron Man", 
                    leadActor = "Robert downey Jr", rating = 7)


movieList$rating
  
# increment and then print the rating
movieList$increment_rating()
movieList$rating
  
# decrement and print the rating
movieList$decrement_rating()
movieList$rating


