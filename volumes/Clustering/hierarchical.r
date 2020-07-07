argv<-commandArgs(TRUE)

filename <- argv[1]
methodology <- argv[2]
cuttoff <- argv[3]
user <- argv[4]
id <- argv[5]

Arquivo<- read.csv(filename, sep="\t", header = T)
row.names(Arquivo) <- Arquivo[,1]
Arquivo <- Arquivo[,2:length(Arquivo)]
d <- dist(Arquivo, method = "euclidean") # distance matrix
fit <- hclust(d, method = methodology)
#plot(fit)
groups <- cutree(fit, k=cuttoff)
write.table(format(groups), quote = FALSE, sprintf("/var/www/html/users/%s/%s/teste",user,id),sep= "\t")


