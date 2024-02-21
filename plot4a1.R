library('ggplot2')
library('dplyr')
library('magrittr')
library('lubridate')


# Change your directory 
wd="C:/Users/balaj/OneDrive/Desktop/ml"
setwd(wd)

data=read.csv("dataset.csv")
c_data <- data.frame(type=character(), 
                    count=integer(),
                    perc=double(),
                    stringsAsFactors=FALSE)
c_data[1,1]="Veg"
c_data[1,2]=0
c_data[2,1]="Non Veg"
c_data[2,2]=0

c_data
for (i in 1:nrow(data))
{
  typei=data[i,9]
  if(typei=="Yes")
  {
    c_data[1,2]=c_data[1,2]+1
  }
  else
  {
    c_data[2,2]=c_data[2,2]+1
  }
}
c_data[1,3]=(c_data[1,2]/(c_data[1,2]+c_data[2,2]))*100
c_data[2,3]=(c_data[2,2]/(c_data[1,2]+c_data[2,2]))*100
c_data

plot<-ggplot(c_data, aes(x="", y=count, fill=type)) +
  ggtitle("Veg vs Non Veg") +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) +
  geom_text(aes(label = paste0(perc, "%")), position = position_stack(vjust=0.5)) +
  labs(x = NULL, y = NULL) +
  theme_classic() +
  theme(axis.line = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank()) +
  scale_fill_brewer(palette="Blues")

plot

