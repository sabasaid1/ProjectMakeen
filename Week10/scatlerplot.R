df<-mtcars
#
qplot(wt,mpg,data = df)
#
qplot(wt,mpg,data = df,color=cyl)
#
qplot(wt,mpg,data = df,size=cyl)
#
qplot(wt,mpg,data = df,color=cyl,size=cyl)
#show 4 fu
qplot(wt,mpg,data = df,color=hp,size=cyl,alpha=0.6)
#
pl<- ggplot(data=df,aes(x=wt,y=mpg))
pl+geom_point()
#
pl<- ggplot(data=df,aes(x=wt,y=mpg))
pl+geom_point(aes(color=cyl))
