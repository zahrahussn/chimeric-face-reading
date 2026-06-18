## gaze-behaviour associations; trial-level analyses

library(rstudioapi)
library(plyr)
library(dplyr)
library(lme4)
library(car)
library(effects)
library(lmerTest)
library(gplots)
library(MuMIn) #(conditional R-squared for fixed and random effects variance)
#rm(list=ls())

setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) # set working directory to location of script

doModels<-1
savePDF<-0
doBins<-0
numBins<-10
numQuantiles<-10
eyedat<-read.csv("csv/eyedat_clean.csv")
eyedat$dwellTime<-eyedat$dwellTime/1000
ymin<-0.1
ymax<-0.9

### if savePDF==1----
if(savePDF==1){
  ovalcol<-"white"

  pdf("figures/figure5.pdf", family="Helvetica", 
      width=9, height=4)
} 

### if doModels==1----
if(doModels==1){
  #### 1. X location on target face, fixX------
  tar<-eyedat[eyedat$aoi=="2. center",]
  nontar<-eyedat[eyedat$aoi!="2. center",]
  tar$faceNumber<-revalue(tar$faceNumber, c("O1"="O01", "O4"="O04", "O8"="O08" ))
  tar$fixX<-round(tar$fixX, 2)
  
  # single trial analyses
  # nFixations doesn't improve the model fit and adds weirdness; jan 2025
  # nFixations removed from model: anova confirms no significant contribution; august 2025
  
  lm.target<-glmer(correct~angle2*fixX+(1|id), data=tar, family="binomial",
                   control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=10000)))
  print("bias~fixX")
  print(Anova(lm.target, type='III'))
  
  # for main effect of fixation
  efx.target<-effect("fixX", lm.target,
                     xlevels=list(fixX=round(seq(-2,2, length.out=9),2)))
  
  # for nonsignificant language x fixation interaction, shown at extremes of x
  efall.target<-effect("angle2:fixX", lm.target,
                       xlevels=list(angle2=round(seq(-1,1, length.out=3),3), 
                                    fixX=round(seq(-2,2, length.out=2),2)))
  
  efx.target<-data.frame(efx.target)
  efalldat.target<-data.frame(efall.target)

  ### 2. nFixation LL-RR -----
  xmin<--1
  xmax<-1
  summin<--1
  summax<-1
  
  xmin<--2
  xmax<-2
  summin<--1
  summax<-1
  
  # single-trial calculations
  nfixdiff <- eyedat %>%
    filter(nFixations < 11) %>%
    filter(face %in% c("1. LL", "3. RR")) %>%
    group_by(id, TrialNumber) %>%
    filter(n_distinct(face) == 2) %>%
    summarise(
      nfix_LL = first(nFixations[face == "1. LL"], default = NA),    
      nfix_RR = first(nFixations[face == "3. RR"], default = NA),   
      nfixdiff = nfix_LL - nfix_RR,
      nfixsum = nfix_LL + nfix_RR,
      id = first(id[face == "1. LL"], default = NA),
      im = first(im[face == "1. LL"], default = NA), 
      firstfix = first(firstFixNum[face == "1. LL"], default = NA),
      trial = first(TrialNumber[face == "1. LL"], default = NA),
      angle2 = first(angle2[face == "1. LL"], default = NA),                        
      correct = first(correct[face == "1. LL"], default = NA),
      group = first(group[face == "1. LL"], default = NA)
    ) %>%
    ungroup()
  nfixdiff<-as.data.frame(nfixdiff)
  # Scale nfixsum and store as a vector; unscaled causes model not to converge
  nfixdiff$nfixsumscaled <- as.vector(scale(nfixdiff$nfixsum))
  
  # is the difference in n fixations on LL v. RR related to language score? no; august 2025
  # lm.nfix.1<-lmer(nfixdiff~angle2*im+(1|id), data=nfixdiff)
  
  lm.nfix<-glmer(correct~nfixdiff*nfixsumscaled*angle2+(1|id), data=nfixdiff, 
                 family="binomial",
                 control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=10000)))
  ef.nfixdiffangle<-effect("nfixdiff:angle2", lm.nfix,
                           xlevels=list(nfixdiff=seq(xmin,xmax, length.out=10),
                                        angle2=seq(-1, 1, length.out=3)))
  efnfixdiffangle<-data.frame(ef.nfixdiffangle)
  print("bias~nfixdiff")
  print(Anova(lm.nfix, type='III'))

  
   ### 3. first & last fixations------
  
  df <- nontar %>%
    group_by(id, TrialNumber) %>%
    mutate(
      firstfixyn = as.integer(firstFixNum == min(firstFixNum)),
      lastfixyn  = as.integer(lastFixNum == max(lastFixNum))
    ) %>%
    ungroup()
  df<-data.frame(df)
  df<-df[df$face=="1. LL",]
  
  lm.saccade<-glmer(correct~angle2*firstfixyn*lastfixyn+(1|id), data=df, family="binomial",
                    control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=10000)))
  # print(Anova(lm1, type='III'))
  ef3.lm1<-effect("firstfixyn:lastfixyn", lm.saccade,
                  xlevels=list(firstfixyn=seq(0,1, length.out=2),
                               lastfixyn=seq(0, 1, length.out=2)))
  ef1.lm1<-effect("angle2:firstfixyn", lm.saccade,
                  xlevels=list(firstfixyn=seq(0,1, length.out=2),
                               angle2=seq(-1, 1, length.out=10)))
  ef2.lm1<-effect("angle2:lastfixyn", lm.saccade,
                  xlevels=list(lastfixyn=seq(0,1, length.out=2),
                               angle2=seq(-1, 1, length.out=10)))
  efall.lm1<-effect("angle2:firstfixyn:lastfixyn", lm.saccade,
                    xlevels=list(firstfixyn=seq(0,1, length.out=2),
                                 lastfixyn=seq(0,1, length.out=2),
                                 angle2=seq(-1, 1, length.out=3)))
  ef1lm1<-data.frame(ef1.lm1)
  ef2lm1<-data.frame(ef2.lm1)
  ef3lm1<-data.frame(ef3.lm1)
  efallm1<-data.frame(efall.lm1)

}

### PLOTTING PARAMETERS ------
col1<-"#3B9AB2"
col2<-"goldenrod"
col3<-"#F21A00"
cextext<-1.3
cextext2<-1.3
ptalpha<-0.8
cexaxis<-1.4
cexaxislabel<-1.1
cexlegend<-1.4
cexlegendpoint<-2
ptcex<-2.2
ptcex2<-3
cexfigurelabel<-1.4
par(mfrow=c(1,3))

### PLOT 1: behav vs. gaze on target ------
ylab<-expression("Left-side bias (" * p[LL] * ")")
par(mar=c(5, 5, 4, 3))
par(xpd=FALSE)
plot(unique(efx.target$fixX), rep(0.5, length.out=9), pch=19, col="white", axes=FALSE,
     xlab="", ylab="", ylim=c(ymin, ymax), xlim=c(-2.25, 2.25)) 
axis(side=1, at=c(-2, -1, 0, 1, 2), cex.axis=cexaxis)
mtext(side=1, line=3, expression("Fixation x position"[target] * "(deg)"), cex=cexaxislabel)
axis(side=2, at=c(0.1, 0.3, 0.5, 0.7, 0.9), cex.axis=cexaxis, las=2)
mtext(side=2, line=3, ylab, cex=cexaxislabel)
#mtext(side=3, line=2, "Target face", cex=cexaxlab)
mtext(side=3, line=2, 'A', adj=-0.05, cex=cexfigurelabel)
lines(c(0, 0), c(0, 0.9), lty=3)
abline(h=0.5, lty=3)

polygon(c(efx.target$fixX, rev(efx.target$fixX)),
          c(efx.target$fit+efx.target$se, rev(efx.target$fit-efx.target$se)), 
        col=scales::alpha("darkgrey", 0.5), border=NA)

if(doBins==0){
 # numQuantiles <- 12
  tar$fixX<-round(tar$fixX,2)
  breaks <- quantile(tar$fixX, probs = seq(0, 1, length.out = numQuantiles + 1), 
                     na.rm = TRUE, type = 7)
  tar <- tar %>%
   mutate(fixXQ = ntile(fixX, numQuantiles))
  #plot(tar$fixXQ, tar$fixX)
  xMean<-tapply(tar$fixX, tar$fixXQ, mean)
  corrMean<-tapply(tar$correct, tar$fixXQ, mean)
  points(xMean, corrMean, pch=19, col="grey50", cex=1.2)
} else{
  #numBins<-7
  tar <- tar %>%
    mutate(fixX_bin = cut(fixX, breaks = numBins, labels = FALSE)) 
  xMean<-tapply(tar$fixX, tar$fixX_bin, mean)
  corrMean<-tapply(tar$correct, tar$fixX_bin, mean)
  points(xMean, corrMean, pch=19, col="grey50", cex=1.2)
}



plotdat<-dlply(efalldat.target, .(angle2), function(plotdat){
    
    if(unique(plotdat$angle2)==-1){
      thiscol<-col1
      xadj<-0
      } else if(unique(plotdat$angle2)==0){
        thiscol=col2
        xadj<-0
        } else{
          thiscol<-col3
          xadj<--0
        }
    
     plotCI(plotdat$fixX+xadj, plotdat$fit, ui=plotdat$fit+plotdat$se, 
            li=plotdat$fit-plotdat$se, 
            col="white", scol=scales::alpha(thiscol,ptalpha),  sfrac=0, add=TRUE)  
     points(plotdat$fixX+xadj, plotdat$fit, col=thiscol, bg=scales::alpha(thiscol,ptalpha),  
            pch=21, cex=ptcex)
      
})


  ### PLOT 2 - nFix difference x language -----
  par(mar=c(5, 4, 4, 3))
   plot(unique(efnfixdiffangle$nfixdiff), rep(0.5, length.out=10), pch=19, col="white", axes=FALSE,
        xlab="", ylab="", ylim=c(ymin, ymax), xlim=c(xmin-0.05, xmax+0.05)) 
     axis(side=1, at=c(xmin, -1, 0,1, xmax), cex.axis=cexaxis)
     mtext(side=1, line=3, expression("Difference in n. fixations"["LL-RR"]), cex=cexaxislabel)
    # mtext(side=3, line=2, "Choice faces (LL vs. RR)", cex=cexaxlab)
     mtext(side=3, line=2, 'B', adj=-0.3, cex=cexfigurelabel)
     abline(h=0.5, lty=3)
     lines(c(0, 0), c(0, 0.9), lty=3)
     par(xpd=TRUE)
     legend(-2, 1.1, pch=c(21, 21, 21),
            col=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)),
            pt.bg=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)),
            pt.cex=cexlegendpoint, cex=cexlegend, bty="n",
            c("English", "Bidirectional", "Arabic"), title="")

     
     plotdat<-dlply(efnfixdiffangle, .(angle2), function(plotdat){
       
       if(unique(plotdat$angle2)==-1){
         thiscol<-"#3B9AB2"
         xadj<-0.05
       } else if(unique(plotdat$angle2)==0){
         thiscol="darkgoldenrod"
         xadj<-0.0
       } else{
         thiscol<-"#F21A00"
         xadj<--0.05
       }

       polygon(c(plotdat$nfixdiff, rev(plotdat$nfixdiff)),
               c(plotdat$fit+plotdat$se, rev(plotdat$fit-plotdat$se)), col=scales::alpha(thiscol, 0.4),
               border=NA)
       
       points(plotdat$nfixdiff[c(1,10)]+xadj, 
              plotdat$fit[c(1,10)], col=thiscol, bg=scales::alpha(thiscol,0.7),  pch=21, cex=2)
       
     }) # plotdat
     
     plotdat<-dlply(nfixdiff, .(group), function(plotdat){
       
       if(unique(plotdat$group)=="1. English"){
         thiscol<-"#3B9AB2"
         xadj<-0.05
       } else if(unique(plotdat$group)=="2. Bilingual"){
         thiscol="darkgoldenrod"
         xadj<-0.0
       } else{
         thiscol<-"#F21A00"
         xadj<--0.05
       }
       
       numQuantiles<-5 # the magic number
       breaks <- quantile(plotdat$nfixdiff, 
                          probs = seq(0, 1, length.out = numQuantiles + 1), na.rm = TRUE, type = 7)
       plotdat <- plotdat %>%
         mutate(nfixdiffQ = ntile(nfixdiff, numQuantiles))
       #plot(tar$fixXQ, tar$fixX)
       meanx<-tapply(plotdat$nfixdiff, plotdat$nfixdiffQ, mean)
       # print(meanx)
       # plot(plotdat$nfixdiffQ, plotdat$nfixdiff)
       meany<-tapply(plotdat$correct, plotdat$nfixdiffQ, mean)
       points(meanx, meany, pch=19, col=thiscol, cex=1.2)
       
     })
     
     ### PLOT 3: 1st vs. last fixation on LL and RR faces -------
    
    # main effects of first and last fixation, and nonsig interaction, and angle
     par(mar=c(5, 4, 4, 3))
     par(xpd=FALSE)
     plot(c(0,1), ef3lm1$fit[2:1], pch=21, cex=ptcex, xlim=c(-0.1, 1.1), ylim=c(0.1, 0.9),
          axes=FALSE, xlab="", ylab="", type='b', col="black", bg="grey", lty=2)
     points(c(0,1), ef3lm1$fit[4:3], pch=21, cex=ptcex, type='b')
     axis(side=1, at=c(0, 1), labels=c("LL", "RR"), cex.axis=cexaxis)
     mtext(side=1, line=3, "First saccade", cex=cexaxislabel)
     mtext(side=3, line=2, 'C', adj=-0.05, cex=cexfigurelabel)
    # mtext(side=3, line=2, "Fixation order (LL vs. RR)", cex=cexaxlab)
     abline(h=0.5, lty=3)
     par(xpd=TRUE)
     legend(0.8, 1.1, pch=c(21, 21),
            col=c(scales::alpha("black", ptalpha), scales::alpha("black", ptalpha)),
            pt.bg=c(scales::alpha("white", ptalpha), scales::alpha("grey", ptalpha)),
            pt.cex=cexlegendpoint, cex=cexlegend, bty="n",
            c("LL", "RR"), 
            title="Last saccade")
     
     plotCI(c(0,1), ef3lm1$fit[2:1], ui=ef3lm1$upper[2:1], 
             li=ef3lm1$lower[2:1], add=TRUE, sfrac=0, pch=21, pt.bg="grey", scol="black", cex=ptcex)
     plotCI(c(0,1), ef3lm1$fit[4:3], ui=ef3lm1$upper[4:3], 
            li=ef3lm1$lower[4:3], add=TRUE, sfrac=0, pch=21, pt.bg="white", scol="black", cex=ptcex)
     
     plotdat<-dlply(efallm1, .(angle2), function(plotdat){
       
       if(unique(plotdat$angle2)==-1){
         thiscol<-col1
         xadj<-0.07
       } else if(unique(plotdat$angle2)==0){
         thiscol<-col2
         xadj<-0.07
       } else{
         thiscol<-col3
         xadj<-0.07
       }
       
       plotCI(c(0+xadj, 1+xadj), plotdat$fit[2:1], ui=plotdat$fit[2:1]+plotdat$se[2:1], 
              li=plotdat$fit[2:1]-plotdat$se[2:1], 
              scol=scales::alpha(thiscol, 0.5), 
              pch=19, col="white", sfrac=0, add=TRUE)
       
       plotCI(c(0+xadj, 1+xadj), plotdat$fit[4:3], ui=plotdat$fit[4:3]+plotdat$se[4:3], 
              li=plotdat$fit[4:3]-plotdat$se[4:3], 
              scol=scales::alpha(thiscol,0.5), 
              pch=19, col="white", sfrac=0, add=TRUE)
       
       points(c(0+xadj, 1+xadj), plotdat$fit[2:1], pch=21, 
              col=thiscol, bg=scales::alpha(thiscol, 0.5), cex=1.8)
       points(c(0+xadj, 1+xadj), plotdat$fit[4:3], pch=21, 
              col=thiscol, bg=scales::alpha(thiscol, 0.6), cex=1.8)
       
       
     })
     
if(savePDF==1){
  dev.off()
  }     
     

