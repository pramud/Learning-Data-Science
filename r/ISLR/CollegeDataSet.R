library(ISLR)
summary(College)
names(College)
fix(College)
attach(College)
rownames(College)
College [,1] 
pairs(College)

Elite=rep("No",nrow(College )) 
Elite[College$Top10perc >50]=" Yes" 
