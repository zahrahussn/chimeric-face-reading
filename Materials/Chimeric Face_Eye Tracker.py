
from __future__ import absolute_import, division, print_function
from psychopy import visual, event, core, gui, data, sound
from psychopy.tools.filetools import fromFile, toFile
from psychopy.visual import ShapeStim
from random import shuffle
import string, time
import random, copy, scipy, pygame, numpy
import os, shutil

from constants import *
import pygaze
import constants
from pygaze import libscreen
from pygaze import liblog
from pygaze import libinput
from pygaze import eyetracker
from pygaze import libtime
from pygaze.display import Display
from pygaze.eyetracker import EyeTracker

variable=''
params = {'ID number':'1', 'lang':'ar',
	 'frameRate':60,'duration':0.3, 'ISI1': 0.2, 'ISI2': 0.5,'fp': 1,'task':'ChimericFace'}

dlg = gui.DlgFromDict(params, title='ChimericFace', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params) #save params to file for next time
else:
    core.quit()#the user hit cancel so exit

fileName = '../data/ChimericFace/'+params['ID number']+'_ChimericFace'
#if os.path.exists(fileName+'.txt')
#    ii=1
#    while True:
#    new_name = fileName + "_" + str(ii) + '.txt'
#    if not os.path.exists(new_name):
#       fileName = new_name
#       break 
#    ii += 1

dataFile = open(fileName+'.csv', 'a') #a simple text file with 'comma-separated-values'
dataFile.write('trial num, face, IM, LLlocation, response, responseField, RT\n') 

disp = Display()

win = pygaze.expdisplay

# Create a visual window:
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=(7.53,7.52))
mask=visual.RadialStim(win, tex='sqrXsqr',color=1, size=4,
    visibleWedge=[0, 360], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False) 

facePath='Final Face Stimuli/'
imageO = [os.path.join(facePath +'O1'),os.path.join(facePath +'O4'),os.path.join(facePath +'O8'),os.path.join(facePath +'O10'),os.path.join(facePath +'O11'),os.path.join(facePath +'O19'),
    os.path.join(facePath +'O20'),os.path.join(facePath +'O22'),os.path.join(facePath +'O28'),os.path.join(facePath +'O31'),os.path.join(facePath +'O32'),os.path.join(facePath +'O33'),
    os.path.join(facePath +'O35'),os.path.join(facePath +'O37'),os.path.join(facePath +'O38'),os.path.join(facePath +'O39'),os.path.join(facePath +'O42'),os.path.join(facePath +'O44'),
    os.path.join(facePath +'O46'),os.path.join(facePath +'O47'),os.path.join(facePath +'O49'),os.path.join(facePath +'O50'),os.path.join(facePath +'O51'),os.path.join(facePath +'O54'),
    os.path.join(facePath +'O58'),os.path.join(facePath +'O59'),os.path.join(facePath +'O62'),os.path.join(facePath +'O66'),os.path.join(facePath +'O67'),os.path.join(facePath +'O68'),
    os.path.join(facePath +'O69'),os.path.join(facePath +'O71'),os.path.join(facePath +'O76'),os.path.join(facePath +'O77'),os.path.join(facePath +'O79'),os.path.join(facePath +'O80'),
    os.path.join(facePath +'O81'),os.path.join(facePath +'O82'),os.path.join(facePath +'O83'),os.path.join(facePath +'O84')]

imageM = [os.path.join(facePath +'M1'),os.path.join(facePath +'M4'),os.path.join(facePath +'M8'),os.path.join(facePath +'M10'),os.path.join(facePath +'M11'),os.path.join(facePath +'M19'),
    os.path.join(facePath +'M20'),os.path.join(facePath +'M22'),os.path.join(facePath +'M28'),os.path.join(facePath +'M31'),os.path.join(facePath +'M32'),os.path.join(facePath +'M33'),
    os.path.join(facePath +'M35'),os.path.join(facePath +'M37'),os.path.join(facePath +'M38'),os.path.join(facePath +'M39'),os.path.join(facePath +'M42'),os.path.join(facePath +'M44'),
    os.path.join(facePath +'M46'),os.path.join(facePath +'M47'),os.path.join(facePath +'M49'),os.path.join(facePath +'M50'),os.path.join(facePath +'M51'),os.path.join(facePath +'M54'),
    os.path.join(facePath +'M58'),os.path.join(facePath +'M59'),os.path.join(facePath +'M62'),os.path.join(facePath +'M66'),os.path.join(facePath +'M67'),os.path.join(facePath +'M68'),
    os.path.join(facePath +'M69'),os.path.join(facePath +'M71'),os.path.join(facePath +'M76'),os.path.join(facePath +'M77'),os.path.join(facePath +'M79'),os.path.join(facePath +'M80'),
    os.path.join(facePath +'M81'),os.path.join(facePath +'M82'),os.path.join(facePath +'M83'),os.path.join(facePath +'M84')]

imageL = [os.path.join(facePath +'LL1'),os.path.join(facePath +'LL4'),os.path.join(facePath +'LL8'),os.path.join(facePath +'LL10'),os.path.join(facePath +'LL11'),os.path.join(facePath +'LL19'),
    os.path.join(facePath +'LL20'),os.path.join(facePath +'LL22'),os.path.join(facePath +'LL28'),os.path.join(facePath +'LL31'),os.path.join(facePath +'LL32'),os.path.join(facePath +'LL33'),
    os.path.join(facePath +'LL35'),os.path.join(facePath +'LL37'),os.path.join(facePath +'LL38'),os.path.join(facePath +'LL39'),os.path.join(facePath +'LL42'),os.path.join(facePath +'LL44'),
    os.path.join(facePath +'LL46'),os.path.join(facePath +'LL47'),os.path.join(facePath +'LL49'),os.path.join(facePath +'LL50'),os.path.join(facePath +'LL51'),os.path.join(facePath +'LL54'),
    os.path.join(facePath +'LL58'),os.path.join(facePath +'LL59'),os.path.join(facePath +'LL62'),os.path.join(facePath +'LL66'),os.path.join(facePath +'LL67'),os.path.join(facePath +'LL68'),
    os.path.join(facePath +'LL69'),os.path.join(facePath +'LL71'),os.path.join(facePath +'LL76'),os.path.join(facePath +'LL77'),os.path.join(facePath +'LL79'),os.path.join(facePath +'LL80'),
    os.path.join(facePath +'LL81'),os.path.join(facePath +'LL82'),os.path.join(facePath +'LL83'),os.path.join(facePath +'LL84')]

imageR = [os.path.join(facePath +'RR1'),os.path.join(facePath +'RR4'),os.path.join(facePath +'RR8'),os.path.join(facePath +'RR10'),os.path.join(facePath +'RR11'),os.path.join(facePath +'RR19'),
    os.path.join(facePath +'RR20'),os.path.join(facePath +'RR22'),os.path.join(facePath +'RR28'),os.path.join(facePath +'RR31'),os.path.join(facePath +'RR32'),os.path.join(facePath +'RR33'),
    os.path.join(facePath +'RR35'),os.path.join(facePath +'RR37'),os.path.join(facePath +'RR38'),os.path.join(facePath +'RR39'),os.path.join(facePath +'RR42'),os.path.join(facePath +'RR44'),
    os.path.join(facePath +'RR46'),os.path.join(facePath +'RR47'),os.path.join(facePath +'RR49'),os.path.join(facePath +'RR50'),os.path.join(facePath +'RR51'),os.path.join(facePath +'RR54'),
    os.path.join(facePath +'RR58'),os.path.join(facePath +'RR59'),os.path.join(facePath +'RR62'),os.path.join(facePath +'RR66'),os.path.join(facePath +'RR67'),os.path.join(facePath +'RR68'),
    os.path.join(facePath +'RR69'),os.path.join(facePath +'RR71'),os.path.join(facePath +'RR76'),os.path.join(facePath +'RR77'),os.path.join(facePath +'RR79'),os.path.join(facePath +'RR80'),
    os.path.join(facePath +'RR81'),os.path.join(facePath +'RR82'),os.path.join(facePath +'RR83'),os.path.join(facePath +'RR84')]

faceWidth=188.49 # equivalent of 5 dg of visual angle in pixels according to screen dimension
faceHeight=188.07
faceSize=(faceWidth,faceHeight)
posLVF=(-320,0)
posRVF=(320,0)

# create eyetracker object
tracker=EyeTracker(disp)

# setup trial handler
stimList=[]
for image in range (0,len(imageO)):
    for intact in [1,0]: # intact vs mirror
        for field in [1,0]: # LVF
            stimList.append({'intact': intact, 'field':field, 'image':image}) # setting trial sequence
trials = data.TrialHandler(stimList, 1)
trials.data.addDataType('RT')
trials.data.addDataType('response')
clockRT = core.Clock() 

# calibrate eye tracker
calibrationsuccess=False 
while calibrationsuccess==False:
    calibrationsuccess=tracker.calibrate()
    if calibrationsuccess==False:
#        text1= visual.TextStim(win, text="Calibration was unsuccessful, press space to retry", color =(-1,-1,-1))
#        text1.draw()
        tracker.screen.clear()
        tracker.screen.draw_text("""Calibration was unsuccessful.
        
        Press R to retry or press Escape (esc) to quit)""", colour=(255, 255, 255), fontsize=20)
        tracker.disp.fill(tracker.screen)
        tracker.disp.show()
        allKeys = event.waitKeys(keyList=['escape','r'],timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
            
        for thisKey in allKeys:
            if thisKey[0] in ['escape']:
                tracker.close()
                disp.close()
                core.quit()
    
# start eye tracking
tracker.start_recording()

response=''
responseField=''
nTrials=0
for thisTrial in trials:
    nTrials=nTrials+1
    faceName=os.path.split(imageO[trials.thisTrial.image])
    trialstart = libtime.get_time()
    if trials.thisTrial.intact==1: # if intact face
        IM='I'
        if trials.thisTrial.field==1: # if LL in LVF trial
                image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image]+'.jpeg', pos=posLVF,size=faceSize)
                image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image]+'.jpeg', pos=(0,0),size=faceSize) 
                image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image]+'.jpeg', pos=posRVF,size=faceSize)
                LL_location='LVF'
        else: # if LL in RVF 
                image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image]+'.jpeg', pos=posLVF,size=faceSize)
                image_Cent = visual.ImageStim(win, image=imageO[trials.thisTrial.image]+'.jpeg', pos=(0,0),size=faceSize) 
                image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image]+'.jpeg', pos=posRVF,size=faceSize)
                LL_location='RVF'
    else: # if mirror face
        IM='M'
        if trials.thisTrial.field==1: # if LL in LVF trial
                image_LVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image]+'.jpeg', pos=posLVF,size=faceSize)
                image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image]+'.jpeg', pos=(0,0),size=faceSize) 
                image_RVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image]+'.jpeg', pos=posRVF,size=faceSize)
                LL_location='LVF'
        else: # if LL in RVF 
                image_LVF = visual.ImageStim(win, image=imageL[trials.thisTrial.image]+'.jpeg', pos=posLVF,size=faceSize)
                image_Cent = visual.ImageStim(win, image=imageM[trials.thisTrial.image]+'.jpeg', pos=(0,0),size=faceSize) 
                image_RVF = visual.ImageStim(win, image=imageR[trials.thisTrial.image]+'.jpeg', pos=posRVF,size=faceSize)
                LL_location='RVF'


    # show blank screen for 500 ms
    for frameN in range(int(round(params['ISI2']*params['frameRate']))):
        win.update()
        # write trial type to eye-tracker log file
        if frameN==1:
            tracker.log("%d\tblank\t%s\t%s\t%s\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1" % (nTrials, faceName[1], IM, LL_location))  # This output must have 13 columns and 12 tabs


    # show fixation point for one second
    for frameN in range(int(round(params['fp']*params['frameRate']))):
        fixation.draw()
        win.update()
        if frameN==1:
            tracker.log("%d\tfixation\t%s\t%s\t%s\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1" % (nTrials, faceName[1], IM, LL_location))  # This output must have 13 columns and 12 tabs

    # show faces
    thisResponse = None
    while thisResponse == None:
        clockRT.reset()
        image_Cent.draw()
        image_LVF.draw()
        image_RVF.draw()
        win.update()
        tracker.log("%d\tfaces\t%s\t%s\t%s\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1" % (nTrials, faceName[1], IM, LL_location))  # This output must have 13 columns and 12 tabs

# collect response
        allKeys = event.waitKeys(keyList=['escape','left','right'],timeStamped = clockRT)
        for keyTuple in allKeys:
            [thisKey, thisRT] = keyTuple
            
        for thisKey in allKeys:
            if thisKey[0] in ['escape']:
                tracker.log("%d\taborted\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1" % (nTrials+1))  # This output must have 13 columns and 12 tabs
                tracker.stop_recording()
                tracker.close()
                dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\n' %(nTrials,faceName[1],IM, LL_location,response,responseField,round(thisRT,2)))
                shutil.copy('default_TOBII_output.tsv', fileName+'.tsv')
                disp.close()
                core.quit()
            elif (thisKey[0] == 'left'):
                responseField='LVF'
                thisResponse=1
                win.update()
            elif (thisKey[0] == 'right'):
                responseField='RVF'
                thisResponse=1
                win.update()
    if LL_location=='LVF':
        if responseField=='LVF': 
            response='L'
        else:
            response='R'
    else:
        if responseField=='LVF':
            response='R'
        else:
            response='L'
    
    trials.addData('RT', thisRT)
    event.clearEvents()
    
    dataFile.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\n' %(nTrials,faceName[1],IM, LL_location,response,responseField,round(thisRT,2)))
    
    # Copy eye-tracker log file every 50 trials
    if nTrials % 50 == 0:
        shutil.copy('default_TOBII_output.tsv', fileName+'.tsv')

# Indicate end of trials, this line should always immediately follow the trial loop
tracker.log("%d\tend of trial loop\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1" % (nTrials+1))  # This output must have 13 columns and 12 tabs


# stop eye tracking
tracker.stop_recording()


tracker.close()
disp.close()
# Copy eye-tracker log file
shutil.copy('default_TOBII_output.tsv', fileName+'.tsv')

win.close()
core.quit()