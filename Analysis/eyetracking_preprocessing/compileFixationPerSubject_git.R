# JAN 7, 2021
# CALCULATE FIXATIONS PER TRIAL FOR EACH SUBJECT
# source("~/mydir/compileFixationPerSubject.R")
# library(plyr)
# library(zoo)

compileFixationPerSubject<-function(id, nAOI, plotMissing, plotTrials){
  
  # params
  resx<-1280
  resy<-1024
  samplingRate<-120
  nfaces<-40
  nreps<-2
  fixthresh<-0
  lcent<--320 
  rcent<-320
  fw<-94+5 # face width/2 plus a few pixels
  lfacex<-c(lcent-fw, lcent+fw) # left face x coordinates
  cfacex<-c(-fw, fw) # 94 pixel width on either side
  rfacex<-c(rcent-fw, rcent+fw) # right face x coordinates
  llx<-lfacex[1]:(lcent-1)
  rlx<-(lcent+1):lfacex[2]
  lcx<-cfacex[1]:-1
  rcx<-1:cfacex[2]
  lrx<-rfacex[1]:(rcent-1)
  rrx<-(rcent+1):rfacex[2]
  facey<--fw:fw
  nTrials<-320
  speedThreshold<-7 # pixels/time sample = 7*120 = 840 pixels per second; velocity above this is defined a saccade
  # with screen width of 33.8cm and 1280 pix resolution, 840 pixels = 22.19cm = 22.29 deg/sec at 57cm vd
  accThreshold<-9.15 # in pixels/time sample^2 = 10.46*120^2 = 150725.7 pixels per second squared, with above screen specs
  # i.e., 4000 deg per squared sec
  nfaces<-40
  nreps<-2
  invThresh<-0.1 # missing data per trial should be less than this proportion of the total trial duration
  trialsToPlot<-1:20
  
  # deal with anomalously formatted files
  if(id %in% c(15, 17, 19)){
    dat<-read.csv(paste(id, "_ChimericFace_eye.csv", sep=""))
  } else{
    dat<-read.csv(paste(id, "_ChimericFace_eye.csv", sep=""), sep="")
  }
  
  # isolate the face stimulus epochs
  fdat<-dat[dat$Phase=="faces",]
  
  # Compute proportion of missing samples per trial
  t<-which(fdat$GazePointX<1 | fdat$GazePointX>1280 ) # outside the screen horizontal or missing
  u<-which(fdat$GazePointY<1 | fdat$GazePointY>1024 ) # outside the screen vertical or missing
  fdat$outscreen<-0
  fdat$outscreen[c(t,u)]<-1
  propOutscreenTotal<-round(mean(fdat$outscreen), 2)
  propOutscreenPerTrial<-aggregate(outscreen~TrialNumber, data=fdat, mean)
  whichTrialsOut<-which(propOutscreenPerTrial$outscreen>invThresh)
  numTrialsOut<-length(which(propOutscreenPerTrial$outscreen>invThresh))
  print(paste (id, numTrialsOut))
  
  if(numTrialsOut>160){
    print(paste("id ", id, " removed", sep=""))
    return()
  }
  
  # plot proportion of missing samples per trial
  if(plotMissing==1){
    par(mfrow=c(2,1))
    hist(propOutscreenPerTrial$outscreen, main=id)
    plot(propOutscreenPerTrial$TrialNumber, propOutscreenPerTrial$outscreen, col="black", type="p", 
         cex=0.8, ylim=c(0,1))
    abline(h=invThresh, col="red")
    text(15, 0.9, paste(numTrialsOut, ", ", round(numTrialsOut/320*100), "%", sep=""))
  }

  dat<-dat[!dat$TrialNumber %in% whichTrialsOut,] # remove trials missing more than 10% of sample
  t<-which(dat$GazePointX<1 | dat$GazePointX>1280 ) # re-identify missing sample points because the indices have changed 
  u<-which(dat$GazePointY<1 | dat$GazePointY>1024 ) # 
  dat<-dat[-c(t,u),]# remove those rows from the data
  
  # center the coordinates and create smoothed locations
  dat$GazePointX<-dat$GazePointX-(resx/2) # center the data
  dat$GazePointY<-dat$GazePointY-(resy/2) # center the data
  # smooth coordinates to determine fixations and saccades:
  tmpX<-rollmean(dat$GazePointX, 5) # rolling average of x locations; jb idea
  tmpY<-rollmean(dat$GazePointY, 5) # rolling average of y locations
  dat$smoothX<-c(NA, NA, tmpX,NA, NA) # pad with NAs because length of rollmean is shorter than data
  dat$smoothY<-c(NA, NA, tmpY,NA, NA)
  
  # calculate eye movement speed
  dat$speed<-(sqrt(diff(c(NA, dat$smoothX))^2 + diff(c(NA, dat$smoothY))^2))  # rms of derivative of x and y position; jb
  dat$acc<-diff(c(NA, dat$speed))
  #  dat$acc2<-(sqrt(diff(c(NA, diff(c(NA, dat$smoothX))))^2 + diff(c(NA, diff(c(NA, dat$smoothY))))^2))

  fdat<-dat[dat$Phase=="faces",]
  
  trialChange<-which(diff(c(0,fdat$TrialNumber))>0) # find lines where trial number changes
  # fdat<-fdat[-trialChange,] # remove first rows of each trial where speed is invalid
  fdat<-fdat[-which(is.na(fdat$speed) | is.na(fdat$speed)),]
  
  # detect fixations and saccades
  fdat$saccade<-fdat$speed>speedThreshold # this is a saccade
  t<-which(diff(diff(fdat$saccade))==(-2)) # what is this? ask jb. zh dec 17, 2020; ANS: remove jitter around threshold
  fdat$saccade[t+1]<-FALSE
  t<-which(diff(diff(fdat$saccade))==(2)) # what is this? ask jb. zh dec 17, 2020
  fdat$saccade[t+1]<-TRUE
  startSacc<-diff(c(FALSE, fdat$saccade))==(1)
  fdat$saccNumber<-0
  fdat$saccNumber[startSacc]<-1
  fdat$saccNumber<-cumsum(fdat$saccNumber)
  tmpdat<-ddply(fdat, .(saccNumber), function(saccDat){
    
    tmp<-sum(saccDat$acc[saccDat$saccade==TRUE]>accThreshold)
    saccDat$saccade2<-tmp>0
    tmpdat<-data.frame(saccDat)
  })
  fdat<-tmpdat
  fdat$saccade2[fdat$saccade==FALSE]<-FALSE
  
  ## PLOTTING
  if(plotTrials==1){
    par(xpd=FALSE)
    par(mar=c(5,5,4,4))
    for(k in trialsToPlot){
      par(mfrow=c(3,1))
      ### location plot
      trialIndices<-which(fdat$TrialNumber==k)
      if(length(trialIndices)>0){
        plot(fdat$TimeStamp[trialIndices], fdat$smoothY[trialIndices], type="b",
             main=paste("Trial number ", k, sep=""), ylab="X position", xlab="Time (ms)", ylim=c(-500, 500), 
             col="pink")
        points(fdat$TimeStamp[trialIndices], fdat$smoothX[trialIndices], type="b",
               pch=21, col="black", cex=0.8)
        abline(h=c(lcent, rcent), col="grey", lty=3)
        abline(h=c(lfacex, rfacex), col="grey", lty=2)
        abline(h=cfacex, col="grey")
        points(fdat$TimeStamp[trialIndices[fdat$saccade[trialIndices]==FALSE]], 
               rep(-480,length(which(fdat$saccade[trialIndices]==FALSE))),
               col="red", pch=3)
        
        ### speed plot
      #  trialIndices<-trialChange[k]:(trialChange[k+1]-2)
        plot(fdat$TimeStamp[trialIndices], fdat$speed[trialIndices], type="b",
             main=paste("Speed-defined saccade"), ylab="Speed (pixels/sample)", xlab="Time (ms)", 
             ylim=c(-11, 150))
        abline(h=speedThreshold, col="red")
        points(fdat$TimeStamp[trialIndices[fdat$saccade[trialIndices]==TRUE]], 
               rep(-10, length(which(fdat$saccade[trialIndices]==TRUE))), col="red", pch=3)
        points(fdat$TimeStamp[trialIndices[fdat$dummy[trialIndices]==1]], 
               rep(-10, length(which(fdat$dummy[trialIndices]==1))), col="green", pch=3)
        
        # acceleration
        plot(fdat$TimeStamp[trialIndices], fdat$acc[trialIndices], type="b",
             main=paste("Acceleration-defined saccade"), ylab="Acceleration (pixels/sample^2)", xlab="Time (ms)", 
             ylim=c(-70, 70))
        abline(h=accThreshold, col="red")
        points(fdat$TimeStamp[trialIndices[fdat$saccade2[trialIndices]==TRUE]], 
               rep(-30, length(which(fdat$saccade2[trialIndices]==TRUE))), col="red", pch=3)
        
        
      }
    }
  }
  
  # create fixation dataframe containing each fixation and duration (ffdat)
  startFix<-diff(c(TRUE, fdat$saccade2))==(-1) # find all fixation starts (change from saccade to fixation: saccade = TRUE to saccade = FALSE)
  startTrialWithinFixation<-diff(c(0, fdat$TrialNumber))>0 & fdat$saccade2==FALSE # find start of a trial within a fixation
  fixationStartIndices<-which(startFix | startTrialWithinFixation) # find the points at which a fixation starts or a trial starts during a fixation
  
  # convert time of each sample relative to start of each trial
  fdat<-ddply(fdat, .(TrialNumber), function(tmpdataframe){
    tmpdataframe$TimeStampTrial<-tmpdataframe$TimeStamp-tmpdataframe$TimeStamp[1]
    return(tmpdataframe)
  })

  # assign each fixation a number (across all trials)
  fdat$fixationNumber<-0
  fdat$fixationNumber[fixationStartIndices]<-1
  fdat$fixationNumber<-cumsum(fdat$fixationNumber)
  fdat<-fdat[fdat$saccade2==FALSE,]

  # calculate average location and duration for fixations numbered above
  ffdat<-ddply(fdat, .(fixationNumber), function(fixDat){
    fixX<-round(mean(fixDat$GazePointX))
    fixY<-round(mean(fixDat$GazePointY))
    fixDuration<-(fixDat$TimeStamp[dim(fixDat)[1]]-fixDat$TimeStamp[1]) + 8 # add an extra 8 ms sample
    fixOnset<-fixDat$TimeStampTrial[1]
    return(data.frame(TrialNumber=fixDat$TrialNumber[1], FileID=fixDat$FileID[1], 
                      Intact=fixDat$Intact[1],Hemifield=fixDat$Hemifield[1],
                      fixX, fixY, fixDuration, fixOnset)
                      )
  })
  

  # define function returning measures per trial and AOI; jb wrote this part
  # one row per fixation and AOI; no saccades in this input dataframe
  computeTrialDataframe <- function(trialDat){
 
    nAOIs <- length(aois)
    # aggregate values across fixations in each AOI
    dwellTime<-matrix(data=NA,nAOIs)
    nFixations<-matrix(data=NA,nAOIs)
    fixX = matrix(data=NA,nAOIs)
    fixY = matrix(data=NA,nAOIs)
    fix1X = matrix(data=NA,nAOIs)
    fix1Y = matrix(data=NA,nAOIs)
    firstFixNum<-matrix(data=NA,nAOIs)
    lastFixNum<-matrix(data=NA,nAOIs)
    lastFixX = matrix(data=NA,nAOIs)
    lastFixY = matrix(data=NA,nAOIs)
    
   # print(head(trialDat))
    
    if(nrow(trialDat)==1 || (trialDat$fixDuration[1]>100)){
      # re-number fixations so that first fixation in trial is number 0
      trialDat$fixationNumber <- trialDat$fixationNumber-trialDat$fixationNumber[1] 
    }else{ # if the first fixation is less than 100 ms, we assume that the second fixation is also on the fixation point
      trialDat$fixationNumber <- trialDat$fixationNumber-trialDat$fixationNumber[2] 
    }
  
    # coordinates of fixation 0, assumed to be the target face... (might not be; zh nov 2023)
    fix0X <- trialDat$fixX[trialDat$fixationNumber==0]
    fix0Y <- trialDat$fixY[trialDat$fixationNumber==0]
    
    for(i in 1:nAOIs){
      fixationsInAOI <- trialDat$aoi==aois[i]
      dwellTime[i]<-round(sum(trialDat$fixDuration[fixationsInAOI])) # total dwell time across fixations (per AOI)
      nFixations[i] <- length(which(fixationsInAOI)) # number of fixations per AOI
      
      # average X & Y location (weighted by dwell time for each fixation)
      fixX[i] <- round(sum(trialDat$fixX[fixationsInAOI] * trialDat$fixDuration[fixationsInAOI])/dwellTime[i]) 
      fixY[i] <- round(sum(trialDat$fixY[fixationsInAOI] * trialDat$fixDuration[fixationsInAOI])/dwellTime[i]) 
      
      # added july 2023 to get first saccade number for each AOI (e.g. face) on the screen, after the starting gaze location
      fixationsAfter0 <- fixationsInAOI & trialDat$fixationNumber>0
      firstFixNum[i]<-trialDat$fixationNumber[fixationsAfter0][1]
      
      # coordinates of first fixation in each aoi (after starting point)
      fix1X[i] <- trialDat$fixX[fixationsAfter0][1]
      fix1Y[i] <- trialDat$fixY[fixationsAfter0][1]
      
      # added january 2025 to get last fixation number for each AOI (e.g. face) on the screen
      if( any(fixationsAfter0) ){ #(need to test this because tail return empty rather than NA, which leads to an error if no fixation in this AOI after 0)
        lastFixNum[i]<-tail(trialDat$fixationNumber[fixationsAfter0],n=1)
      
        # coordinates of last fixation to each aoi (after starting point)
        lastFixX[i] <- tail(trialDat$fixX[fixationsAfter0],n=1)
        lastFixY[i] <- tail(trialDat$fixY[fixationsAfter0],n=1)
      }
    }
    
    # count dwells (consecutive fixations in the same AOI) per AOI
    aoiChange = c( 1, trialDat$aoi[2:nrow(trialDat)]!=trialDat$aoi[1:nrow(trialDat)-1])  # 
    trialDat$dwellNumber = cumsum(aoiChange)
    dwellDat <- ddply(trialDat, .(dwellNumber), function(dwellDat){
      aoi = dwellDat$aoi[1]
      return(data.frame(aoi))
    })
    nDwells<-matrix(data=NA,nAOIs)
    for(i in 1:nAOIs){
      nDwells[i] <- length(which(dwellDat$aoi==aois[i]))
    }
    
    return(data.frame(id=rep(id,nAOIs),im=rep(trialDat$Intact[1],nAOIs), faceNumber=rep(trialDat$FileID[1], nAOIs), 
                      hemifield=rep(trialDat$Hemifield[1],nAOIs),
                      aois,dwellTime, nFixations, nDwells, fixX, fixY, firstFixNum, lastFixNum,
                      fix0X=rep(fix0X[1], nAOIs), fix0Y=rep(fix0Y[1], nAOIs), fix1X, fix1Y, lastFixX, lastFixY
                      ))
  }
  
  if(nAOI==6){
    # apply function for 6 AOIs
    ffdat$aoi = "other"
    ffdat$aoi[ffdat$fixX %in% llx & ffdat$fixY %in% facey]<-"ll"
    ffdat$aoi[ffdat$fixX %in% rlx & ffdat$fixY %in% facey]<-"rl"
    ffdat$aoi[ffdat$fixX %in% lcx & ffdat$fixY %in% facey]<-"lc"
    ffdat$aoi[ffdat$fixX %in% rcx & ffdat$fixY %in% facey]<-"rc"
    ffdat$aoi[ffdat$fixX %in% lrx & ffdat$fixY %in% facey]<-"lr"
    ffdat$aoi[ffdat$fixX %in% rrx & ffdat$fixY %in% facey]<-"rr"
    aois<-c("ll", "rl","lc", "rc","lr", "rr")
   
  }else if(nAOI==3){
    # apply function for 3 AOIs
    ffdat$aoi = "other"
    ffdat$aoi[ffdat$fixX >= lfacex[1] & ffdat$fixX <= lfacex[2] & ffdat$fixY %in% facey]<-"left"
    ffdat$aoi[ffdat$fixX >= cfacex[1] & ffdat$fixX <= cfacex[2] & ffdat$fixY %in% facey]<-"center"
    ffdat$aoi[ffdat$fixX >= rfacex[1] & ffdat$fixX <= rfacex[2] & ffdat$fixY %in% facey]<-"right"
    aois<-c("left", "center", "right")
  }
 
  eyeData<-ddply(ffdat, .(TrialNumber), computeTrialDataframe)
  
  return(list("trialSummary"= eyeData, "allSamples"=fdat))
  #return(eyeData)
}

