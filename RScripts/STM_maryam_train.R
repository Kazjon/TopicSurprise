library(stm)
path <- "d:/pique/"
topics <- 50
lower_thresh <- 298
upper_thresh <- 149012
args <- paste(lower_thresh,upper_thresh,sep="_")
load(paste(path,args,"_preprocessed.RData",sep=""))
model <- stm(corpus$documents,corpus$vocab,K=topics)
save(model, file=paste(path,args,"model.RData",sep=""), row.names=F)
theta <- as.data.frame(model$theta)
write.csv(theta, file=paste(path,"theta.csv",sep=""), row.names=F)
corrs <- as.data.frame(cor(model$theta))
write.csv(corrs, file=paste(path,"corrs.csv",sep=""), row.names=F)
finaldata <- cbind(corpus$meta, theta)
write.csv(finaldata, file=paste(path,"outputdata.csv",sep=""), row.names=F)