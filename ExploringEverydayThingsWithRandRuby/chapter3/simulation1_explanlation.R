library(ggplot2)
data <- read.table("simulation1.csv",header=TRUE,sep=',')
mean <- apply(data,2,mean)  
median <- apply(data,2,median)
max <- apply(data,2,max)


