
##############    DASH library

library(ggplot2)
library(plotly)
library(gapminder)
library(grappolo)
library(CytoDx)
library(Biobase)




# p <- gapminder %>%
#   filter(year==1977) %>%
#   ggplot( aes(gdpPercap, lifeExp, size = pop, color=continent)) +
#   geom_point() +
#   theme_bw()

# ggplotly(p)



# file_path <- "C:/Users/Zuhayr/Downloads/776 F SP.fcs"
# file <- flowCore::read.FCS(file_path)
# #convert_fcs(file)
# #fcs2DF(file)
# #file <- as.data.frame(file)
# file <- exprs(file)
# typeof(file)
# # p <- file %>%
# #   ggplot(aes("FSC-A", "FSC-H")) +
# #   geom_point() +
# #   theme_bw()

# # ggplotly(p)






# library(plotly) 
# library(umap) 
# iris.data = iris[, grep("Sepal|Petal", colnames(iris))] 
# iris.labels = iris[, "Species"] 
# iris.umap = umap(iris.data, n_components = 2, random_state = 15) 
# layout <- iris.umap[["layout"]] 
# layout <- data.frame(layout) 
# final <- cbind(layout, iris$Species) 

# fig <- plot_ly(final, x = ~X1, y = ~X2, color = ~iris$Species, colors = c('#636EFA','#EF553B','#00CC96'), type = 'scatter', mode = 'markers')%>%  
#   layout(
#     plot_bgcolor = "#e5ecf6",
#     legend=list(title=list(text='species')), 
#     xaxis = list( 
#       title = "0"),  
#     yaxis = list( 
#       title = "1")) 

# iris.umap = umap(iris.data, n_components = 3, random_state = 15) 
# layout <- iris.umap[["layout"]] 
# layout <- data.frame(layout) 
# final <- cbind(layout, iris$Species) 

# fig2 <- plot_ly(final, x = ~X1, y = ~X2, z = ~X3, color = ~iris$Species, colors = c('#636EFA','#EF553B','#00CC96')) 
# fig2 <- fig2 %>% add_markers() 
# fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = '0'), 
#                                      yaxis = list(title = '1'), 
#                                      zaxis = list(title = '2'))) 

# fig 
# save_image(fig, "temporary_images/staticThing.png")
