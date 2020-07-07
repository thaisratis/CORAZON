library('ggplot2')
suppressMessages(library(plotly))
library('reshape2')
argv<-commandArgs(TRUE)


filename <- argv[1]
normalized_filename <- argv[2]
user <- argv[3]
id <- argv[4]


input_file<- read.csv(filename, sep="\t", head = T)
var = t(input_file)
input_file_melt <- melt(input_file, id.vars = colnames(input_file[1]))
m <- list(
    l = 50,
    r = 50,
    b = 100,
    t = 100,
    pad = 4
)

figure <- ggplotly( ggplot(data = input_file_melt, aes(x = input_file_melt$variable, y = input_file_melt$value)) + 
                      geom_boxplot(outlier.shape = NA) +
                      geom_jitter(position = position_jitter(0.2))+
                      ggtitle("Before Normalization \n") +
                      labs(x = "Samples", y = "Expression Values") + 
                      theme(axis.text.x = element_text(angle = 90), 
                            plot.title = element_text(hjust = 0.5, size=22, face="bold"),
                            axis.title.x = element_text(size=16, face="bold"),
                            axis.title.y = element_text(size=16, face="bold")))%>%
	layout(autosize = F, width = 1700, height = 800, margin = m) 

htmlwidgets::saveWidget(as_widget(figure), selfcontained = TRUE, file = sprintf("/var/www/html/users/%s/%s/boxplot_bn.html",user,id))

input_normalized_file<- read.csv(normalized_filename, sep="\t", head = T)
var = t(input_normalized_file)
input_normalized_file_melt <- melt(input_normalized_file, id.vars = colnames(input_normalized_file[1]))


figure_normalization <- ggplotly( ggplot(data = input_normalized_file_melt, aes(x = input_normalized_file_melt$variable, y = input_normalized_file_melt$value)) +
                     geom_boxplot(outlier.shape = NA) +
                     geom_jitter(position = position_jitter(0.2))+
                     ggtitle("After Normalization \n") +
                     labs(x = "Samples", y = "Expression Values") +
                     theme(axis.text.x = element_text(angle = 90),
                           plot.title = element_text(hjust = 0.5, size=22, face="bold"),
                           axis.title.x = element_text(size=16, face = "bold"),
                           axis.title.y = element_text(size=16, face = "bold")) )%>%
		layout(autosize = F, width = 1700, height = 800, margin = m)

htmlwidgets::saveWidget(as_widget(figure_normalization), selfcontained = TRUE, file = sprintf("/var/www/html/users/%s/%s/boxplot_an.html",user,id))









