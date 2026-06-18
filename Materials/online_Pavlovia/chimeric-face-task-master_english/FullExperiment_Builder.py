#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu Jul  9 12:47:38 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'ChimericFaceTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'sex': '', 'country of residence': '', 'native language': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/zahrahussain/Dropbox/Research/AUB/Experiments/chimericFace_Pavlovia/FullExperiment/FullExperiment_Builder.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "StepQuestScreen"
StepQuestScreenClock = core.Clock()
mouseWelcome = event.Mouse(win=win)
x, y = [None, None]
mouseWelcome.mouseClock = core.Clock()
textStepQuest = visual.TextStim(win=win, name='textStepQuest',
    text='       Please answer the following questions before we begin the experiment. \n\n\n                                            Press SPACE to continue.',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=30, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keySpaceStepQuest = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Languages"
LanguagesClock = core.Clock()
InstrLanguages = visual.TextStim(win=win, name='InstrLanguages',
    text='            Which language are you most fluent in?\n\n\n    1.   English, French or other European language \n\n    2.   Arabic, Hebrew, Urdu, Farsi, Aramaic, Azeri or Kurdish\n\n    3.   Hindi, Malay or other South Asian or South East Asian language\n\n    4.   Chinese, Japanese or Korean\n\n    5.   Amharic, Berber or other African language\n\n    6.   Other\n',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fluentLang = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ProficiencyEng"
ProficiencyEngClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
mouseInstructions = visual.TextStim(win=win, name='mouseInstructions',
    text='Use the mouse to respond below. ',
    font='Arial',
    units='height', pos=(0, 0.45), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
textProficiencyEng = visual.TextStim(win=win, name='textProficiencyEng',
    text='How fluent are you in English or any language written from LEFT to RIGHT?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
engSpeak = visual.Slider(win=win, name='engSpeak',
    size=(0.5, 0.02), pos=(0, 0.2), units='height',
    labels=(0, '', '', '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engRead = visual.Slider(win=win, name='engRead',
    size=(0.5, 0.02), pos=(0, 0), units='height',
    labels=(0, '', '', '', 4), ticks=(0,1,2,3,4),
    granularity=0, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engWrite = visual.Slider(win=win, name='engWrite',
    size=(0.5, 0.02), pos=(0, -0.2), units='height',
    labels=(0, '', '', '', 4), ticks=(0,1,2,3,4),
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text = visual.TextStim(win=win, name='text',
    text='Press SPACE to continue \n',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
spaceKey = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ActivitiesEng"
ActivitiesEngClock = core.Clock()
textActivitiesEng = visual.TextStim(win=win, name='textActivitiesEng',
    text='How OFTEN do you use English or a language with a script written from LEFT to RIGHT for:',
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
engSpeakFreq = visual.RatingScale(win=win, name='engSpeakFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Speaking',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
engListenFreq = visual.RatingScale(win=win, name='engListenFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Listening',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
engReadFreq = visual.RatingScale(win=win, name='engReadFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Reading',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
engWriteFreq = visual.RatingScale(win=win, name='engWriteFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Writing',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.4], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
textSpaceActivitiesEng = visual.TextStim(win=win, name='textSpaceActivitiesEng',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
keyActivitiesEng = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ReadingEng"
ReadingEngClock = core.Clock()
hoursReading = visual.TextStim(win=win, name='hoursReading',
    text='How many hours/day do you read printed or online material in English or a language written from LEFT to RIGHT:',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
engReadHrs = visual.RatingScale(win=win, name='engReadHrs', choices=('<2', '2-4', '4-6', '6-8', '8+'), 
low=0, 
high=4, 
precision=1, 
scale=None,
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.25], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
space = visual.TextStim(win=win, name='space',
    text='Press SPACE to continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_reading = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ProficiencyAr"
ProficiencyArClock = core.Clock()
textProficiencyAr = visual.TextStim(win=win, name='textProficiencyAr',
    text='How fluent are you in Arabic, Hebrew, Urdu, or any language written from RIGHT to LEFT:',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbSpeak = visual.RatingScale(win=win, name='arbSpeak', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Speaking',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
arbRead = visual.RatingScale(win=win, name='arbRead', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Reading',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
arbWrite = visual.RatingScale(win=win, name='arbWrite', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Writing',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
textSpaceAr = visual.TextStim(win=win, name='textSpaceAr',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
keySpaceAr = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ActivitiesAr"
ActivitiesArClock = core.Clock()
textActivitiesAr = visual.TextStim(win=win, name='textActivitiesAr',
    text='How OFTEN do you use Arabic, Hebrew or a language with a script written from RIGHT to LEFT for:',
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbSpeakFreq = visual.RatingScale(win=win, name='arbSpeakFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Speaking',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
arbListenFreq = visual.RatingScale(win=win, name='arbListenFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Listening',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
arbReadFreq = visual.RatingScale(win=win, name='arbReadFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Reading',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
arbWriteFreq = visual.RatingScale(win=win, name='arbWriteFreq', choices=None, 
low=0, 
high=4, 
precision=1, 
scale='Writing',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.4], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
textSpaceActivitiesAr = visual.TextStim(win=win, name='textSpaceActivitiesAr',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
keySpaceActivitiesAr = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ReadingAr"
ReadingArClock = core.Clock()
readingAr = visual.TextStim(win=win, name='readingAr',
    text='How many hours/day do you read printed or online material in Arabic or a language written from LEFT to RIGHT:',
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbReadHrs = visual.RatingScale(win=win, name='arbReadHrs', choices=('>2', '2-4', '4-6', '6-8', '8+'), 
low=0, 
high=4, 
precision=1, 
scale=None,
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
spaceContinue = visual.TextStim(win=win, name='spaceContinue',
    text='Press SPACE to continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_space = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CountryAr"
CountryArClock = core.Clock()
textCountAr = visual.TextStim(win=win, name='textCountAr',
    text='Have you ever lived in a country where Arabic, Hebrew, Urdu, Farsi or Aramaic is the dominant communicating language?\n\n\n                                                                        1. Yes\n\n                                                                        2. No',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbCountryYN = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TimeAr"
TimeArClock = core.Clock()
textLongCountAr = visual.TextStim(win=win, name='textLongCountAr',
    text='For how long have you lived in this country / countries?\n\n        1.  Less than 1 year\n\n        2.  1-3 years\n\n        3.  4-7 years\n\n        4.  More than 7 years',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbCountryTime = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Handedness"
HandednessClock = core.Clock()
textHandedness = visual.TextStim(win=win, name='textHandedness',
    text='Which hand do you use for the following activities:',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
writeHand = visual.RatingScale(win=win, name='writeHand', choices=None, 
low=1, 
high=5, 
precision=1, 
scale='Writing',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart=2, 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
throwHand = visual.RatingScale(win=win, name='throwHand', choices=None, 
low=1, 
high=5, 
precision=1, 
scale='Throwing',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,0], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
toothHand = visual.RatingScale(win=win, name='toothHand', choices=None, 
low=1, 
high=5, 
precision=1, 
scale='Toothbrush',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.2], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
spoonHand = visual.RatingScale(win=win, name='spoonHand', choices=None, 
low=1, 
high=5, 
precision=1, 
scale='Spoon',
labels=(), 
tickMarks=None, 
tickHeight=1.0, 
marker='circle', 
markerStart='', 
markerColor='DarkRed', 
singleClick=True, 
disappear=False, 
textSize=1.0, 
textColor='white', 
textFont='Helvetica Bold', 
showValue=True, 
showAccept=False, 
acceptKeys='', 
acceptPreText='key, click', 
acceptText='accept?', 
acceptSize=1.0, 
leftKeys='left', 
rightKeys='right', 
respKeys=(), 
lineColor='White', 
skipKeys='tab', 
mouseOnly=True, 
noMouse=False, 
size=0.75, 
stretch=1.0, 
pos=[0,-0.4], 
minTime=0.4, 
maxTime=0.0, 
flipVert=False,
depth=0, 
autoLog=True)
textScale = visual.TextStim(win=win, name='textScale',
    text='1: Always left 2: Usually left 3: Both equally 4: Usually right 5: Always right',
    font='Arial',
    pos=(0,0.2), height=0.03, wrapWidth=27, ori=0, 
    color='gray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
textSpaceHand = visual.TextStim(win=win, name='textSpaceHand',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
keySpaceHand = keyboard.Keyboard()

# Initialize components for Routine "Q_Finish"
Q_FinishClock = core.Clock()
QDone = visual.TextStim(win=win, name='QDone',
    text='                Questionnaire complete!\n \nPress SPACE to continue with the experiment',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finishQKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "StepQuestScreen"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouseWelcome
gotValidClick = False  # until a click is received
mouse.setVisible(0)
keySpaceStepQuest.keys = []
keySpaceStepQuest.rt = []
_keySpaceStepQuest_allKeys = []
# keep track of which components have finished
StepQuestScreenComponents = [mouseWelcome, textStepQuest, keySpaceStepQuest]
for thisComponent in StepQuestScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StepQuestScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StepQuestScreen"-------
while continueRoutine:
    # get current time
    t = StepQuestScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StepQuestScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textStepQuest* updates
    if textStepQuest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textStepQuest.frameNStart = frameN  # exact frame index
        textStepQuest.tStart = t  # local t and not account for scr refresh
        textStepQuest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textStepQuest, 'tStartRefresh')  # time at next scr refresh
        textStepQuest.setAutoDraw(True)
    
    # *keySpaceStepQuest* updates
    waitOnFlip = False
    if keySpaceStepQuest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keySpaceStepQuest.frameNStart = frameN  # exact frame index
        keySpaceStepQuest.tStart = t  # local t and not account for scr refresh
        keySpaceStepQuest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySpaceStepQuest, 'tStartRefresh')  # time at next scr refresh
        keySpaceStepQuest.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySpaceStepQuest.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySpaceStepQuest.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySpaceStepQuest.status == STARTED and not waitOnFlip:
        theseKeys = keySpaceStepQuest.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _keySpaceStepQuest_allKeys.extend(theseKeys)
        if len(_keySpaceStepQuest_allKeys):
            keySpaceStepQuest.keys = _keySpaceStepQuest_allKeys[-1].name  # just the last key pressed
            keySpaceStepQuest.rt = _keySpaceStepQuest_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StepQuestScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StepQuestScreen"-------
for thisComponent in StepQuestScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "StepQuestScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Languages"-------
continueRoutine = True
# update component parameters for each repeat
fluentLang.keys = []
fluentLang.rt = []
_fluentLang_allKeys = []
# keep track of which components have finished
LanguagesComponents = [InstrLanguages, fluentLang]
for thisComponent in LanguagesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LanguagesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Languages"-------
while continueRoutine:
    # get current time
    t = LanguagesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LanguagesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrLanguages* updates
    if InstrLanguages.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrLanguages.frameNStart = frameN  # exact frame index
        InstrLanguages.tStart = t  # local t and not account for scr refresh
        InstrLanguages.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrLanguages, 'tStartRefresh')  # time at next scr refresh
        InstrLanguages.setAutoDraw(True)
    
    # *fluentLang* updates
    waitOnFlip = False
    if fluentLang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fluentLang.frameNStart = frameN  # exact frame index
        fluentLang.tStart = t  # local t and not account for scr refresh
        fluentLang.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fluentLang, 'tStartRefresh')  # time at next scr refresh
        fluentLang.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fluentLang.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fluentLang.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fluentLang.status == STARTED and not waitOnFlip:
        theseKeys = fluentLang.getKeys(keyList=['1', '2', '3', '4', '5', '6', 'space'], waitRelease=False)
        _fluentLang_allKeys.extend(theseKeys)
        if len(_fluentLang_allKeys):
            fluentLang.keys = _fluentLang_allKeys[-1].name  # just the last key pressed
            fluentLang.rt = _fluentLang_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LanguagesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Languages"-------
for thisComponent in LanguagesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if fluentLang.keys in ['', [], None]:  # No response was made
    fluentLang.keys = None
thisExp.addData('fluentLang.keys',fluentLang.keys)
if fluentLang.keys != None:  # we had a response
    thisExp.addData('fluentLang.rt', fluentLang.rt)
thisExp.nextEntry()
# the Routine "Languages" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ProficiencyEng"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
mouse.setVisible(1)
mouse.setPos(newPos=(0,0.25))
engSpeak.reset()
engRead.reset()
engWrite.reset()
spaceKey.keys = []
spaceKey.rt = []
_spaceKey_allKeys = []
# keep track of which components have finished
ProficiencyEngComponents = [mouse, mouseInstructions, textProficiencyEng, engSpeak, engRead, engWrite, text, spaceKey]
for thisComponent in ProficiencyEngComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProficiencyEngClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProficiencyEng"-------
while continueRoutine:
    # get current time
    t = ProficiencyEngClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProficiencyEngClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mouseInstructions* updates
    if mouseInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouseInstructions.frameNStart = frameN  # exact frame index
        mouseInstructions.tStart = t  # local t and not account for scr refresh
        mouseInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouseInstructions, 'tStartRefresh')  # time at next scr refresh
        mouseInstructions.setAutoDraw(True)
    
    # *textProficiencyEng* updates
    if textProficiencyEng.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textProficiencyEng.frameNStart = frameN  # exact frame index
        textProficiencyEng.tStart = t  # local t and not account for scr refresh
        textProficiencyEng.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textProficiencyEng, 'tStartRefresh')  # time at next scr refresh
        textProficiencyEng.setAutoDraw(True)
    
    # *engSpeak* updates
    if engSpeak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engSpeak.frameNStart = frameN  # exact frame index
        engSpeak.tStart = t  # local t and not account for scr refresh
        engSpeak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engSpeak, 'tStartRefresh')  # time at next scr refresh
        engSpeak.setAutoDraw(True)
    
    # *engRead* updates
    if engRead.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engRead.frameNStart = frameN  # exact frame index
        engRead.tStart = t  # local t and not account for scr refresh
        engRead.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engRead, 'tStartRefresh')  # time at next scr refresh
        engRead.setAutoDraw(True)
    
    # *engWrite* updates
    if engWrite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engWrite.frameNStart = frameN  # exact frame index
        engWrite.tStart = t  # local t and not account for scr refresh
        engWrite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engWrite, 'tStartRefresh')  # time at next scr refresh
        engWrite.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *spaceKey* updates
    waitOnFlip = False
    if spaceKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceKey.frameNStart = frameN  # exact frame index
        spaceKey.tStart = t  # local t and not account for scr refresh
        spaceKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceKey, 'tStartRefresh')  # time at next scr refresh
        spaceKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(spaceKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(spaceKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if spaceKey.status == STARTED and not waitOnFlip:
        theseKeys = spaceKey.getKeys(keyList=['space'], waitRelease=False)
        _spaceKey_allKeys.extend(theseKeys)
        if len(_spaceKey_allKeys):
            spaceKey.keys = _spaceKey_allKeys[-1].name  # just the last key pressed
            spaceKey.rt = _spaceKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProficiencyEngComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProficiencyEng"-------
for thisComponent in ProficiencyEngComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('engSpeak.response', engSpeak.getRating())
thisExp.addData('engRead.response', engRead.getRating())
thisExp.addData('engWrite.response', engWrite.getRating())
thisExp.addData('engWrite.rt', engWrite.getRT())
thisExp.addData('engWrite.started', engWrite.tStartRefresh)
thisExp.addData('engWrite.stopped', engWrite.tStopRefresh)
# the Routine "ProficiencyEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ActivitiesEng"-------
continueRoutine = True
# update component parameters for each repeat
engSpeakFreq.reset()
engListenFreq.reset()
engReadFreq.reset()
engWriteFreq.reset()
keyActivitiesEng.keys = []
keyActivitiesEng.rt = []
_keyActivitiesEng_allKeys = []
# keep track of which components have finished
ActivitiesEngComponents = [textActivitiesEng, engSpeakFreq, engListenFreq, engReadFreq, engWriteFreq, textSpaceActivitiesEng, keyActivitiesEng]
for thisComponent in ActivitiesEngComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ActivitiesEngClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ActivitiesEng"-------
while continueRoutine:
    # get current time
    t = ActivitiesEngClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ActivitiesEngClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textActivitiesEng* updates
    if textActivitiesEng.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textActivitiesEng.frameNStart = frameN  # exact frame index
        textActivitiesEng.tStart = t  # local t and not account for scr refresh
        textActivitiesEng.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textActivitiesEng, 'tStartRefresh')  # time at next scr refresh
        textActivitiesEng.setAutoDraw(True)
    # *engSpeakFreq* updates
    if engSpeakFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engSpeakFreq.frameNStart = frameN  # exact frame index
        engSpeakFreq.tStart = t  # local t and not account for scr refresh
        engSpeakFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engSpeakFreq, 'tStartRefresh')  # time at next scr refresh
        engSpeakFreq.setAutoDraw(True)
    # *engListenFreq* updates
    if engListenFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engListenFreq.frameNStart = frameN  # exact frame index
        engListenFreq.tStart = t  # local t and not account for scr refresh
        engListenFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engListenFreq, 'tStartRefresh')  # time at next scr refresh
        engListenFreq.setAutoDraw(True)
    # *engReadFreq* updates
    if engReadFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engReadFreq.frameNStart = frameN  # exact frame index
        engReadFreq.tStart = t  # local t and not account for scr refresh
        engReadFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engReadFreq, 'tStartRefresh')  # time at next scr refresh
        engReadFreq.setAutoDraw(True)
    # *engWriteFreq* updates
    if engWriteFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engWriteFreq.frameNStart = frameN  # exact frame index
        engWriteFreq.tStart = t  # local t and not account for scr refresh
        engWriteFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engWriteFreq, 'tStartRefresh')  # time at next scr refresh
        engWriteFreq.setAutoDraw(True)
    
    # *textSpaceActivitiesEng* updates
    if textSpaceActivitiesEng.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpaceActivitiesEng.frameNStart = frameN  # exact frame index
        textSpaceActivitiesEng.tStart = t  # local t and not account for scr refresh
        textSpaceActivitiesEng.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpaceActivitiesEng, 'tStartRefresh')  # time at next scr refresh
        textSpaceActivitiesEng.setAutoDraw(True)
    
    # *keyActivitiesEng* updates
    waitOnFlip = False
    if keyActivitiesEng.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyActivitiesEng.frameNStart = frameN  # exact frame index
        keyActivitiesEng.tStart = t  # local t and not account for scr refresh
        keyActivitiesEng.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyActivitiesEng, 'tStartRefresh')  # time at next scr refresh
        keyActivitiesEng.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyActivitiesEng.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyActivitiesEng.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyActivitiesEng.status == STARTED and not waitOnFlip:
        theseKeys = keyActivitiesEng.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _keyActivitiesEng_allKeys.extend(theseKeys)
        if len(_keyActivitiesEng_allKeys):
            keyActivitiesEng.keys = _keyActivitiesEng_allKeys[-1].name  # just the last key pressed
            keyActivitiesEng.rt = _keyActivitiesEng_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ActivitiesEngComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ActivitiesEng"-------
for thisComponent in ActivitiesEngComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('engSpeakFreq.response', engSpeakFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('engListenFreq.response', engListenFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('engReadFreq.response', engReadFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('engWriteFreq.response', engWriteFreq.getRating())
thisExp.nextEntry()
# the Routine "ActivitiesEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ReadingEng"-------
continueRoutine = True
# update component parameters for each repeat
engReadHrs.reset()
key_reading.keys = []
key_reading.rt = []
_key_reading_allKeys = []
# keep track of which components have finished
ReadingEngComponents = [hoursReading, engReadHrs, space, key_reading]
for thisComponent in ReadingEngComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadingEngClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ReadingEng"-------
while continueRoutine:
    # get current time
    t = ReadingEngClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadingEngClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hoursReading* updates
    if hoursReading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hoursReading.frameNStart = frameN  # exact frame index
        hoursReading.tStart = t  # local t and not account for scr refresh
        hoursReading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hoursReading, 'tStartRefresh')  # time at next scr refresh
        hoursReading.setAutoDraw(True)
    # *engReadHrs* updates
    if engReadHrs.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engReadHrs.frameNStart = frameN  # exact frame index
        engReadHrs.tStart = t  # local t and not account for scr refresh
        engReadHrs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engReadHrs, 'tStartRefresh')  # time at next scr refresh
        engReadHrs.setAutoDraw(True)
    
    # *space* updates
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.setAutoDraw(True)
    
    # *key_reading* updates
    waitOnFlip = False
    if key_reading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_reading.frameNStart = frameN  # exact frame index
        key_reading.tStart = t  # local t and not account for scr refresh
        key_reading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_reading, 'tStartRefresh')  # time at next scr refresh
        key_reading.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_reading.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_reading.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_reading.status == STARTED and not waitOnFlip:
        theseKeys = key_reading.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _key_reading_allKeys.extend(theseKeys)
        if len(_key_reading_allKeys):
            key_reading.keys = _key_reading_allKeys[-1].name  # just the last key pressed
            key_reading.rt = _key_reading_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadingEngComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ReadingEng"-------
for thisComponent in ReadingEngComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('engReadHrs.response', engReadHrs.getRating())
thisExp.nextEntry()
# the Routine "ReadingEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ProficiencyAr"-------
continueRoutine = True
# update component parameters for each repeat
arbSpeak.reset()
arbRead.reset()
arbWrite.reset()
keySpaceAr.keys = []
keySpaceAr.rt = []
_keySpaceAr_allKeys = []
# keep track of which components have finished
ProficiencyArComponents = [textProficiencyAr, arbSpeak, arbRead, arbWrite, textSpaceAr, keySpaceAr]
for thisComponent in ProficiencyArComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProficiencyArClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProficiencyAr"-------
while continueRoutine:
    # get current time
    t = ProficiencyArClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProficiencyArClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textProficiencyAr* updates
    if textProficiencyAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textProficiencyAr.frameNStart = frameN  # exact frame index
        textProficiencyAr.tStart = t  # local t and not account for scr refresh
        textProficiencyAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textProficiencyAr, 'tStartRefresh')  # time at next scr refresh
        textProficiencyAr.setAutoDraw(True)
    # *arbSpeak* updates
    if arbSpeak.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbSpeak.frameNStart = frameN  # exact frame index
        arbSpeak.tStart = t  # local t and not account for scr refresh
        arbSpeak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbSpeak, 'tStartRefresh')  # time at next scr refresh
        arbSpeak.setAutoDraw(True)
    # *arbRead* updates
    if arbRead.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbRead.frameNStart = frameN  # exact frame index
        arbRead.tStart = t  # local t and not account for scr refresh
        arbRead.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbRead, 'tStartRefresh')  # time at next scr refresh
        arbRead.setAutoDraw(True)
    # *arbWrite* updates
    if arbWrite.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbWrite.frameNStart = frameN  # exact frame index
        arbWrite.tStart = t  # local t and not account for scr refresh
        arbWrite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbWrite, 'tStartRefresh')  # time at next scr refresh
        arbWrite.setAutoDraw(True)
    
    # *textSpaceAr* updates
    if textSpaceAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpaceAr.frameNStart = frameN  # exact frame index
        textSpaceAr.tStart = t  # local t and not account for scr refresh
        textSpaceAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpaceAr, 'tStartRefresh')  # time at next scr refresh
        textSpaceAr.setAutoDraw(True)
    
    # *keySpaceAr* updates
    waitOnFlip = False
    if keySpaceAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keySpaceAr.frameNStart = frameN  # exact frame index
        keySpaceAr.tStart = t  # local t and not account for scr refresh
        keySpaceAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySpaceAr, 'tStartRefresh')  # time at next scr refresh
        keySpaceAr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySpaceAr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySpaceAr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySpaceAr.status == STARTED and not waitOnFlip:
        theseKeys = keySpaceAr.getKeys(keyList=['space'], waitRelease=False)
        _keySpaceAr_allKeys.extend(theseKeys)
        if len(_keySpaceAr_allKeys):
            keySpaceAr.keys = _keySpaceAr_allKeys[-1].name  # just the last key pressed
            keySpaceAr.rt = _keySpaceAr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProficiencyArComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProficiencyAr"-------
for thisComponent in ProficiencyArComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbSpeak.response', arbSpeak.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbRead.response', arbRead.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbWrite.response', arbWrite.getRating())
thisExp.nextEntry()
# the Routine "ProficiencyAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ActivitiesAr"-------
continueRoutine = True
# update component parameters for each repeat
arbSpeakFreq.reset()
arbListenFreq.reset()
arbReadFreq.reset()
arbWriteFreq.reset()
keySpaceActivitiesAr.keys = []
keySpaceActivitiesAr.rt = []
_keySpaceActivitiesAr_allKeys = []
# keep track of which components have finished
ActivitiesArComponents = [textActivitiesAr, arbSpeakFreq, arbListenFreq, arbReadFreq, arbWriteFreq, textSpaceActivitiesAr, keySpaceActivitiesAr]
for thisComponent in ActivitiesArComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ActivitiesArClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ActivitiesAr"-------
while continueRoutine:
    # get current time
    t = ActivitiesArClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ActivitiesArClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textActivitiesAr* updates
    if textActivitiesAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textActivitiesAr.frameNStart = frameN  # exact frame index
        textActivitiesAr.tStart = t  # local t and not account for scr refresh
        textActivitiesAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textActivitiesAr, 'tStartRefresh')  # time at next scr refresh
        textActivitiesAr.setAutoDraw(True)
    # *arbSpeakFreq* updates
    if arbSpeakFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbSpeakFreq.frameNStart = frameN  # exact frame index
        arbSpeakFreq.tStart = t  # local t and not account for scr refresh
        arbSpeakFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbSpeakFreq, 'tStartRefresh')  # time at next scr refresh
        arbSpeakFreq.setAutoDraw(True)
    # *arbListenFreq* updates
    if arbListenFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbListenFreq.frameNStart = frameN  # exact frame index
        arbListenFreq.tStart = t  # local t and not account for scr refresh
        arbListenFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbListenFreq, 'tStartRefresh')  # time at next scr refresh
        arbListenFreq.setAutoDraw(True)
    # *arbReadFreq* updates
    if arbReadFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbReadFreq.frameNStart = frameN  # exact frame index
        arbReadFreq.tStart = t  # local t and not account for scr refresh
        arbReadFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbReadFreq, 'tStartRefresh')  # time at next scr refresh
        arbReadFreq.setAutoDraw(True)
    # *arbWriteFreq* updates
    if arbWriteFreq.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbWriteFreq.frameNStart = frameN  # exact frame index
        arbWriteFreq.tStart = t  # local t and not account for scr refresh
        arbWriteFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbWriteFreq, 'tStartRefresh')  # time at next scr refresh
        arbWriteFreq.setAutoDraw(True)
    
    # *textSpaceActivitiesAr* updates
    if textSpaceActivitiesAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpaceActivitiesAr.frameNStart = frameN  # exact frame index
        textSpaceActivitiesAr.tStart = t  # local t and not account for scr refresh
        textSpaceActivitiesAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpaceActivitiesAr, 'tStartRefresh')  # time at next scr refresh
        textSpaceActivitiesAr.setAutoDraw(True)
    
    # *keySpaceActivitiesAr* updates
    waitOnFlip = False
    if keySpaceActivitiesAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keySpaceActivitiesAr.frameNStart = frameN  # exact frame index
        keySpaceActivitiesAr.tStart = t  # local t and not account for scr refresh
        keySpaceActivitiesAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySpaceActivitiesAr, 'tStartRefresh')  # time at next scr refresh
        keySpaceActivitiesAr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySpaceActivitiesAr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySpaceActivitiesAr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySpaceActivitiesAr.status == STARTED and not waitOnFlip:
        theseKeys = keySpaceActivitiesAr.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _keySpaceActivitiesAr_allKeys.extend(theseKeys)
        if len(_keySpaceActivitiesAr_allKeys):
            keySpaceActivitiesAr.keys = _keySpaceActivitiesAr_allKeys[-1].name  # just the last key pressed
            keySpaceActivitiesAr.rt = _keySpaceActivitiesAr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ActivitiesArComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ActivitiesAr"-------
for thisComponent in ActivitiesArComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbSpeakFreq.response', arbSpeakFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbListenFreq.response', arbListenFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbReadFreq.response', arbReadFreq.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbWriteFreq.response', arbWriteFreq.getRating())
thisExp.nextEntry()
# the Routine "ActivitiesAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ReadingAr"-------
continueRoutine = True
# update component parameters for each repeat
arbReadHrs.reset()
key_space.keys = []
key_space.rt = []
_key_space_allKeys = []
# keep track of which components have finished
ReadingArComponents = [readingAr, arbReadHrs, spaceContinue, key_space]
for thisComponent in ReadingArComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadingArClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ReadingAr"-------
while continueRoutine:
    # get current time
    t = ReadingArClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadingArClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *readingAr* updates
    if readingAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        readingAr.frameNStart = frameN  # exact frame index
        readingAr.tStart = t  # local t and not account for scr refresh
        readingAr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(readingAr, 'tStartRefresh')  # time at next scr refresh
        readingAr.setAutoDraw(True)
    # *arbReadHrs* updates
    if arbReadHrs.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arbReadHrs.frameNStart = frameN  # exact frame index
        arbReadHrs.tStart = t  # local t and not account for scr refresh
        arbReadHrs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arbReadHrs, 'tStartRefresh')  # time at next scr refresh
        arbReadHrs.setAutoDraw(True)
    
    # *spaceContinue* updates
    if spaceContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceContinue.frameNStart = frameN  # exact frame index
        spaceContinue.tStart = t  # local t and not account for scr refresh
        spaceContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceContinue, 'tStartRefresh')  # time at next scr refresh
        spaceContinue.setAutoDraw(True)
    
    # *key_space* updates
    waitOnFlip = False
    if key_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_space.frameNStart = frameN  # exact frame index
        key_space.tStart = t  # local t and not account for scr refresh
        key_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_space, 'tStartRefresh')  # time at next scr refresh
        key_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_space.status == STARTED and not waitOnFlip:
        theseKeys = key_space.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _key_space_allKeys.extend(theseKeys)
        if len(_key_space_allKeys):
            key_space.keys = _key_space_allKeys[-1].name  # just the last key pressed
            key_space.rt = _key_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadingArComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ReadingAr"-------
for thisComponent in ReadingArComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('arbReadHrs.response', arbReadHrs.getRating())
thisExp.nextEntry()
# the Routine "ReadingAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loopTimeAr = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loopTimeAr')
thisExp.addLoop(loopTimeAr)  # add the loop to the experiment
thisLoopTimeAr = loopTimeAr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopTimeAr.rgb)
if thisLoopTimeAr != None:
    for paramName in thisLoopTimeAr:
        exec('{} = thisLoopTimeAr[paramName]'.format(paramName))

for thisLoopTimeAr in loopTimeAr:
    currentLoop = loopTimeAr
    # abbreviate parameter names if possible (e.g. rgb = thisLoopTimeAr.rgb)
    if thisLoopTimeAr != None:
        for paramName in thisLoopTimeAr:
            exec('{} = thisLoopTimeAr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "CountryAr"-------
    continueRoutine = True
    # update component parameters for each repeat
    arbCountryYN.keys = []
    arbCountryYN.rt = []
    _arbCountryYN_allKeys = []
    # keep track of which components have finished
    CountryArComponents = [textCountAr, arbCountryYN]
    for thisComponent in CountryArComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CountryArClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CountryAr"-------
    while continueRoutine:
        # get current time
        t = CountryArClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CountryArClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textCountAr* updates
        if textCountAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textCountAr.frameNStart = frameN  # exact frame index
            textCountAr.tStart = t  # local t and not account for scr refresh
            textCountAr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textCountAr, 'tStartRefresh')  # time at next scr refresh
            textCountAr.setAutoDraw(True)
        
        # *arbCountryYN* updates
        waitOnFlip = False
        if arbCountryYN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arbCountryYN.frameNStart = frameN  # exact frame index
            arbCountryYN.tStart = t  # local t and not account for scr refresh
            arbCountryYN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arbCountryYN, 'tStartRefresh')  # time at next scr refresh
            arbCountryYN.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(arbCountryYN.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(arbCountryYN.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if arbCountryYN.status == STARTED and not waitOnFlip:
            theseKeys = arbCountryYN.getKeys(keyList=['1', '2', 'escape'], waitRelease=False)
            _arbCountryYN_allKeys.extend(theseKeys)
            if len(_arbCountryYN_allKeys):
                arbCountryYN.keys = _arbCountryYN_allKeys[-1].name  # just the last key pressed
                arbCountryYN.rt = _arbCountryYN_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountryArComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CountryAr"-------
    for thisComponent in CountryArComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if arbCountryYN.keys in ['', [], None]:  # No response was made
        arbCountryYN.keys = None
    loopTimeAr.addData('arbCountryYN.keys',arbCountryYN.keys)
    if arbCountryYN.keys != None:  # we had a response
        loopTimeAr.addData('arbCountryYN.rt', arbCountryYN.rt)
    # the Routine "CountryAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [textBlank]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(True)
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "TimeAr"-------
    continueRoutine = True
    # update component parameters for each repeat
    arbCountryTime.keys = []
    arbCountryTime.rt = []
    _arbCountryTime_allKeys = []
    event.clearEvents('keyboard')
    keys = event.getKeys()
    if arbCountryYN.keys=='2':
        continueRoutine = False
    # keep track of which components have finished
    TimeArComponents = [textLongCountAr, arbCountryTime]
    for thisComponent in TimeArComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TimeArClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TimeAr"-------
    while continueRoutine:
        # get current time
        t = TimeArClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TimeArClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLongCountAr* updates
        if textLongCountAr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLongCountAr.frameNStart = frameN  # exact frame index
            textLongCountAr.tStart = t  # local t and not account for scr refresh
            textLongCountAr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLongCountAr, 'tStartRefresh')  # time at next scr refresh
            textLongCountAr.setAutoDraw(True)
        
        # *arbCountryTime* updates
        waitOnFlip = False
        if arbCountryTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arbCountryTime.frameNStart = frameN  # exact frame index
            arbCountryTime.tStart = t  # local t and not account for scr refresh
            arbCountryTime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arbCountryTime, 'tStartRefresh')  # time at next scr refresh
            arbCountryTime.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(arbCountryTime.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(arbCountryTime.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if arbCountryTime.status == STARTED and not waitOnFlip:
            theseKeys = arbCountryTime.getKeys(keyList=['1', '2', '3', '4', 'escape'], waitRelease=False)
            _arbCountryTime_allKeys.extend(theseKeys)
            if len(_arbCountryTime_allKeys):
                arbCountryTime.keys = _arbCountryTime_allKeys[-1].name  # just the last key pressed
                arbCountryTime.rt = _arbCountryTime_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TimeArComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TimeAr"-------
    for thisComponent in TimeArComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if arbCountryTime.keys in ['', [], None]:  # No response was made
        arbCountryTime.keys = None
    loopTimeAr.addData('arbCountryTime.keys',arbCountryTime.keys)
    if arbCountryTime.keys != None:  # we had a response
        loopTimeAr.addData('arbCountryTime.rt', arbCountryTime.rt)
    # the Routine "TimeAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'loopTimeAr'


# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [textBlank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Handedness"-------
continueRoutine = True
# update component parameters for each repeat
writeHand.reset()
throwHand.reset()
toothHand.reset()
spoonHand.reset()
keySpaceHand.keys = []
keySpaceHand.rt = []
_keySpaceHand_allKeys = []
# keep track of which components have finished
HandednessComponents = [textHandedness, writeHand, throwHand, toothHand, spoonHand, textScale, textSpaceHand, keySpaceHand]
for thisComponent in HandednessComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HandednessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Handedness"-------
while continueRoutine:
    # get current time
    t = HandednessClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HandednessClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textHandedness* updates
    if textHandedness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textHandedness.frameNStart = frameN  # exact frame index
        textHandedness.tStart = t  # local t and not account for scr refresh
        textHandedness.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textHandedness, 'tStartRefresh')  # time at next scr refresh
        textHandedness.setAutoDraw(True)
    # *writeHand* updates
    if writeHand.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        writeHand.frameNStart = frameN  # exact frame index
        writeHand.tStart = t  # local t and not account for scr refresh
        writeHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(writeHand, 'tStartRefresh')  # time at next scr refresh
        writeHand.setAutoDraw(True)
    # *throwHand* updates
    if throwHand.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        throwHand.frameNStart = frameN  # exact frame index
        throwHand.tStart = t  # local t and not account for scr refresh
        throwHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(throwHand, 'tStartRefresh')  # time at next scr refresh
        throwHand.setAutoDraw(True)
    # *toothHand* updates
    if toothHand.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        toothHand.frameNStart = frameN  # exact frame index
        toothHand.tStart = t  # local t and not account for scr refresh
        toothHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(toothHand, 'tStartRefresh')  # time at next scr refresh
        toothHand.setAutoDraw(True)
    # *spoonHand* updates
    if spoonHand.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spoonHand.frameNStart = frameN  # exact frame index
        spoonHand.tStart = t  # local t and not account for scr refresh
        spoonHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spoonHand, 'tStartRefresh')  # time at next scr refresh
        spoonHand.setAutoDraw(True)
    
    # *textScale* updates
    if textScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textScale.frameNStart = frameN  # exact frame index
        textScale.tStart = t  # local t and not account for scr refresh
        textScale.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textScale, 'tStartRefresh')  # time at next scr refresh
        textScale.setAutoDraw(True)
    
    # *textSpaceHand* updates
    if textSpaceHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpaceHand.frameNStart = frameN  # exact frame index
        textSpaceHand.tStart = t  # local t and not account for scr refresh
        textSpaceHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpaceHand, 'tStartRefresh')  # time at next scr refresh
        textSpaceHand.setAutoDraw(True)
    
    # *keySpaceHand* updates
    waitOnFlip = False
    if keySpaceHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keySpaceHand.frameNStart = frameN  # exact frame index
        keySpaceHand.tStart = t  # local t and not account for scr refresh
        keySpaceHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySpaceHand, 'tStartRefresh')  # time at next scr refresh
        keySpaceHand.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySpaceHand.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySpaceHand.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySpaceHand.status == STARTED and not waitOnFlip:
        theseKeys = keySpaceHand.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _keySpaceHand_allKeys.extend(theseKeys)
        if len(_keySpaceHand_allKeys):
            keySpaceHand.keys = _keySpaceHand_allKeys[-1].name  # just the last key pressed
            keySpaceHand.rt = _keySpaceHand_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HandednessComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Handedness"-------
for thisComponent in HandednessComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('writeHand.response', writeHand.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('throwHand.response', throwHand.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('toothHand.response', toothHand.getRating())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('spoonHand.response', spoonHand.getRating())
thisExp.nextEntry()
# the Routine "Handedness" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Q_Finish"-------
continueRoutine = True
# update component parameters for each repeat
finishQKey.keys = []
finishQKey.rt = []
_finishQKey_allKeys = []
# keep track of which components have finished
Q_FinishComponents = [QDone, finishQKey]
for thisComponent in Q_FinishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Q_FinishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Q_Finish"-------
while continueRoutine:
    # get current time
    t = Q_FinishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Q_FinishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *QDone* updates
    if QDone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        QDone.frameNStart = frameN  # exact frame index
        QDone.tStart = t  # local t and not account for scr refresh
        QDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(QDone, 'tStartRefresh')  # time at next scr refresh
        QDone.setAutoDraw(True)
    
    # *finishQKey* updates
    waitOnFlip = False
    if finishQKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finishQKey.frameNStart = frameN  # exact frame index
        finishQKey.tStart = t  # local t and not account for scr refresh
        finishQKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finishQKey, 'tStartRefresh')  # time at next scr refresh
        finishQKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finishQKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(finishQKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if finishQKey.status == STARTED and not waitOnFlip:
        theseKeys = finishQKey.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _finishQKey_allKeys.extend(theseKeys)
        if len(_finishQKey_allKeys):
            finishQKey.keys = _finishQKey_allKeys[-1].name  # just the last key pressed
            finishQKey.rt = _finishQKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Q_FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Q_Finish"-------
for thisComponent in Q_FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Q_Finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
