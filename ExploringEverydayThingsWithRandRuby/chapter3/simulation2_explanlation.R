require(ggplot2)

data <- read.table("simulatin2.csv",header=TRUE,sep=",")
max <- apply(data,2,max)
mean <- apply(data,2,mean)
median <- apply(data,2,median)

df <- data.frame(population=sep)