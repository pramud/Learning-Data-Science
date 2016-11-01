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
result$cleanedVotes <- sapply(strsplit(as.character(result$votes), " "), function(x) x[1])
View(result)
summary(result$cleanedVotes)
result$cleanedVotes <- as.numeric(result$cleanedVotes)
summary(result$cleanedVotes)
result$cleanedNoOfRevs <- sapply(strsplit(as.character(result$noOfReviews), " "), function(x) x[1])
View(result)
summary(result$cleanedNoOfRevs)
result$cleanedNoOfRevs <- as.numeric(result$cleanedNoOfRevs)

