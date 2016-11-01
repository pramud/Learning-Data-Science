result <- read.csv("~/GitHub/Scraping-Zomato/src/result.csv", encoding = "UTF-8")
View(result)
summary(result$Upcoming.)
result$Upcoming. <- NULL
View(result)
summary(result$Promotions.)
result$Promotions. <- NULL
View(result)
result$Special. <- NULL
result$Today. <- NULL
View(result)
result$Freebie. <- NULL
result$Discount. <- NULL
result$Featured.in. <- NULL
View(result)
result$page <- NULL

