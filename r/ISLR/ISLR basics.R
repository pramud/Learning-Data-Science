install.packages("ISLR")
library(ISLR)
fix(Auto)
plot(Auto$cylinders,Auto$mpg)
attach(Auto)
plot(cylinders,mpg)
#If the variable plotted on the x-axis is categorial, then boxplots will
#automatically be produced by the plot() function. As usual, a number of options can be speci???ed in order to customize the plots
cylinders =as.factor(cylinders )
plot(cylinders , mpg , col="red")
plot(cylinders , mpg , col="red", varwidth =T)
#The hist() function can be used to plot a histogram
hist(mpg)
summary(mpg)
names(Auto)
pairs(Auto)

