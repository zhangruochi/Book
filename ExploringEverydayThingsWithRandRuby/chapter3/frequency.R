require(ggplot2)

data <- read.table("simulation1.csv",header=TRUE,sep=",")
#print(data)
df <- data.frame(table(data$X170))
colnames(df) <- c("queue_size","frequency")
percent_labels <- paste(df$frequency,'(',round(df$frequency * 100 /540, 2), '%)')
print(percent_labels)
print(df)


ggplot(data=df) + scale_fill_grey(start = 0.6, end = 0.8) + 
geom_bar(stat = "identity",aes(x = queue_size, y = frequency, fill = factor(queue_size)))+
geom_text(aes(x=queue_size,y=frequency,label = percent_labels,size = 1)) +
scale_y_continuous("frequency")+
scale_x_discrete("queue size")
ggsave("frequency.jpg")    
