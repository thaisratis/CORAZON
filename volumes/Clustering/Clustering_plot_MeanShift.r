library('ggplot2')
suppressMessages(library(plotly))
library('reshape2')
argv<-commandArgs(TRUE)
options(warn=-1)

filename <- argv[1]
result_filename <- argv[2]
user <- argv[3]
id <- argv[4]

result<- read.csv(result_filename, sep="\t", head = F, skip = 4)
input_file<-read.csv(filename, sep="\t", head = T)
colnames(input_file)[1] <- "V1"

if(result$V1 == input_file$V1){
  result_input<- merge(result, input_file)
}


Clusters <- factor(result_input$V2)
end<- result_input[,-2]
end_PCA <- prcomp(scale(end[,-1]))
convert <- data.frame(end_PCA$x[,1:2])


figure<- ggplotly (ggplot(convert, aes(x=PC1,y=PC2,color=Clusters))+
  geom_point(size=3)+
  ggtitle("Clustering \n") +
  theme_bw()+
  theme(axis.text.x = element_text(angle = 90), 
          plot.title = element_text(hjust = 0.5, size=22, face="bold"),
          axis.title.x = element_text(size=16, face="bold"),
          axis.title.y = element_text(size=16, face="bold")) )

htmlwidgets::saveWidget(as_widget(figure), selfcontained = TRUE, file = sprintf("/var/www/html/users/%s/%s/Clustering.html",user,id))
