#Day 1 coding
X<- 'r'
class(X)
X=c('r','t')
x1=c(3,5,45)
c(TRUE,FALSE)->x2
##
temps <- c(72,71,68,73,69,75,71,90)
temps
?name

names(temps)=c('Su','Mo','Tu','We','Th','Fr','Sa')
temps

#between 3 and 6 or use temps[c(3:6)]
temps[3:6]

#Multiply by 4
new_temp = c(temps*4)
  
#Add 10

#min(),max(),mean(),median

min(temps)
max(temps)
mean(temps)
median(temps)

#sum()
sum(temps)
#Logical
temps[temps>71]

temps[temps>71 | temps<70]
#create varible include 70
temp70=temps[temps>69 & temps<80]
#create varible not  include < 70
tempNo70 =temps[temps<70 | temps>80]

temps['We']


mean(temps)

temp_day=temps[c('We','Sa')]
mean(temp_day)
#
temp01 = temps[names(temps)%in% c('We','Sa')]

temp01
temp02 = temps[!names(temps)%in% c('We','Sa')]

temp02
#vector


##what is two to the power of five?
2^4



##1create vactor called stock.price with following data point 23,27,23,21,34??

stockprice <- c(23,27,23,21,34)

##2
names(stockprice)=c('Mon','Tues','Wed','Thu','Fri')
stockprice

#3what was the averge(mean) for the week?
mean(stockprice)

#4create vatcor called over23 consisting of logicicte 

stockprice>23
#5
stockprice[stockprice>23]


stockprice[stockprice==max(stockprice)] #name and value

max(stockprice) #value

names(stockprice[stockprice==max(stockprice)]) #only name

#####Matrices
y <- matrix(1:20,nrow = 5,ncol = 4)
y
cells <- c(1,26,24,68)
rnames <- c('R1','R2')
cname <- c('c1','c2')
mymatrix <- matrix(cells,nrow = 2,ncol = 2,byrow = FALSE, dimnames = list(rnames,cname))
mymatrix
colnames(mymatrix) <- cname
colnames
#multipy cells 4
cells*4

mymatrix * mymatrix
cells1 <- c(1,26,24,68,22,50)
rnames1 <- c('R1','R2')
cname1 <- c('c1','c2','c3')
mymatrix2 <- matrix(cells1,nrow = 2,ncol = 3,byrow = TRUE, dimnames = list(rnames1,cname1))
mymatrix2

cells2 <- c(1,26,24,68,22,50)
rnames2 <- c('R1','R2','R3')
cname2 <- c('c1','c2')
mymatrix3 <- matrix(cells1,nrow = 3,ncol = 2,byrow = TRUE, dimnames = list(rnames2,cname2))
mymatrix3
#multiply two matrix
mymatrix2%*%mymatrix3

mymatrix
#find first colume
mymatrix[,1]
#find second row
mymatrix[2,]

##H.W
#generate list of  random number using :
#runif 30 
#rnorm 30

r_runif=runif(30)
r_rnorm=rnorm(30)
plot(r_runif)
plot(r_rnorm)
