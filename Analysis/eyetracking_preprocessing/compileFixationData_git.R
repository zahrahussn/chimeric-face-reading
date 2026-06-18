## wrapper around compileFixationPerSubject (line 16) to write eye data per subject to a csv file 

library(plyr)
library(zoo)
#library(reshape2)
rm(list=ls()) 
graphics.off()
setwd("~/yourdir/etc") 
eyeFiles<-list.files(path="~/yourdir/eyeTrackingDataFiles", 
                     pattern="*_ChimericFace_eye.csv", full.names=T, recursive=FALSE)

naoi<-3
plotMissing<-0
plotTrials<-0

source("~/yourdir/compileFixationPerSubject_git.R")

eyeData<-lapply(eyeFiles, function(getfile) {
  
  id<-substr(basename(getfile), 1, nchar(basename(getfile))-21) # get subject initials
  eyeData<-compileFixationPerSubject_git(id,naoi, plotMissing,plotTrials)
  eyeData<-eyeData$trialSummary
    
  })
eyedat<-as.data.frame(do.call(rbind, eyeData))

names(eyedat)[names(eyedat)=="aois"]<-"aoi"
if(naoi==3){
  eyedat$aoi<-revalue(eyedat$aoi, c("left"="1. left", "center"="2. center", "right"="3. right"))  
}

# write.csv(eyedat, "alleyedat_3aoi.csv")
# wide to long: 
# eyedatlong<-reshape2::melt(eyedat, id.vars=c("id", "TrialNumber", "im", "hemifield"), variable.name="aoi", value.name="dwellTime")
