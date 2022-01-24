library(methods)

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
