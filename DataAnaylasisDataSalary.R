#import the dataset
library(readr)
Salary_Data <- read_csv("C:/Users/user/Desktop/Project/codeAcdmey/Salary_Data.csv")
View(Salary_Data)

#summay of Data
summary(Salary_Data)

str(Salary_Data)
#number of varible 6
#number observation

#boxplot(data1$`Years of Experience`,data1$Salary,col=c("red","blue"),horizontal = TRUE)
boxplot(data1$`Years of Experience`,col="red",horizontal = TRUE,main ="Years of Experience")
boxplot(data1$Salary,col="pink",horizontal = TRUE,main="Salary")
boxplot(data1$`Years of Experience`~ data1$Gender,col="pink",horizontal = TRUE)
boxplot(data1$Salary ~ data1$Gender,col="pink",horizontal = TRUE)
#split the screen
#par(mfrow=c(2,2))


#fitting liner model for Experience and Salary 


#
data2$Experience= data2$`Years of Experience`

attach(data2)
View(data2)
plot(data2$Experience,data2$Salary)
cor(data2$Experience,data2$Salary,use = "complete.obs")

model01=lm(data2$Experience~data2$Salary)

newdata <- na.omit(data2)
cor(newdata$Experience,newdata$Salary,use = "complete.obs")
model01=lm(newdata$Experience~newdata$Salary)
abline(model01)

table(newdata$Gender)
#split Male and Female
#create Male sub dataset
DMale=newdata[newdata$Gender=='Male',]
#create Female sub dataset
DFemale=newdata[newdata$Gender=='Female',]

cor(newdata$Experience,newdata$Gender=='Male',use = "complete.obs")
cor(newdata$Gender=='Male',newdata$Gender=='Female',use = "complete.obs")
cor(newdata$Experience,newdata$Gender=='Female',use = "complete.obs")
plot(newdata$Experience,newdata$Gender=='Male')
plot(newdata$Experience,newdata$Gender=='Female')
#barChart
#change color backgound
par(bg="lightpink")

barplot(table(newdata$Gender),col = rainbow(3))
barplot(table(newdata$`Education Level`),col = rainbow(6))


