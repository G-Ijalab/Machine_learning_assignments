library('ggplot2')
library('dplyr')
library('magrittr')
library('lubridate')

# Change your directory 
wd="C:/Users/balaj/OneDrive/Desktop/ml"
setwd(wd)

data=read.csv("dataset.csv")
dc<-data %>% distinct(Cuisine)
#print(" Distinct Cuisine : ")
# defining empty dataframe to record count values for each distinct cuisines
c_occ <- data.frame(cuisine_name=character(), 
                    count=integer(),
                    stringsAsFactors=FALSE)
for (i in 1:nrow(dc))
{
  cuisine_name<-dc[i,1]
  dcs<-data %>% 
    filter(Cuisine==cuisine_name) %>%
    select(Cuisine)
  c_occ[i,1]=cuisine_name
  c_occ[i,2]=nrow(dcs)
}
# Descending order
c_occ <- c_occ[order(-c_occ$count), ]
# limiting to first 10 rows
c_occ <- c_occ[c(1:15),]

plot<-ggplot(data=c_occ,aes(x=cuisine_name,y=count))+
  ggtitle("Top 15 cuisines ")+
  geom_bar(stat="identity",width=0.5,aes(fill = count))+
  scale_fill_gradient2(low='snow', mid='blue', high='black')+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
plot



