library('ggplot2')
library('dplyr')
library('magrittr')
library('lubridate')


# Change your directory 
wd="C:/Users/balaj/OneDrive/Desktop/ml"
setwd(wd)

data=read.csv("dataset.csv")
data$Number.of.Offers = as.numeric(data$Number.of.Offers) # Discrete continuous value error

plot<-ggplot(data=data,aes(x=Number.of.Offers))+
  ggtitle("Distribution of number of offers")+
  geom_bar()+
  theme(axis.text.x = element_text(angle = 0, hjust = 1))
plot

