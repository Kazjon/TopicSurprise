library(stm)
path <- "d:/pique/"
topics <- 50
lower_thresh <- 29
upper_thresh <- 149012
args <- paste(lower_thresh,upper_thresh,sep="_")
load(paste(path,args,"_preprocessed.RData",sep=""))
docbows <- as.data.frame(corpus$documents)
write.csv(docbows, file=paste(path,args,"_docbows.csv",sep=""),row.names=F)
vocab <- as.data.frame(corpus$vocab)
write.csv(vocab, file=paste(path,args,"_vocab.csv",sep=""),row.names=F)
model <- stm(corpus$documents,corpus$vocab,K=topics)
save(model, file=paste(path,args,"_model.RData",sep=""), row.names=F)
theta <- as.data.frame(model$theta)
write.csv(theta, file=paste(path,args,"_theta.csv",sep=""), row.names=F)
corrs <- as.data.frame(cor(model$theta))
write.csv(corrs, file=paste(path,args,"_corrs.csv",sep=""), row.names=F)
finaldata <- cbind(corpus$meta, theta)
write.csv(finaldata, file=paste(path,args,"_combined.csv",sep=""), row.names=F)
