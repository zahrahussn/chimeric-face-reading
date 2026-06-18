# figure 2: behavioural data and models; uses biasdat, langdat

library(rstudioapi)
library(lmerTest)
library(effects)
library(effectsize)
library(MuMIn) # r.squared
library(car)
library(plyr)

# library(extrafont)
# loadfonts()
# library(wesanderson)
# library(scales) # alpha
# library(tidyr)
# library(BurStMisc)
# library(tidyverse) # do this or langdat gets messed up

setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) # set working directory to location of script
# rm(list=ls())
#source("loadData_git.R")
biasdat<-read.csv("csv/biasdat_clean.csv")
langdat<-read.csv("csv/langdat_clean.csv")

runModels<-1 # set to 0 to tinker with figures once models are run
aggregateModel<-1 # aggregate or trialwise model; aggregate reported
savePDF<-0 # set to 1 to save PDF in figures folder
removeLowLang<-0 # set this to 0 for figure 2A and 1 for models
xmin<--1
xmax<-1
rad<-0.75
lowLangScoreN<-length(langdat$radius[langdat$radius<0.75])
if(removeLowLang==1){
  biasdat<-biasdat[biasdat$radius > rad,]
  langdat<-langdat[langdat$radius > rad,]
}


### OPEN PDF-----
if(savePDF==1){
  pdf("figures/figure2.pdf",
      family="Helvetica",
      width=10, height=10)
}

### MODELS-----
if(runModels==1){

  #### Model 1, Figure 2B------
  # simple linear regression of mean bias on language score 
  tmpdat<-aggregate(correct~id+group+angle2+radius+cols+col1+pch, mean, 
                    data=biasdat[biasdat$radius>rad,])
  tmpdat$pll<-tmpdat$correct
  lm1<-lm(pll~angle2, data=tmpdat)
  test1<-cor.test(tmpdat$pll, tmpdat$angle2)
  
  print("STAT 1: FIG 2B")
  print(t.test(tmpdat$pll,mu=0.5))
  
  print("STAT 2: FIG 2B")
  print(cor.test(tmpdat$pll, tmpdat$angle2))
  
  ### Model 2, Figure 2C----
  if(aggregateModel==1){
    tmpdat2<-aggregate(correct~id+group+angle2+radius+cols+col1+pch+im+hemifield, mean, 
                       data=biasdat[biasdat$radius>rad,])
    lm2.0<-lmer(correct~angle2*im*hemifield+(1|id), data=tmpdat2)
    anovalm2.0<-anova(lm2.0)
    effectsize(anovalm2.0, partial=TRUE)
    r.squaredGLMM(lm2.0)
    ef<-effect("angle2:im:hemifield", lm2.0,xlevels=list(angle2=seq(xmin, xmax, length.out=3)))
    efdat<-data.frame(ef)
    
    print("STAT 3: FIG 2C")
    print(Anova(lm2.0, type="III"))
    
    
  } else{
    ## logit model 
    lm2<-glmer(correct~angle2*im*hemifield+(1|id)+(1|face),
               data=biasdat, family="binomial",
               control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=10000)))
    
    print("STAT 3: FIG 2C")
    print(Anova(lm2, type="III"))
    ef<-effect("angle2:im:hemifield", lm2, 
               xlevels=list(angle2=seq(xmin, xmax, length.out=3)))
    efdat<-data.frame(ef)
  }
  
}

ylab<-expression("Left-side bias (" * p[LL] * ")")
cols<-c("white", "white")
c1<-35
c2<-55
textcex<-1.6
mtextcex<-1.3
figurelabelcex<-1.6
cexaxis<-1.8
cexlabels<-1.8
cexlegend<-1.6
ptcex1<-1.9
ptcex2<-2.6
ptcex3<-1.7
ptbox<-1.4
colalpha<-0.4
xlocs<-c(-1, 0, 1) # c(c1/2, 45, c2+c1/2)

#par(mfrow=c(1,3))
mylayout <- matrix(c(1, 2, 3, 3),nrow = 2,byrow = TRUE)
layout(mylayout, heights = c(1, 1), widths = c(1, 1))

### 2A LANGUAGE GROUPS SCATTERPLOT----
par(xpd=FALSE)
par(mar=c(4.5,4.5,4,2.5))
plot(langdat$engComp, langdat$arabicComp, pch=19, col="white", 
     cex.axis=cexaxis, cex.lab=cexlabels,
     xlab="", ylab="", frame.plot = FALSE, xlim=c(0, 1), ylim=c(0, 1))
mtext(side=1, line=3, "English score", cex=mtextcex)
mtext(side=2, line=3, "Arabic score", cex=mtextcex)
mtext(side=3, line=2, 'A', adj=-0.1, cex=figurelabelcex)
theta<-seq(0, pi, length.out=20)
x<-rad*cos(theta)
y<-rad*sin(theta)
lines(x,y, lty=3, col="darkslategrey")
lines(c(0, 1.2*cos(c1*pi/180)),c(0,1.2*sin(c1*pi/180)), lty=3, col="#3B9AB2", lwd=1.5)
lines(c(0, 1.2*cos(c2*pi/180)),c(0,1.2*sin(c2*pi/180)), lty=3, col="#F21A00", lwd=1.5)

points(langdat$engComp, langdat$arabicComp, pch=langdat$pch,
       col=langdat$col1, bg=scales::alpha(langdat$cols, 0.7), 
       cex=ptcex1)
text(0.85,0.05, length(unique(biasdat$id[biasdat$group=="1. English"])), 
     col="#3B9AB2", cex=textcex)
text(0.05,0.95, length(unique(biasdat$id[biasdat$group=="3. Arabic"])), 
     col=scales::alpha("#F21A00",0.7), cex=textcex)
par(xpd=TRUE)
text(1.07,1.05, length(unique(biasdat$id[biasdat$group=="2. Bilingual"])), 
     col="darkgoldenrod", cex=textcex)
text(0.4,0.05, lowLangScoreN, col=rgb(0.4,0.4,0.4), cex=textcex)

### 2B BEHAVIOUR - CONTINUOUS----
ymin<-0.2
ymax<-0.8

par(xpd=FALSE)
plot(tmpdat$angle2, tmpdat$pll, xlab="", ylab="", 
     pch=19, col="white", xlim=c(-1.05,1.05), ylim=c(ymin, ymax), 
     cex=cexaxis, frame.plot = FALSE, 
     axes="F")
axis(side=1, at=xlocs, labels=xlocs, 
     cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
axis(side=2, at=c(0.2, 0.3, 0.4, 0.5,0.6, 0.7, 0.8), 
     cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
mtext(side=1, line=3, "Language score", cex=mtextcex)
mtext(side=2, line=3, ylab, cex=mtextcex)
mtext(side=3, line=2, 'B', adj=-0.1, cex=figurelabelcex)
points(tmpdat$angle, tmpdat$pll, pch=tmpdat$pch, col=tmpdat$col1, 
       bg=scales::alpha(tmpdat$cols, 0.7), cex=ptcex1)

abline(lm1, col=rgb(0.4,0.4,0.4))
abline(h=0.5, lty=3, col=rgb(0,0,0))
text(-0.87, 1.02*ymin, "English", col="#3B9AB2", cex=textcex)
text(0, 1.02*ymin, "Bidirectional", col="darkgoldenrod", cex=textcex)
text(0.9, 1.02*ymin, "Arabic", col="#F21A00", cex=textcex)

par(xpd=TRUE)
text(0.5, 1.05*ymax, paste("r = ", round(test1$estimate,2), 
                           ", p = ", round(test1$p.value,4), sep="" ), cex=textcex)
par(xpd=FALSE)
## 2C-D BEHAVIOUR DISCRETE, USING SINGLE TRIALS-----
par(mar=c(4.5,16,5.5,16))
col1<-"#3B9AB2"
col2<-"goldenrod"
col3<-"#F21A00"
lvfpolycol<-scales::alpha("thistle2", 0.35)
rvfpolycol<-scales::alpha("gray82",0.35)
lvfptcol<-scales::alpha("thistle3", 0.9)
rvfptcol<-scales::alpha("gray70", 0.9)

ymin<-0.35
ymax<-0.65

for(i in 1:1){
  fig<-ifelse(i==1, 'C', 'D')
  
  par(xpd=FALSE)
  #  xlocs<-c(1,2,3)
  plot(xlocs, c(0.5, 0.5, 0.5),  col="white", 
       xlab="", ylab="",
       xaxt="none", 
       xlim=c(1.05*xmin, 1.05*xmax), ylim=c(ymin,ymax), 
       cex.axis=cexaxis, 
       cex.lab=cexlabels, axes="F",
       #box(bty='L'),
       main="")
  axis(side=1, at=xlocs, labels=c(-1, 0, 1), 
       cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
  axis(side=2,
       at = c(0.35, 0.5,0.65),
       cex.axis=cexaxis, lwd=1, tick="TRUE", lwd.ticks=1)
  mtext(side=2, ylab, line=2.95, cex=mtextcex)
  mtext(side=1, line=3, "Language score", cex=mtextcex)
  mtext(side=3, line=2, fig, adj=-0.1, cex=figurelabelcex)
  abline(h=0.5, lty=3, col="darkslategrey")
  text(-0.87, 1.02*ymin, "English", col="#3B9AB2", cex=textcex)
  text(0, 1.02*ymin, "Bidirectional", col="darkgoldenrod", cex=textcex)
  text(0.9, 1.02*ymin, "Arabic", col="#F21A00", cex=textcex)
  par(xpd=TRUE)
  if(i==1){
    legend(1.1*xmax, 1.4*ymin, title="", pch=c(15,15), 
           col=c(scales::alpha(lvfpolycol, 0.9), scales::alpha(rvfpolycol,0.9)),
           c("LL left of target", "LL right of target"),
           bty="n", yjust=1, title.adj=0.1, #adj=0, 
           pt.cex=2.75, cex=cexlegend)
    
    legend(1.1*xmax, ymax, pch=c(3,4,21),
           c("Original target", "Mirror-reversed", "Mean"),
           bty="n", horiz=FALSE, xjust=0, title.adj=0.1,
           yjust=1, pt.cex=c(1.6,1.6, 2.7),
           col=c("black", "black", "darkslategrey"),
           pt.bg=c("black", "black", "grey"),
           cex=cexlegend)
  }
  
  #### fit-------
  par(xpd=FALSE)
  plotdat<-ddply(efdat, .(im, hemifield), function(plotdat){
    
    if(unique(plotdat$hemifield)[1]=="RVF"){
      polycol<-rvfpolycol
    }else{
      polycol<-lvfpolycol}
    
    polygon(c(plotdat$angle2, rev(plotdat$angle2)),
            c(plotdat$fit+plotdat$se,
              rev(plotdat$fit-plotdat$se)), 
            col=polycol,
            border=NA)
  })
  # 
  
  #### grand mean------
  alphaval<-1
  meanangle<-tapply(biasdat$angle2, biasdat$group, mean)
  meanprop<-tapply(biasdat$correct, biasdat$group, mean)
  seprop<-tapply(biasdat$correct, biasdat$group, sd)/sqrt(table(biasdat$group)/4)
  plotrix::plotCI(meanangle, meanprop, ui=meanprop+seprop, li=meanprop-seprop, add=TRUE, 
                  col="white",
                  scol=c(scales::alpha(col1, 0.7), scales::alpha(col2, 0.7), scales::alpha(col3, 0.7)), sfrac=0.002)
  points(meanangle, meanprop, pch=21, cex=ptcex2, col=c(col1, col2, col3), 
         bg=c(scales::alpha(col1,alphaval), 
              scales::alpha(col2,alphaval), scales::alpha(col3, alphaval)), lwd=2)
  
  #### points-----
  plotdat<-ddply(biasdat, .(im, hemifield), function(plotdat){
    
    ptpch<-ifelse(unique(plotdat$im)[1]=="Intact", 3 , 4 )
    ptcol<-ifelse(unique(plotdat$hemifield)[1]=="RVF", rvfptcol,lvfptcol)
    
    meanangle<-tapply(plotdat$angle2, plotdat$group, mean)
    meanprop<-tapply(plotdat$correct, plotdat$group, mean)
    seprop<-tapply(plotdat$correct, plotdat$group, sd)/sqrt(table(plotdat$group))
    points(meanangle, meanprop, pch=ptpch, cex=ptcex3, col=ptcol, lwd=2) 
    
  })
  
}

### CLOSE PDF-----
if(savePDF==1){
  dev.off()
}

