library(stm)
path <- "d:/pique/"
lower_thresh <- 0.0001
upper_thresh <- 0.5
data <- read.csv(paste(path,"finalACMData.csv", sep=""))
lower_thresh <- as.integer(lower_thresh * length(data$Abstract))
upper_thresh <- as.integer(upper_thresh * length(data$Abstract))
args <- paste(lower_thresh,upper_thresh,sep="_")
print(args)
custom_stopwords <- c(t(paste(path,"d:/pique/customstopwords.txt", sep="")))
processed <- textProcessor(data$Abstract, metadata=data, customstopwords = custom_stopwords)
corpus <- prepDocuments(processed$documents, processed$vocab, processed$meta,lower.thresh = lower_thresh, upper.thresh = upper_thresh)
save(corpus,file=paste(path,args,"_preprocessed.RData",sep=""))
