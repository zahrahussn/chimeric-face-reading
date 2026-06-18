## gaze bias measures for 115 eyetracking subjects; uses eyedat

library(rstudioapi)
library(png)
library(plyr)
library(dplyr)
library(lme4)
library(effects)
library(lmerTest)
library(scales)
library(effectsize)
library(MuMIn) # r.squared
#rm(list=ls())

## params----
loadStuff<-1
savePDF<-0
doLM<-1
doFig2<-0

#### IF LOAD STUFF ==1------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) # set working directory to location of script
if(loadStuff==1){
  faceNumber<-69
  eyedat<-read.csv("csv/eyedat_clean.csv")
  oval<-read.csv("csv/ovalCoordinates.csv",
                 header=FALSE)
  # face images on which to superimpose data
  cface<-readPNG(sprintf("PNG/O%02d.PNG", faceNumber))
  lface<-readPNG(sprintf("PNG/LL%02d.PNG", faceNumber))
  rface<-readPNG(sprintf("PNG/RR%02d.PNG", faceNumber))
  
  xvar<-"fixX"
  yvar<-"fixY"
  
}

#### IF SAVE PDF ==1------
if(savePDF==1){
  ovalcol<-"white"
  pdf("figures/figure4.pdf", family="Helvetica", 
      width=9, height=6)
} else{
  ovalcol<-"grey"
}

#### IF DO MODELS ==1--------
nLangLevels<-20
if(doLM==1){
  ###### 1. FIG 3B X coordinates-----
  ### aggregate models 
  ## previous model comparisons justify dropping im and hemifield from these analyses
  tmpdat<-aggregate(fixX~id+angle2+aoi, data=eyedat, mean)
  lmx.0<-lmer(fixX~angle2*aoi+(1|id), data=tmpdat)
  print("x-coordinates")
  print(anova(lmx.0))
  print(effectsize(anova(lmx.0), partial=TRUE))
  r.squaredGLMM(lmx.0)
  efx<-effect("angle2:aoi", lmx.0, xlevels=list(angle2=seq(-1, 1, length.out=nLangLevels)))
  efx<-data.frame(efx)
  #Anova(lmx)
  
  #### 2. FIG 3C Y coordinates-----
  tmpdat<-aggregate(fixY~id+angle2+aoi, data=eyedat, mean)
  lmy.0<-lmer(fixY~angle2*aoi+(1|id), data=tmpdat)
  print("y-coordinates")
  print(anova(lmy.0))
  print(effectsize(anova(lmy.0), partial=TRUE))
  r.squaredGLMM(lmy.0)
  efy<-effect("angle2:aoi", lmy.0, xlevels=list(angle2=seq(-1, 1, length.out=nLangLevels)))
  efy<-data.frame(efy)
  
  #### 3. FIG 3D First fixation-----
  tmpdat<-aggregate(firstFixNum~id+angle2+aoi, data=eyedat[eyedat$aoi !="2. center",], mean)
  lmff.0<-lmer(firstFixNum~angle2*aoi+(1|id), data=tmpdat)
  print("first fix")
  print(anova(lmff.0))
  print(effectsize(anova(lmff.0), partial=TRUE))
  ef1<-effect("angle2:aoi", lmff.0, xlevels=list(angle2=seq(-1,1, length.out=10)))
  efff<-data.frame(ef1)
  r.squaredGLMM(lmff.0)
  
  #### 4. FIG 3E N fixations-----
  tmpdat<-aggregate(nFixations~id+angle2+aoi, data=eyedat[eyedat$aoi !="2. center",], mean)
  lmnfix.0<-lmer(nFixations~angle2*aoi+(1|id), data=tmpdat)
  print("n. fixations")
  print(anova(lmnfix.0))
  print(effectsize(anova(lmnfix.0), partial=TRUE))
  efnfix<-effect("angle2:aoi", lmnfix.0, xlevels=list(angle2=seq(-1,1, length.out=10)))
  nfixeffect<-data.frame(efnfix)
  r.squaredGLMM(lmnfix.0)
}

### PLOTTING PARAMETERS ------
col1<-"#3B9AB2"
col2<-"goldenrod"
col3<-"#F21A00"
centerpolycol<-scales::alpha("grey",0.4)
lvfpolycol<-centerpolycol
rvfpolycol<-centerpolycol
faceTransp<-0.4 # contrast
cextext<-1.3
cextext2<-1.3
ptalpha<-0.8
cexaxis<-1.4
cexaxislabel<-1.2
cexlegend<-1.4
cexlegendpoint<-2
ptcex<-2.2
ptcex2<-3
cexfigurelabel<-1.4
plotmat<-rbind(c(1,1,1,1, 2,2,2,2, 3,3,3,3),
               c(4,4,4,5,5,5,6,6,6,7,7,7))
layout(plotmat)

## FIGURES----
##### 3A: Gaze on faces -----
xlimval<-1.95 # axis range
ylimval<-1.95
facexlimval<-2.54 # face range is bigger than axis range to zoom
xloc<-0
ivs<-c("aoi")
ncalc<-aggregate(fixX~id+group, data=eyedat, mean)
n<-table(ncalc$group)

plotdat<-ddply(eyedat, .(aoi), function(plotdat){
  if(plotdat$aoi[1]=="1. left"){
    face<-lface
    caption<-"Left face"
    thispch<-24
    par(mar=c(2,4,4,2))
  } else if (plotdat$aoi[1]=="2. center"){
    face<-cface
    caption<-"Target face"
    thispch<-21
    par(mar=c(2,3,4,3))
  } else{
    face<-rface
    caption<-"Right face"
    thispch<-25
    par(mar=c(2,2,4,4))
  }
  
  plot(c(1,2), c(-2, -1), pch=19, col="white", xlab="", 
       xaxt="none", yaxt="none", ylab="", axes=F, asp=1,
       xlim=c(-xlimval, xlimval), ylim=c(-ylimval,ylimval))
  polygon(oval$V1, oval$V2, col="white",border=ovalcol)
  rasterImage(1-faceTransp+face*faceTransp,
              xleft=-facexlimval, xright=facexlimval,
              ybottom=-facexlimval, ytop=facexlimval)
  lines(range(oval$V1), c(0,0), lty=3, col="darkslategrey")
  lines(c(0,0), range(oval$V2), lty=3, col="darkslategrey")
  par(xpd=FALSE)
  mtext(caption, side=3, line=1, cex=cextext)
  text(-1, -0.05, "1", col="darkslategrey")
  text(1, -0.05, "1", col="darkslategrey")
  text(0, -2, "2", col="darkslategrey")
  text(0, 2, "2", col="darkslategrey")
  if(plotdat$aoi[1]=="1. left"){
    par(xpd=TRUE)
    mtext(side=3, line=2, 'A', adj=-0.05, cex=cexfigurelabel)
    legend(1.60*-xlimval, 1.25*ylimval, pch=c(21,21,21),
           col=c(col1, col2, col3), 
           pt.bg= c(col1, col2, col3),
           c("English", "Bidirectional", "Arabic"),
           adj=0, bg="snow1", box.col="lightgrey",
           #  y.intersp = 1.1,
           pt.cex=cexlegendpoint, cex=cexlegend)
    par(xpd=FALSE)
  }
  
  xdat<-aggregate(get(xvar)~id+group, data=plotdat, mean)
  ydat<-aggregate(get(yvar)~id+group, data=plotdat, mean)
  xdat$fixY<-ydat[[3]]
  names(xdat)<-c("id","group", "fixX", "fixY")
  
  xmean<-tapply(xdat$fixX, xdat$group, mean)
  xse<-tapply(xdat$fixX,  xdat$group, sd)/sqrt(n)
  ymean<-tapply(xdat$fixY, xdat$group, mean)
  yse<-tapply(xdat$fixY,  xdat$group, sd)/sqrt(n)
  
  plotrix::plotCI(xmean, y=ymean, ui=xmean+xse, li=xmean-xse, pch=thispch, col="white",
                  scol=c(col1, col2, col3), err="x",
                  sfrac=0, add=TRUE, lwd=1.5)
  plotrix::plotCI(xmean, ymean, ui=ymean+yse, li=ymean-yse,pch=thispch, col="white",
                  scol=c(col1, col2, col3), err="y",
                  sfrac=0, add=TRUE, lwd=1.5)
  points(xmean, ymean, pch=thispch, col=c(col1, col2, col3), 
         bg=c(col1, col2, col3),
         cex=1.7, lwd=1)
})


##### 3B: X coordinate - language x roi interaction effects plot-----
par(mar=c(4,4,3,2))
par(xpd=FALSE)
plot(c(-1,1), c(-1, 1), xlab="", ylab="", axes=FALSE, col="white")
abline(h=0, lty=2)
axis(side=1, at=c(-1,0,1), cex.axis=cexaxis)
axis(side=2, at=c(-1,0,1), cex.axis=cexaxis, las=2)
mtext(side=2,  "X position (deg)", line=2.5, cex=cexaxislabel)
mtext(side=1,  "Language score", line=2.5, cex=cexaxislabel)
par(xpd=TRUE)
text(-0.7, -0.96, "English", col=col1, cex=cextext2)
text(0, -0.96, "Bi", col=col2, cex=cextext2)
text(0.7, -0.96, "Arabic", col=col3, cex=cextext2)
legend(-1, 1.7, title="", pch=c(24,21,25),
       col=c(col1, col1, col1), pt.bg=c(col1, col1 ,col1),
       c("Left face","Target face","Right face"),
       bty="n", adj=0,
       y.intersp = 1.1,
       pt.cex=cexlegendpoint, cex=cexlegend)
mtext(side=3, line=1.3, 'B', adj=-0.2, cex=cexfigurelabel)
par(xpd=FALSE)

plotdat<-ddply(efx, .(aoi), function(plotdat){
  
  if(plotdat$aoi[1]=="1. left"){
    thispch<-24
    thiscol<-lvfpolycol
  } else if(plotdat$aoi[1]=="2. center"){
    thispch<-21
    thiscol<-centerpolycol}
  else{
    thispch<-25
    thiscol<-rvfpolycol
  }
  
  polygon(c(plotdat$angle2, rev(plotdat$angle2)), 
          c(plotdat$fit+plotdat$se, rev(plotdat$fit-plotdat$se)), col=thiscol, 
          border=NA)
  
  tmpdat<-eyedat[eyedat$aoi==unique(plotdat$aoi),]
  meanangle<-tapply(tmpdat$angle2, tmpdat$group, mean)
  meandata<-tapply(tmpdat[[xvar]], tmpdat$group, mean)
  sedata<-tapply(tmpdat[[xvar]], tmpdat$group, sd)/sqrt(n)
  plotrix::plotCI(meanangle, meandata, ui=meandata+sedata, li=meandata-sedata, col="white",
                  scol=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)), cex=0.1,
                  sfrac=0, add=TRUE)
  points(meanangle, meandata, col=c(col1, col2, col3), 
         pch = thispch,
         bg = c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)), 
         cex=ptcex, lwd=1)
  
})

##### 3C: Y coordinate - language x roi interaction effects plot-----
#par(mar=c(4,4,2,2))
par(mar=c(4,3,3,3))
par(xpd=FALSE)
plot(c(-1,1), c(-1, 1), xlab="", ylab="", axes=FALSE, col="white")
abline(h=0, lty=2)
axis(side=1, at=c(-1,0,1), labels=c(-1,0,1), cex.axis=cexaxis)
axis(side=2, at=c(-1,0,1), labels=c(-1,0,1), cex.axis=cexaxis, las=2)
mtext(side=2,  "Y position (deg)", line=2.5, cex=cexaxislabel)
mtext(side=3, line=1.3, 'C', adj=-0.2, cex=cexfigurelabel)

plotdat<-ddply(efy, .(aoi), function(plotdat){
  
  if(plotdat$aoi[1]=="1. left"){
    thispch<-24
    thiscol<-lvfpolycol
  } else if(plotdat$aoi[1]=="2. center"){
    thispch<-21
    thiscol<-centerpolycol}
  else{
    thispch<-25
    thiscol<-rvfpolycol
  }
  
  polygon(c(plotdat$angle2, rev(plotdat$angle2)), 
          c(plotdat$fit+plotdat$se, rev(plotdat$fit-plotdat$se)), col=thiscol, 
          border=NA)
  
})
plotdat<-ddply(eyedat, .(aoi), function(plotdat){
  if(plotdat$aoi[1]=="1. left"){
    thispch<-24
  } else if(plotdat$aoi[1]=="2. center"){
    thispch<-21}
  else{
    thispch<-25
  }
  
  meanangle<-tapply(plotdat$angle2, plotdat$group, mean)
  meandata<-tapply(plotdat[[yvar]], plotdat$group, mean)
  sedata<-tapply(plotdat[[yvar]], plotdat$group, sd)/sqrt(n)
  plotrix::plotCI(meanangle, meandata, ui=meandata+sedata, li=meandata-sedata, col="white",
                  scol=c(col1, col2, col3), cex=0.1,
                  sfrac=0, add=TRUE)
  points(meanangle, meandata, col=c(col1, col2, col3), pch=thispch,
         bg=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)), cex=ptcex, lwd=1)
})

##### 3D: firstFixNum ------
par(mar=c(4,3,3,3))
plot(efff$angle2, efff$fit, xlim=c(-1,1), ylim=c(1,3), axes=FALSE, pch=19,
     col="white",
     xlab="", ylab="")
axis(side=1, at=seq(-1,1, length.out=3), cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
axis(side=2, at=c(1, 2,3), cex.axis=cexaxis, las=2)
mtext(side=2, "First saccade number", line=2.5,cex=cexaxislabel)
mtext(side=3, line=1.3, 'D', adj=-0.2, cex=cexfigurelabel)

plotdat<-ddply(efff, .(aoi), function(plotdat){
  
  fitcol<-ifelse(unique(plotdat$aoi)=="1. left", lvfpolycol,rvfpolycol)
  polygon(c(plotdat$angle2, rev(plotdat$angle)),
          c(plotdat$fit+plotdat$se, rev(plotdat$fit-plotdat$se)), col=fitcol,
          border=NA)
})
plotdat<-ddply(efff, .(aoi), function(plotdat){
  thispch<-ifelse(unique(plotdat$aoi)=="1. left", 24, 25)
  
  tmpdat2<-aggregate(firstFixNum~id+group+angle2, data=eyedat[eyedat$aoi==plotdat$aoi[1],], mean)
  names(tmpdat2)<-c("id","group", "angle2", "firstFixNum")
  n<-table(tmpdat2$group)
  meanangle<-tapply(tmpdat2$angle2, tmpdat2$group, mean)
  sac1mean<-tapply(tmpdat2$firstFixNum, tmpdat2$group, mean)
  sac1se<-tapply(tmpdat2$firstFixNum, tmpdat2$group, sd)/sqrt(n)
  
  plotrix::plotCI(meanangle, sac1mean, ui=sac1mean+sac1se, li=sac1mean-sac1se,
                  add=TRUE, col="white",
                  scol=c(col1, col2, col3), sfrac=0.002)
  points(meanangle, sac1mean, pch=thispch, cex=ptcex,
         col= c(col1, col2, col3),
         bg=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)), lwd=1)
  
})


##### 3E: N fixations-----
par(mar=c(4,2,3,4))
plot(nfixeffect$angle2, nfixeffect$fit, axes=FALSE, pch=19,
     col="white", xlab="", ylab="", ylim=c(1,3))
axis(side=2, at=c(1,2,3), cex.axis=cexaxis, las=2)
mtext(side=2, "Number of fixations", line=2.5,cex=cexaxislabel)
axis(side=1, at=seq(-1,1, length.out=3), cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
mtext(side=3, line=1.3, 'E', adj=-0.2, cex=cexfigurelabel)
par(xpd=FALSE)
plotdat<-ddply(nfixeffect, .(aoi), function(plotdat){
  thiscol<-ifelse(unique(plotdat$aoi)=="1. left", lvfpolycol, rvfpolycol)
  polygon(c(plotdat$angle2, rev(plotdat$angle2)),
          c(plotdat$fit+plotdat$se, rev(plotdat$fit-plotdat$se)), col=thiscol,
          border=NA)
})

plotdat2<-ddply(nfixeffect, .(aoi), function(plotdat2){
  thispch<-ifelse(unique(plotdat2$aoi)=="1. left", 24, 25)
  tmpdat2<-aggregate(nFixations~id+group+angle2,
                     data=eyedat[eyedat$aoi==plotdat2$aoi[1],],mean)
  names(tmpdat2)<-c("id","group", "angle2", "nfix")
  n<-table(tmpdat2$group)
  meanangle<-tapply(tmpdat2$angle2, tmpdat2$group, mean)
  meanfix<-with(tmpdat2, tapply(nfix, group, mean))
  sefix<-with(tmpdat2, tapply(nfix, group, sd))/sqrt(n)
  plotrix::plotCI(meanangle, meanfix, ui=meanfix+sefix, li=meanfix-sefix, add=TRUE,
                  col="white", scol=c(col1, col2, col3), pch=thispch,
                  sfrac=0.002)
  points(meanangle, meanfix, pch=thispch, cex=ptcex, 
         col=c(col1, col2, col3),
         bg=c(scales::alpha(col1, ptalpha), scales::alpha(col2, ptalpha), scales::alpha(col3, ptalpha)), lwd=1)
})


if(savePDF==1){
  dev.off()
}

