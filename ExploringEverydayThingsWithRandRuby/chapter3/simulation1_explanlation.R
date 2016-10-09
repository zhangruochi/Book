library(ggplot2)

data <- read.table("simulation1.csv",header=TRUE,sep=',')
mean <- apply(data,2,mean)  
median <- apply(data,2,median)
max <- apply(data,2,max)

df <- data.frame(poplation=seq(from=10,to=600,by=10),mean = mean,median=median,max=max)
print(df)
#head(data)
#summary(data)
#dim(data)



graph <- ggplot(data = df) + scale_shape_manual(name='Type',values=c(2,3,4)) + 
geom_smooth(aes(x=poplation,y=mean)) + geom_point(aes(x=poplation,y=mean,shape="mean")) +
geom_smooth(aes(x=poplation,y=median)) + geom_point(aes(x=poplation,y=median,shape="median")) +
geom_smooth(aes(x=poplation,y=max)) + geom_point(aes(x=poplation,y=max,shape="max")) +
scale_y_continuous("queue size",breaks=seq(0,500,50)) + scale_x_continuous("poplation",breaks=seq(from=10,to=650,by=30))

ggsave("similation1.jpg")



