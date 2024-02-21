library('ggplot2')
library('dplyr')
library('magrittr')
library('lubridate')


# Change your directory 
wd="C:/Users/balaj/OneDrive/Desktop/ml/assn1"
setwd(wd)

data=read.csv("dataset.csv")
data$Rating = as.numeric(data$Rating) # Discrete continuous value error

plot<-ggplot(data=data,aes(x=Rating))+
  ggtitle("Distribution of restaurant ratings")+
  geom_bar()+
  scale_x_continuous(breaks=seq(from=1, to=5, by=1),limits=c(1,5))+
  theme(axis.text.x = element_text(angle = 0, hjust = 1))
plot

