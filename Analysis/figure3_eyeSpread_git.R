## plot fixation locations for 3 representative subjects per group, fit ellipses to fixation spread
## and show on face images (A); calculate ellipse area for all subjects and show as boxplots. (B)
library(rstudioapi)
library(png)
library(plyr)
library(dplyr)
library(lme4)
library(effects)
library(lmerTest)
library(ellipse)
# rm(list=ls())

## params----
savePDF<-0
doLM<-0 # set to 1 to run models; not used here
faceNumber<-69 # face image on which to superimpose data
colGradients<-50 # plotting param
xvar<-"fixX" # average fixation x position per trial
yvar<-"fixY" # average fixation y position per trial

## load data and other----
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) # set working directory to location of script
eyedat<-read.csv("csv/eyedat_clean.csv") # eye-tracking subjects only; 115 subjects
oval<-read.csv("csv/ovalCoordinates.csv", header=FALSE)
# face images on which to superimpose data
cface<-readPNG(sprintf("PNG/O%02d.PNG", faceNumber))
lface<-readPNG(sprintf("PNG/LL%02d.PNG", faceNumber))
rface<-readPNG(sprintf("PNG/RR%02d.PNG", faceNumber))

## if savePDF----
if(savePDF==1){
  ovalcol<-"white"
  pdf("figures/figure3.pdf", family="Helvetica", 
      width=7.5, height=10)
} else{
  ovalcol<-"grey"
}

# calculate sample size per language group----
ncalc<-aggregate(fixX~id+group, data=eyedat, mean)
n<-table(ncalc$group)

## models (can't recall why i'm doing this here; not used later)----
### model comparison with lm0 (all terms) shows no diff in variance
if(doLM==1){
  lm0.1<-lmer(fixX~angle2+aoi+im+hemifield+
                angle2:aoi+
                aoi:im+
                (1|id), data=eyedat)
  
  efx<-effect("angle2:aoi", lm0.1, xlevels=list(angle2=seq(-1, 1, length.out=colGradients)))
  ef<-data.frame(efx$x)
  ef$xfit<-efx$fit
  ef$xse<-efx$se
  
  lm0y.1<-lmer(fixY~angle2+aoi+im+hemifield+
                 angle2:aoi+
                 (1|id), data=eyedat)
  efy<-effect("angle2:aoi", lm0y.1, xlevels=list(angle2=seq(-1, 1, length.out=colGradients)))
  ef$yfit<-efy$fit
  ef$yse<-efy$se
  ef$cols<-wes_palette("Zissou1", colGradients, type = "continuous")
}

par(mfrow=c(2,3))
#layout(plotmat)


## Plot A: Fixation ellipses  -----
### plotting params----
xlimval<-1.95
ylimval<-1.95
facexlimval<-2.54
xloc<-0
ivs<-c("aoi")
cexlegend<-1.1
ptcex2<-3
faceTransp<-0.3
col1<-"#3B9AB2"
col2<-"goldenrod"
col3<-"#F21A00"
par(mfrow=c(4,3), mar=c(0.5,0.5,0,0), oma=c(2,3,3,1))

### identify a couple subjects from each group----
tmpdat<-aggregate(eyedat$fixX, list(eyedat$id, eyedat$group, eyedat$angle2), mean)
tmpdat[order(tmpdat$Group.3, tmpdat$x),]
#plotids<-c(37, 62, 59, 71, 73, 161, 120, 88, 153) # representative subjects, original ids
plotids<-c("j10", "j33", "j30", "j40", "j42", "j117", "j82", "j54", "j109") # de-identified

### data subset for those subjects---- 
eyedatsubset<-eyedat[eyedat$id %in% plotids,]
eyedatsubset <- eyedatsubset %>%
  group_by(group, id) %>%
  mutate(id2 = cur_group_id()) %>%
  ungroup() %>%
  group_by(group) %>%
  mutate(id2 = paste0("s", dense_rank(id2)))
eyedatsubset<-data.frame(eyedatsubset)

### plot----
plotdat<-ddply(eyedatsubset, .(group, aoi), function(plotdat){
  
  if(plotdat$aoi[1]=="1. left"){
    face<-lface
    caption<-"Left face"
  } else if (plotdat$aoi[1]=="2. center"){
    face<-cface
    caption<-"Target face"
  } else{
    face<-rface
    caption<-"Right face"
  }

  plot(c(1,2), c(-2, -1), pch=19, col="white", xlab="", 
       xaxt="none", yaxt="none", ylab="", axes=F, asp=1,
       xlim=c(-xlimval, xlimval), ylim=c(-ylimval,ylimval))
  
  rasterImage(1-faceTransp+face*faceTransp,
              xleft=-facexlimval, xright=facexlimval,
              ybottom=-facexlimval, ytop=facexlimval)
  par(xpd=FALSE)
  lines(c(facexlimval, -facexlimval), c(0,0), lty=3, col="darkslategrey")
  lines(c(0,0), c(facexlimval, -facexlimval), lty=3, col="darkslategrey")
  text(-1, -0.05, "1", col="darkslategrey")
  text(1, -0.05, "1", col="darkslategrey")
  text(0, -2, "2", col="darkslategrey")
  text(0, 2, "2", col="darkslategrey")
  if(unique(plotdat$group)=="1. English"){
    mtext(caption, side=3, line=0.5, cex=1.3)
    }

  plotdat2<-ddply(plotdat, .(id2), function(plotdat2){
    
    if(unique(plotdat2$id2)=="s1"){
      thispch<-16
    } else if(unique((plotdat2$id2)=="s2")){
      thispch<-8
    } else{
      thispch<-3
    }
    points(plotdat2$fixX, plotdat2$fixY, pch=thispch, col=scales::alpha(plotdat2$col,0.2), cex=0.9)
    cov_matrix <- cov(cbind(plotdat2$fixX, plotdat2$fixY))
    ellipse_coords <- data.frame(ellipse::ellipse(cov_matrix, centre = c(mean(plotdat2$fixX), mean(plotdat2$fixY)), 
                                      level = 0.90))
    lines(ellipse_coords$x, ellipse_coords$y,col=scales::alpha(plotdat2$col,1),lwd=1)

  })
})

## Plot B----
### calculate ellipse area for all subjects and save----
chi_sq_val <- qchisq(0.95, df = 2)

ellipse_areas <- eyedat %>%
  group_by(id, aoi) %>%
  summarise(
    n = n(),
    meanX = mean(fixX, na.rm = TRUE),
    meanY = mean(fixY, na.rm = TRUE),
    cov_matrix = list(cov(cbind(fixX, fixY), use = "complete.obs"))
  ) %>%
  rowwise() %>%
  mutate(
    ellipse_area = pi * sqrt(det(cov_matrix)) * sqrt(chi_sq_val)
  ) %>%
  ungroup() %>%
  select(id, aoi, ellipse_area) %>%
  left_join(
    eyedat %>%
      select(id, aoi, group, angle2) %>%
      distinct(),
    by = c("id", "aoi")
  )

el<-data.frame(ellipse_areas)
el$group2 <- factor(el$group, levels = rev(levels(factor(el$group))))

### boxplots----
plotdat<-dlply(el, .(aoi), function(plotdat){
  
  if(unique(plotdat$aoi)=="1. left"){
    par(mar=c(2,4,1,1))
  } else if(unique(plotdat$aoi)=="2. center"){
    par(mar=c(2, 3, 1, 2))
  } else{
    par(mar=c(2, 3, 1, 2))
  }

  yticks<-c(0.2,0.5, 1, 2, 4)
  boxplot(plotdat$ellipse_area~plotdat$group, 
          col=c(scales::alpha(col1,0.7),  scales::alpha(col2, 0.7),  scales::alpha(col3, 0.7)),
          ann=FALSE, axes=FALSE, ylim=c(0.15, max(yticks)), log="y", staplewex=0.3, notch=FALSE)
  axis(side=2, at=yticks, cex.axis=1.2)
  if(unique(plotdat$aoi)=="1. left"){
    mtext(side=2, line=2.5, expression("Ellipse Area (deg"^2*")"))
    axis(side=1, at=c(1,2,3), labels=c("English", "Bi", "Arabic"), cex.axis=1.4)
  }
  
})

## if savePDF----
if(savePDF==1){
  dev.off()
}