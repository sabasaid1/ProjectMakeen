#dataset import from kaggle

library(readr)
marksheet <- read_csv("E:/Downloads/archive (7)/marksheet.csv")
View(marksheet)

library(xlsx)
install.packages("xlsx", dependencies = TRUE)
library(rio)


export(marksheet,'marksheet.csv')
export(marksheet,'marksheet.xlsx')

######
#create a matrix of 5 student score in three subject
#create student score using function
#make sure the number you get are integer without decimal point 
# math phys Bio Total Percent

#ALi
#Bader
#saif
#Total
#save the result in exel sheet


cells <- c(1,26,24,68,50,80,70,60,50)
rnames <- c('ALi','Bader','saif')
cname <- c('math','phys','Bio')
mymatrix <- matrix(cells,nrow = 3,ncol = 3,byrow = TRUE, dimnames = list(rnames,cname))
mymatrix

Total = c(sum(cells))
price=c(144,553)
df3 <- cbind(mymatrix, Total)
df3


#Ali
ali=rnorm(3,45,4)
#Bader
bader=rnorm(3,66,3)
#Saif
saif=rnorm(3,80,9)

#submatrix
submatrix=rbind(ali,bader,saif)
submatrix
colnames(submatrix) <- c('math','phys','Bio')
submatrix
#total cbind create new colume
submatrix = cbind(submatrix, 'Total'=rowSums(submatrix))
submatrix
#percent 
submatrix = cbind(submatrix, 'Percent'=submatrix[,4]/300)
submatrix
#total rbind new row 
submatrix = rbind(submatrix, 'Total'= colSums(submatrix))
submatrix
#convert matrix to dataframe
df=data.frame(submatrix)
df

#save the result in exel sheet
export(df,'submatrix.xlsx')









