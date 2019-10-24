install.packages("ISLR")
library(MASS)
install.packages("DAAG")
library(DAAG)
library(nlme)
library(ISLR)
View(mtcars)

lmodel<-cv.lm(data = Auto, mpg ~ cylinders + displacement + horsepower + weight + acceleration + year + origin, m=2, dots = FALSE, seed = 29, plotit = TRUE, printit = TRUE)
lmodel<-cv.lm(data = Auto, mpg ~ cylinders + displacement + horsepower + weight + acceleration + year + origin, m=3, dots = FALSE, seed = 29, plotit = TRUE, printit = TRUE)
lmodel<-cv.lm(data = Auto, mpg ~ cylinders + displacement + horsepower + weight + acceleration + year + origin, m=8, dots = FALSE, seed = 29, plotit = TRUE, printit = TRUE)

cv.error.10 = rep (0,10)
set.seed(17)

for(i in 2:10)
{
  lmodel <- cv.lm(data =  Auto, mpg ~ cylinders + displacement + horsepower
                  + weight + acceleration + year + origin, m = i , dots =
                    + FALSE, seed=29, plotit=TRUE, printit=TRUE)
  lmodel
  cv.error.10[i]=attr(lmodel,"ms")
}

j<-1
for (j in 1:10)
{
  # printing MS error for each value of K print(cv.error.10[j])
}
X=c(1,2,3,4,5,6,7,8,9,10)
Y=cv.error.10

plot(X,Y, type='l', xlab = "value of K" , ylab = "mean Square error", main = "with change in
value of K there is change in Mean Square Error")
