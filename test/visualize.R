library(data.table)
require (reshape)
require (ggplot2)
library(dplyr)
library(tidyr)


kmer_count_0.0001 <- read.csv("test/data/kmer_count_0.0001.csv")
kmer_count_0.001 <- read.csv("test/data/kmer_count_0.001.csv")
kmer_count_0.1 <- read.csv("test/data/kmer_count_0.1.csv")
kmer_count_0.005 <- read.csv("test/data/kmer_count_0.005.csv")
kmer_count_0.05 <- read.csv("test/data/kmer_count_0.05.csv")
kmer_count_ALL <- read.csv("test/data/kmer_countALL.csv")

dataList <- list(kmer_count_ALL, kmer_count_0.0001, kmer_count_0.001,kmer_count_0.005,kmer_count_0.05, kmer_count_0.1)
myMerge <- function(df1, df2){                                
  merge(df1, df2, by = "kmer")
}

data <- Reduce(myMerge, dataList)                                   
colnames(data)=c('kmer', 'ALL', '0.0001', '0.001', '.005', '0.05', '0.1')
write.csv(data,"test/data.csv", row.names = FALSE)


data=data[data$ALL>1,]
lista <- list()
for (i in sort(unique(data$ALL))) {
  temp=data[data$ALL==i,-c(1, 2)]
  tempPositive=data.frame(temp==i)
  accuracy = colMeans(tempPositive)
  id=paste('kmer', i)
  lista[[id]] <- accuracy
}
df=data.frame(lista)
summary(df)
plot(df)

dft <- transpose(df)
colnames(dft)=c('0.0001', '0.001', '0.005', '0.05', '0.1')
dft$kmer=sort(unique(data$ALL))
dft <- dft %>% gather(prob, acc, 1:5)

e <- ggplot(dft, aes(x =prob , y = acc))
e +  geom_boxplot()+
geom_jitter(aes(color = factor(kmer)), size=3, alpha=0.7)

