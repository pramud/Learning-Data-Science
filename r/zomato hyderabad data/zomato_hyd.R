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
result$costForTwo <- sapply(gsub("(\u20b9)","",result$Cost.for.two.), function(x) x[1])
View(result)
result$costForTwo <- sapply(gsub(",","",result$costForTwo), function(x) x[1])
View(result)
c <- ggplot(result, aes(factor(place)))
c + geom_bar() + coord_flip()
result$p =strsplit(as.character(result$place), ',')
result$cleanedPlace <- sapply(strsplit(as.character(result$place), ", "), function(x) ifelse(match(x[[1]][2],NA),x[[1]][1],x[[1]][2]))
result$cleanedPlace <- sapply(strsplit(as.character(result$place), ", "), function(x) print(x[[1]]))
# have to change this

