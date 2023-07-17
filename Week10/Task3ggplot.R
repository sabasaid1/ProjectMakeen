#import gplot
library(ggplot2)
varnorm = as.integer(rnorm(200,4,3))
varunif = as.integer(runif(200,1,7))
Count = rnorm(200,10,5)

df = data.frame(varnorm,varunif,Count)

#
str(df)
summary(df)
#pass a colum straight into hist()

hist(varnorm)

#usin gplot ,lots of abilty to cutomize, but bit  more compliited

ggplot(data=df,aes(varnorm))+geom_histogram()

#clustring qplot
qplot(data=df,x=varnorm,geom= 'histogram' ,xlim = c(0,15),col='red')

#
qplot(varnorm,data=df,geom= 'histogram' ,alpha=0.2,fill=I('green'))

#ggplot(data,aesthetics)
p1 <- ggplot(df,aes(x=varnorm))
#Add histogram Geometry
p1 + geom_histogram()
#adding color 
p1 + geom_histogram(binwidth = 1,color='red',fill='pink')
#adding labele
p1 <- ggplot(df,aes(x=varnorm))
p1 + geom_histogram(binwidth = 1,color='red',fill='pink') + xlab("Normal Distrbution") + ylab("Occurences") + 
  ggtitle('histogram of Normal Distrbution ')


#change alpha (Transparency)
p1 <- ggplot(df,aes(x=varnorm))
p1 + geom_histogram(binwidth = 1,color='red',fill="blue",alpha=0.6) + xlab("Normal Distrbution") + ylab("Occurences") + 
  ggtitle('histogram of Normal Distrbution ')

#line types

p1 <- ggplot(df,aes(x=varnorm))
p1 + geom_histogram(binwidth = 1,color='red',fill="blue",alpha=0.4,linetype="dotted") + xlab("Normal Distrbution") + ylab("Occurences") + 
  ggtitle('histogram of Normal Distrbution ')

#Advanceed  
p1 <- ggplot(df,aes(x=varnorm))
p1 + geom_histogram(binwidth = 0.5,aes(fill=factor(varnorm))) + xlab("Normal Distrbution") + ylab("Occurences") + 
  ggtitle('histogram of Normal Distrbution ')


