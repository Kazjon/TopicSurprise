library(stm)
path <- "/media/kazjon/Storage/pique/books/"
lower_thresh <- 0.0001
upper_thresh <- 0.9
data <- read.table(paste(path,"amazonBooks_desc_quoted.csv", sep=""),sep=",",header=FALSE,col.names=c("id","title","abstract"),quote="~", strip.white=TRUE)
lower_thresh <- as.integer(lower_thresh * length(data$id))
upper_thresh <- as.integer(upper_thresh * length(data$id))
args <- paste(lower_thresh,upper_thresh,sep="_")
print(args)
custom_stopwords <- c(t(paste(path,"customstopwords.txt", sep="")))
processed <- textProcessor(paste(data$title,data$abstract, sep=" "), metadata=data, customstopwords = custom_stopwords)
corpus <- prepDocuments(processed$documents, processed$vocab, processed$meta,lower.thresh = lower_thresh, upper.thresh = upper_thresh)
save(corpus,file=paste(path,args,"_preprocessed.RData",sep=""))
