#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Mon Oct 19 16:27:08 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.1.2')


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
    originPath='/Users/rayanekouzy/Documents/PsychopyCodes/PsychopyPavlovia/chimeric-face-task/FullExperiment_Builder_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "ConsentForm"
ConsentFormClock = core.Clock()
consentForm = visual.ImageStim(
    win=win,
    name='consentForm', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
spaceConsent = visual.TextStim(win=win, name='spaceConsent',
    text='Press space to continue\n',
    font='Arial',
    pos=(0.6, 0), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AcceptConsent"
AcceptConsentClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Press space to give your consent and proceed with the study.\n\n',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Qstart"
QstartClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='                Thank you for agreeing to participate in this study.\n\nFirst, we will ask you some questions about your language experience.\n\n                    This will be followed by the experimental task. \n\n                   The whole experiment will take about 30 minutes.\n\n                                        Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=1, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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
    text='     Which language are you most fluent in?\n\n\n1.   English, French or other European language \n\n2.   Arabic, Hebrew, Urdu, Farsi, Aramaic, Azeri or Kurdish\n\n3.   Hindi, Malay or other South Asian or South East Asian language\n\n4.   Chinese, Japanese or Korean\n\n5.   Amharic, Berber or other African language\n\n6.   Other\n',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fluentLang = keyboard.Keyboard()
spaceTextLang = visual.TextStim(win=win, name='spaceTextLang',
    text='Press space to continue ',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

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
textProficiencyEng = visual.TextStim(win=win, name='textProficiencyEng',
    text='How fluent are you in English or any language written from LEFT to RIGHT?\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    pos=(0, 0.32), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
engSpeak = visual.Slider(win=win, name='engSpeak',
    size=(0.5, 0.02), pos=(0, 0.2), units='height',
    labels=[0, '' , 2, '' , 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engRead = visual.Slider(win=win, name='engRead',
    size=(0.5, 0.02), pos=(0, 0), units='height',
    labels=[0, '' , 2, '' , 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engWrite = visual.Slider(win=win, name='engWrite',
    size=(0.5, 0.02), pos=(0, -0.2), units='height',
    labels=[0, '', 2, '', 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
eSpeakLabel = visual.TextStim(win=win, name='eSpeakLabel',
    text='Speaking',
    font='Arial',
    units='height', pos=(-0.35, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
eReadLabel = visual.TextStim(win=win, name='eReadLabel',
    text='Reading',
    font='Arial',
    units='height', pos=(-0.35,0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
eWriteLabel = visual.TextStim(win=win, name='eWriteLabel',
    text='Writing',
    font='Arial',
    units='height', pos=(-0.35, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
spaceText = visual.TextStim(win=win, name='spaceText',
    text='Press space to continue ',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
spaceKey = keyboard.Keyboard()
mouseProf = event.Mouse(win=win)
x, y = [None, None]
mouseProf.mouseClock = core.Clock()

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
    text='How OFTEN do you use English or a language with a script written from LEFT to RIGHT for:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    units='height', pos=(0, 0.32), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
engSpeakFreq = visual.Slider(win=win, name='engSpeakFreq',
    size=(0.5, 0.02), pos=(0, 0.2), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engListenFreq = visual.Slider(win=win, name='engListenFreq',
    size=(0.5, 0.02), pos=(0, 0.08), units='height',
    labels=[0, '', 2 ,'', 4], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engReadFreq = visual.Slider(win=win, name='engReadFreq',
    size=(0.5, 0.02), pos=(0, -0.04), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engWriteFreq = visual.Slider(win=win, name='engWriteFreq',
    size=(0.5, 0.02), pos=(0, -0.16), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
engSpeakLabel = visual.TextStim(win=win, name='engSpeakLabel',
    text='Speaking',
    font='Arial',
    units='height', pos=(-0.35, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
engListenLabel = visual.TextStim(win=win, name='engListenLabel',
    text='Listening\n',
    font='Arial',
    units='height', pos=(-0.35, 0.08), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
engReadLabel = visual.TextStim(win=win, name='engReadLabel',
    text='Reading',
    font='Arial',
    units='height', pos=(-0.35, -0.04), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
engWriteLabel = visual.TextStim(win=win, name='engWriteLabel',
    text='Writing',
    font='Arial',
    pos=(-0.35, -0.16), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
textSpaceActivitiesEng = visual.TextStim(win=win, name='textSpaceActivitiesEng',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
keyActivitiesEng = keyboard.Keyboard()
mouseActEng = event.Mouse(win=win)
x, y = [None, None]
mouseActEng.mouseClock = core.Clock()

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
    text='How many hours/day do you read printed or online material in English or a language written from LEFT to RIGHT:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
slider_engReadHrs = visual.Slider(win=win, name='slider_engReadHrs',
    size=(0.5,0.02), pos=(0, 0.15), units=None,
    labels=['<2', '2-4', '4-6', '6-8', '8+'], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
space = visual.TextStim(win=win, name='space',
    text='Press space to continue',
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
    text='How fluent are you in Arabic, Hebrew, Urdu, or any language written from RIGHT to LEFT:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ArSpeak = visual.Slider(win=win, name='ArSpeak',
    size=(0.5,0.02), pos=(0, 0.2), units=None,
    labels=[0, '', 2, '', 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
ArRead = visual.Slider(win=win, name='ArRead',
    size=(0.5,0.02), pos=(0, 0), units=None,
    labels=[0, '', 2, '', 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
ArWrite = visual.Slider(win=win, name='ArWrite',
    size=(0.5,0.02), pos=(0, -0.2), units=None,
    labels=[0, '', 2, '', 4], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
arSpeakLabel = visual.TextStim(win=win, name='arSpeakLabel',
    text='Speaking',
    font='Arial',
    pos=(-0.35, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
arReadLabel = visual.TextStim(win=win, name='arReadLabel',
    text='Reading',
    font='Arial',
    pos=(-0.35, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
arWriteLabel = visual.TextStim(win=win, name='arWriteLabel',
    text='Writing',
    font='Arial',
    pos=(-0.35, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
textSpaceAr = visual.TextStim(win=win, name='textSpaceAr',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
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
    text='How OFTEN do you use Arabic, Hebrew or a language with a script written from RIGHT to LEFT for:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arSpeakFreq = visual.Slider(win=win, name='arSpeakFreq',
    size=(0.5, 0.02), pos=(0, 0.2), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
arListenFreq = visual.Slider(win=win, name='arListenFreq',
    size=(0.5, 0.02), pos=(0, 0.08), units='height',
    labels=[0, '', 2 ,'', 4], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
arReadFreq = visual.Slider(win=win, name='arReadFreq',
    size=(0.5, 0.02), pos=(0, -0.04), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
arWriteFreq = visual.Slider(win=win, name='arWriteFreq',
    size=(0.5, 0.02), pos=(0, -0.16), units='height',
    labels=(0, '', 2, '', 4), ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
aSpeakLabel = visual.TextStim(win=win, name='aSpeakLabel',
    text='Speaking',
    font='Arial',
    units='height', pos=(-0.35, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
aListenLabel = visual.TextStim(win=win, name='aListenLabel',
    text='Listening\n',
    font='Arial',
    units='height', pos=(-0.35, 0.08), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
aReadLabel = visual.TextStim(win=win, name='aReadLabel',
    text='Reading',
    font='Arial',
    units='height', pos=(-0.35, -0.04), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
aWriteLabel = visual.TextStim(win=win, name='aWriteLabel',
    text='Writing',
    font='Arial',
    pos=(-0.35, -0.16), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
textSpaceActivitiesAr = visual.TextStim(win=win, name='textSpaceActivitiesAr',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
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
    text='How many hours/day do you read printed or online material in Arabic or a language written from RIGHT to LEFT:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spaceContinue_3 = visual.TextStim(win=win, name='spaceContinue_3',
    text='Press space to continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_space = keyboard.Keyboard()
arReadHrs = visual.Slider(win=win, name='arReadHrs',
    size=(0.5,0.02), pos=(0, 0.15), units=None,
    labels=['<2', '2-4', '4-6', '6-8', '8+'], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)

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
    text='Have you ever lived in a country where Arabic, Hebrew, Urdu, \nFarsi or Aramaic is the dominant communicating language?\n\n\n                                    1) Yes\n\n    \n                                    2) No',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbCountryYN = keyboard.Keyboard()
key_space_2 = keyboard.Keyboard()
spaceContinue = visual.TextStim(win=win, name='spaceContinue',
    text='Press space to continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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
    text='For how long have you lived in this country / countries?\n\n            1.  Less than 1 year\n\n            2.  1-3 years\n\n            3.  4-7 years\n    \n            4.  More than 7 years',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
arbCountryTime = keyboard.Keyboard()
spaceContinue_2 = visual.TextStim(win=win, name='spaceContinue_2',
    text='Press space to continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_space_3 = keyboard.Keyboard()

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
    text='Which hand do you use to:\n\n                 Use the mouse to respond to these questions.',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=27, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
writeHand = visual.Slider(win=win, name='writeHand',
    size=(0.5, 0.02), pos=(0, 0.2), units='height',
    labels=[1, '', 3, '', 5], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
throwHand = visual.Slider(win=win, name='throwHand',
    size=(0.5, 0.02), pos=(0, 0.08), units='height',
    labels=[1, '', 3, '', 5], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
toothHand = visual.Slider(win=win, name='toothHand',
    size=(0.5, 0.02), pos=(0, -0.04), units='height',
    labels=[1, '', 3, '', 5], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
spoonHand = visual.Slider(win=win, name='spoonHand',
    size=(0.5, 0.02), pos=(0, -0.16), units='height',
    labels=[1, '', 3, '', 5], ticks=(1,2,3,4,5),
    granularity=1, style=['rating'],
    color='White', font='HelveticaBold',
    flip=False)
writeHandLabel = visual.TextStim(win=win, name='writeHandLabel',
    text='Write',
    font='Arial',
    units='height', pos=(-0.35, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
throwHandLabel = visual.TextStim(win=win, name='throwHandLabel',
    text='Throw\n',
    font='Arial',
    units='height', pos=(-0.35, 0.08), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
toothHandLabel = visual.TextStim(win=win, name='toothHandLabel',
    text='Hold your toothbrush',
    font='Arial',
    units='height', pos=(-0.43, -0.04), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
spoonHandLabel = visual.TextStim(win=win, name='spoonHandLabel',
    text='Hold a spoon',
    font='Arial',
    pos=(-0.40, -0.16), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
textSpaceHand = visual.TextStim(win=win, name='textSpaceHand',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=27, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
keySpaceHand = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Q_Finish"
Q_FinishClock = core.Clock()
QDone = visual.TextStim(win=win, name='QDone',
    text='                Questionnaire complete!\n \nPress space to continue with the experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finishQKey = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeInstr"
PracticeInstrClock = core.Clock()
practiceInstr = visual.TextStim(win=win, name='practiceInstr',
    text='In this task, you will judge facial resemblance.\n\nYou will be presented with 3 faces on the screen on each trial.\n\nThe center face is the target face.\n\nPress the LEFT arrow key if the face on the left looks more like the target. \nPress the RIGHT key if the face on the right looks more like the target. \n\nThere is no right or wrong answer. Sometimes it will be hard to decide - this is perfectly normal. \n\nThere will be a few practice trials followed by the main experiment.\n',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=1, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textSpacePractInstr = visual.TextStim(win=win, name='textSpacePractInstr',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
SpacePracticInst = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
mouse.setVisible(False)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeTrials"
PracticeTrialsClock = core.Clock()
imageCenterPract = visual.ImageStim(
    win=win,
    name='imageCenterPract', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageLVFPract = visual.ImageStim(
    win=win,
    name='imageLVFPract', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageRVFPract = visual.ImageStim(
    win=win,
    name='imageRVFPract', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
keyChimericPract = keyboard.Keyboard()
imageCentLabel = visual.TextStim(win=win, name='imageCentLabel',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.025, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
imageLVFLabel = visual.TextStim(win=win, name='imageLVFLabel',
    text='Press the LEFT arrow key \nif you think this face \nlooks more like the target ',
    font='Arial',
    pos=(-0.45, -0.2), height=0.025, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
imageRVFLabel = visual.TextStim(win=win, name='imageRVFLabel',
    text='Press the RIGHT arrow key \nif you think this face \nlooks more like the target ',
    font='Arial',
    pos=(0.45, -0.2), height=0.025, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TrialsInstr"
TrialsInstrClock = core.Clock()
trialsInstr = visual.TextStim(win=win, name='trialsInstr',
    text='You will now begin the actual experiment\n\nThe face in the center is the target face.\n\nPress the LEFT key if the face on the left looks more like the target. \n\nPress the RIGHT key if the face on the right looks more like the target. \n\nThere is no right or wrong answer. \n',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textSpaceTrials = visual.TextStim(win=win, name='textSpaceTrials',
    text='Press space to continue',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keySpaceTrialsInstr = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ChimericTrials"
ChimericTrialsClock = core.Clock()
imageCenter = visual.ImageStim(
    win=win,
    name='imageCenter', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageLVF = visual.ImageStim(
    win=win,
    name='imageLVF', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageRVF = visual.ImageStim(
    win=win,
    name='imageRVF', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.26,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
keyChimeric = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
textEnd = visual.TextStim(win=win, name='textEnd',
    text='Thank you for participating in the study!\n\n          Press escape to quit.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
consentFormLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('consentForm.xlsx'),
    seed=None, name='consentFormLoop')
thisExp.addLoop(consentFormLoop)  # add the loop to the experiment
thisConsentFormLoop = consentFormLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsentFormLoop.rgb)
if thisConsentFormLoop != None:
    for paramName in thisConsentFormLoop:
        exec('{} = thisConsentFormLoop[paramName]'.format(paramName))

for thisConsentFormLoop in consentFormLoop:
    currentLoop = consentFormLoop
    # abbreviate parameter names if possible (e.g. rgb = thisConsentFormLoop.rgb)
    if thisConsentFormLoop != None:
        for paramName in thisConsentFormLoop:
            exec('{} = thisConsentFormLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ConsentForm"-------
    continueRoutine = True
    # update component parameters for each repeat
    consentForm.setImage(image)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ConsentFormComponents = [consentForm, spaceConsent, key_resp]
    for thisComponent in ConsentFormComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConsentFormClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ConsentForm"-------
    while continueRoutine:
        # get current time
        t = ConsentFormClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConsentFormClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *consentForm* updates
        if consentForm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consentForm.frameNStart = frameN  # exact frame index
            consentForm.tStart = t  # local t and not account for scr refresh
            consentForm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consentForm, 'tStartRefresh')  # time at next scr refresh
            consentForm.setAutoDraw(True)
        
        # *spaceConsent* updates
        if spaceConsent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spaceConsent.frameNStart = frameN  # exact frame index
            spaceConsent.tStart = t  # local t and not account for scr refresh
            spaceConsent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spaceConsent, 'tStartRefresh')  # time at next scr refresh
            spaceConsent.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConsentFormComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ConsentForm"-------
    for thisComponent in ConsentFormComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ConsentForm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.200000)
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
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'consentFormLoop'


# ------Prepare to start Routine "AcceptConsent"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
AcceptConsentComponents = [text, key_resp_2]
for thisComponent in AcceptConsentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AcceptConsentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "AcceptConsent"-------
while continueRoutine:
    # get current time
    t = AcceptConsentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AcceptConsentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AcceptConsentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "AcceptConsent"-------
for thisComponent in AcceptConsentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "AcceptConsent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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

# ------Prepare to start Routine "Qstart"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
QstartComponents = [key_resp_3, text_2]
for thisComponent in QstartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QstartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Qstart"-------
while continueRoutine:
    # get current time
    t = QstartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QstartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QstartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Qstart"-------
for thisComponent in QstartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Qstart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
LanguagesComponents = [InstrLanguages, fluentLang, spaceTextLang]
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
    
    # *spaceTextLang* updates
    if spaceTextLang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceTextLang.frameNStart = frameN  # exact frame index
        spaceTextLang.tStart = t  # local t and not account for scr refresh
        spaceTextLang.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceTextLang, 'tStartRefresh')  # time at next scr refresh
        spaceTextLang.setAutoDraw(True)
    
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
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
engSpeak.reset()
engRead.reset()
engWrite.reset()
spaceKey.keys = []
spaceKey.rt = []
_spaceKey_allKeys = []
# setup some python lists for storing info about the mouseProf
gotValidClick = False  # until a click is received
# keep track of which components have finished
ProficiencyEngComponents = [textProficiencyEng, engSpeak, engRead, engWrite, eSpeakLabel, eReadLabel, eWriteLabel, spaceText, spaceKey, mouseProf]
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
    
    # *eSpeakLabel* updates
    if eSpeakLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eSpeakLabel.frameNStart = frameN  # exact frame index
        eSpeakLabel.tStart = t  # local t and not account for scr refresh
        eSpeakLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eSpeakLabel, 'tStartRefresh')  # time at next scr refresh
        eSpeakLabel.setAutoDraw(True)
    
    # *eReadLabel* updates
    if eReadLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eReadLabel.frameNStart = frameN  # exact frame index
        eReadLabel.tStart = t  # local t and not account for scr refresh
        eReadLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eReadLabel, 'tStartRefresh')  # time at next scr refresh
        eReadLabel.setAutoDraw(True)
    
    # *eWriteLabel* updates
    if eWriteLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eWriteLabel.frameNStart = frameN  # exact frame index
        eWriteLabel.tStart = t  # local t and not account for scr refresh
        eWriteLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eWriteLabel, 'tStartRefresh')  # time at next scr refresh
        eWriteLabel.setAutoDraw(True)
    
    # *spaceText* updates
    if spaceText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceText.frameNStart = frameN  # exact frame index
        spaceText.tStart = t  # local t and not account for scr refresh
        spaceText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceText, 'tStartRefresh')  # time at next scr refresh
        spaceText.setAutoDraw(True)
    
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
thisExp.addData('engSpeak.response', engSpeak.getRating())
thisExp.addData('engRead.response', engRead.getRating())
thisExp.addData('engWrite.response', engWrite.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "ProficiencyEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
# setup some python lists for storing info about the mouseActEng
gotValidClick = False  # until a click is received
# keep track of which components have finished
ActivitiesEngComponents = [textActivitiesEng, engSpeakFreq, engListenFreq, engReadFreq, engWriteFreq, engSpeakLabel, engListenLabel, engReadLabel, engWriteLabel, textSpaceActivitiesEng, keyActivitiesEng, mouseActEng]
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
    if engSpeakFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engSpeakFreq.frameNStart = frameN  # exact frame index
        engSpeakFreq.tStart = t  # local t and not account for scr refresh
        engSpeakFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engSpeakFreq, 'tStartRefresh')  # time at next scr refresh
        engSpeakFreq.setAutoDraw(True)
    
    # *engListenFreq* updates
    if engListenFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engListenFreq.frameNStart = frameN  # exact frame index
        engListenFreq.tStart = t  # local t and not account for scr refresh
        engListenFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engListenFreq, 'tStartRefresh')  # time at next scr refresh
        engListenFreq.setAutoDraw(True)
    
    # *engReadFreq* updates
    if engReadFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engReadFreq.frameNStart = frameN  # exact frame index
        engReadFreq.tStart = t  # local t and not account for scr refresh
        engReadFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engReadFreq, 'tStartRefresh')  # time at next scr refresh
        engReadFreq.setAutoDraw(True)
    
    # *engWriteFreq* updates
    if engWriteFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engWriteFreq.frameNStart = frameN  # exact frame index
        engWriteFreq.tStart = t  # local t and not account for scr refresh
        engWriteFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engWriteFreq, 'tStartRefresh')  # time at next scr refresh
        engWriteFreq.setAutoDraw(True)
    
    # *engSpeakLabel* updates
    if engSpeakLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engSpeakLabel.frameNStart = frameN  # exact frame index
        engSpeakLabel.tStart = t  # local t and not account for scr refresh
        engSpeakLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engSpeakLabel, 'tStartRefresh')  # time at next scr refresh
        engSpeakLabel.setAutoDraw(True)
    
    # *engListenLabel* updates
    if engListenLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engListenLabel.frameNStart = frameN  # exact frame index
        engListenLabel.tStart = t  # local t and not account for scr refresh
        engListenLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engListenLabel, 'tStartRefresh')  # time at next scr refresh
        engListenLabel.setAutoDraw(True)
    
    # *engReadLabel* updates
    if engReadLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engReadLabel.frameNStart = frameN  # exact frame index
        engReadLabel.tStart = t  # local t and not account for scr refresh
        engReadLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engReadLabel, 'tStartRefresh')  # time at next scr refresh
        engReadLabel.setAutoDraw(True)
    
    # *engWriteLabel* updates
    if engWriteLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        engWriteLabel.frameNStart = frameN  # exact frame index
        engWriteLabel.tStart = t  # local t and not account for scr refresh
        engWriteLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(engWriteLabel, 'tStartRefresh')  # time at next scr refresh
        engWriteLabel.setAutoDraw(True)
    
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
        theseKeys = keyActivitiesEng.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('engSpeakFreq.response', engSpeakFreq.getRating())
thisExp.addData('engListenFreq.response', engListenFreq.getRating())
thisExp.addData('engReadFreq.response', engReadFreq.getRating())
thisExp.addData('engWriteFreq.response', engWriteFreq.getRating())
thisExp.addData('engWriteLabel.started', engWriteLabel.tStartRefresh)
thisExp.addData('engWriteLabel.stopped', engWriteLabel.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "ActivitiesEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
slider_engReadHrs.reset()
key_reading.keys = []
key_reading.rt = []
_key_reading_allKeys = []
# keep track of which components have finished
ReadingEngComponents = [hoursReading, slider_engReadHrs, space, key_reading]
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
    
    # *slider_engReadHrs* updates
    if slider_engReadHrs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_engReadHrs.frameNStart = frameN  # exact frame index
        slider_engReadHrs.tStart = t  # local t and not account for scr refresh
        slider_engReadHrs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_engReadHrs, 'tStartRefresh')  # time at next scr refresh
        slider_engReadHrs.setAutoDraw(True)
    
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
        theseKeys = key_reading.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('slider_engReadHrs.response', slider_engReadHrs.getRating())
# the Routine "ReadingEng" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
ArSpeak.reset()
ArRead.reset()
ArWrite.reset()
keySpaceAr.keys = []
keySpaceAr.rt = []
_keySpaceAr_allKeys = []
# keep track of which components have finished
ProficiencyArComponents = [textProficiencyAr, ArSpeak, ArRead, ArWrite, arSpeakLabel, arReadLabel, arWriteLabel, textSpaceAr, keySpaceAr]
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
    
    # *ArSpeak* updates
    if ArSpeak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ArSpeak.frameNStart = frameN  # exact frame index
        ArSpeak.tStart = t  # local t and not account for scr refresh
        ArSpeak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArSpeak, 'tStartRefresh')  # time at next scr refresh
        ArSpeak.setAutoDraw(True)
    
    # *ArRead* updates
    if ArRead.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ArRead.frameNStart = frameN  # exact frame index
        ArRead.tStart = t  # local t and not account for scr refresh
        ArRead.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArRead, 'tStartRefresh')  # time at next scr refresh
        ArRead.setAutoDraw(True)
    
    # *ArWrite* updates
    if ArWrite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ArWrite.frameNStart = frameN  # exact frame index
        ArWrite.tStart = t  # local t and not account for scr refresh
        ArWrite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArWrite, 'tStartRefresh')  # time at next scr refresh
        ArWrite.setAutoDraw(True)
    
    # *arSpeakLabel* updates
    if arSpeakLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arSpeakLabel.frameNStart = frameN  # exact frame index
        arSpeakLabel.tStart = t  # local t and not account for scr refresh
        arSpeakLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arSpeakLabel, 'tStartRefresh')  # time at next scr refresh
        arSpeakLabel.setAutoDraw(True)
    
    # *arReadLabel* updates
    if arReadLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arReadLabel.frameNStart = frameN  # exact frame index
        arReadLabel.tStart = t  # local t and not account for scr refresh
        arReadLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arReadLabel, 'tStartRefresh')  # time at next scr refresh
        arReadLabel.setAutoDraw(True)
    
    # *arWriteLabel* updates
    if arWriteLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arWriteLabel.frameNStart = frameN  # exact frame index
        arWriteLabel.tStart = t  # local t and not account for scr refresh
        arWriteLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arWriteLabel, 'tStartRefresh')  # time at next scr refresh
        arWriteLabel.setAutoDraw(True)
    
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
thisExp.addData('ArSpeak.response', ArSpeak.getRating())
thisExp.addData('ArRead.response', ArRead.getRating())
thisExp.addData('ArWrite.response', ArWrite.getRating())
# the Routine "ProficiencyAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
arSpeakFreq.reset()
arListenFreq.reset()
arReadFreq.reset()
arWriteFreq.reset()
keySpaceActivitiesAr.keys = []
keySpaceActivitiesAr.rt = []
_keySpaceActivitiesAr_allKeys = []
# keep track of which components have finished
ActivitiesArComponents = [textActivitiesAr, arSpeakFreq, arListenFreq, arReadFreq, arWriteFreq, aSpeakLabel, aListenLabel, aReadLabel, aWriteLabel, textSpaceActivitiesAr, keySpaceActivitiesAr]
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
    
    # *arSpeakFreq* updates
    if arSpeakFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arSpeakFreq.frameNStart = frameN  # exact frame index
        arSpeakFreq.tStart = t  # local t and not account for scr refresh
        arSpeakFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arSpeakFreq, 'tStartRefresh')  # time at next scr refresh
        arSpeakFreq.setAutoDraw(True)
    
    # *arListenFreq* updates
    if arListenFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arListenFreq.frameNStart = frameN  # exact frame index
        arListenFreq.tStart = t  # local t and not account for scr refresh
        arListenFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arListenFreq, 'tStartRefresh')  # time at next scr refresh
        arListenFreq.setAutoDraw(True)
    
    # *arReadFreq* updates
    if arReadFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arReadFreq.frameNStart = frameN  # exact frame index
        arReadFreq.tStart = t  # local t and not account for scr refresh
        arReadFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arReadFreq, 'tStartRefresh')  # time at next scr refresh
        arReadFreq.setAutoDraw(True)
    
    # *arWriteFreq* updates
    if arWriteFreq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arWriteFreq.frameNStart = frameN  # exact frame index
        arWriteFreq.tStart = t  # local t and not account for scr refresh
        arWriteFreq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arWriteFreq, 'tStartRefresh')  # time at next scr refresh
        arWriteFreq.setAutoDraw(True)
    
    # *aSpeakLabel* updates
    if aSpeakLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        aSpeakLabel.frameNStart = frameN  # exact frame index
        aSpeakLabel.tStart = t  # local t and not account for scr refresh
        aSpeakLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(aSpeakLabel, 'tStartRefresh')  # time at next scr refresh
        aSpeakLabel.setAutoDraw(True)
    
    # *aListenLabel* updates
    if aListenLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        aListenLabel.frameNStart = frameN  # exact frame index
        aListenLabel.tStart = t  # local t and not account for scr refresh
        aListenLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(aListenLabel, 'tStartRefresh')  # time at next scr refresh
        aListenLabel.setAutoDraw(True)
    
    # *aReadLabel* updates
    if aReadLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        aReadLabel.frameNStart = frameN  # exact frame index
        aReadLabel.tStart = t  # local t and not account for scr refresh
        aReadLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(aReadLabel, 'tStartRefresh')  # time at next scr refresh
        aReadLabel.setAutoDraw(True)
    
    # *aWriteLabel* updates
    if aWriteLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        aWriteLabel.frameNStart = frameN  # exact frame index
        aWriteLabel.tStart = t  # local t and not account for scr refresh
        aWriteLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(aWriteLabel, 'tStartRefresh')  # time at next scr refresh
        aWriteLabel.setAutoDraw(True)
    
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
        theseKeys = keySpaceActivitiesAr.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('arSpeakFreq.response', arSpeakFreq.getRating())
thisExp.addData('arListenFreq.response', arListenFreq.getRating())
thisExp.addData('arReadFreq.response', arReadFreq.getRating())
thisExp.addData('arWriteFreq.response', arWriteFreq.getRating())
thisExp.addData('aWriteLabel.started', aWriteLabel.tStartRefresh)
thisExp.addData('aWriteLabel.stopped', aWriteLabel.tStopRefresh)
# the Routine "ActivitiesAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
key_space.keys = []
key_space.rt = []
_key_space_allKeys = []
arReadHrs.reset()
# keep track of which components have finished
ReadingArComponents = [readingAr, spaceContinue_3, key_space, arReadHrs]
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
    
    # *spaceContinue_3* updates
    if spaceContinue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceContinue_3.frameNStart = frameN  # exact frame index
        spaceContinue_3.tStart = t  # local t and not account for scr refresh
        spaceContinue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceContinue_3, 'tStartRefresh')  # time at next scr refresh
        spaceContinue_3.setAutoDraw(True)
    
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
        theseKeys = key_space.getKeys(keyList=['space'], waitRelease=False)
        _key_space_allKeys.extend(theseKeys)
        if len(_key_space_allKeys):
            key_space.keys = _key_space_allKeys[-1].name  # just the last key pressed
            key_space.rt = _key_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *arReadHrs* updates
    if arReadHrs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arReadHrs.frameNStart = frameN  # exact frame index
        arReadHrs.tStart = t  # local t and not account for scr refresh
        arReadHrs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arReadHrs, 'tStartRefresh')  # time at next scr refresh
        arReadHrs.setAutoDraw(True)
    
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
thisExp.addData('arReadHrs.response', arReadHrs.getRating())
# the Routine "ReadingAr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
    key_space_2.keys = []
    key_space_2.rt = []
    _key_space_2_allKeys = []
    # keep track of which components have finished
    CountryArComponents = [textCountAr, arbCountryYN, key_space_2, spaceContinue]
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
            theseKeys = arbCountryYN.getKeys(keyList=['1', '2'], waitRelease=False)
            _arbCountryYN_allKeys.extend(theseKeys)
            if len(_arbCountryYN_allKeys):
                arbCountryYN.keys = _arbCountryYN_allKeys[-1].name  # just the last key pressed
                arbCountryYN.rt = _arbCountryYN_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_space_2* updates
        waitOnFlip = False
        if key_space_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_space_2.frameNStart = frameN  # exact frame index
            key_space_2.tStart = t  # local t and not account for scr refresh
            key_space_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_space_2, 'tStartRefresh')  # time at next scr refresh
            key_space_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_space_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_space_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_space_2.status == STARTED and not waitOnFlip:
            theseKeys = key_space_2.getKeys(keyList=['space'], waitRelease=False)
            _key_space_2_allKeys.extend(theseKeys)
            if len(_key_space_2_allKeys):
                key_space_2.keys = _key_space_2_allKeys[-1].name  # just the last key pressed
                key_space_2.rt = _key_space_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *spaceContinue* updates
        if spaceContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spaceContinue.frameNStart = frameN  # exact frame index
            spaceContinue.tStart = t  # local t and not account for scr refresh
            spaceContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spaceContinue, 'tStartRefresh')  # time at next scr refresh
            spaceContinue.setAutoDraw(True)
        
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
    routineTimer.add(0.200000)
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
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
    key_space_3.keys = []
    key_space_3.rt = []
    _key_space_3_allKeys = []
    # keep track of which components have finished
    TimeArComponents = [textLongCountAr, arbCountryTime, spaceContinue_2, key_space_3]
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
            theseKeys = arbCountryTime.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _arbCountryTime_allKeys.extend(theseKeys)
            if len(_arbCountryTime_allKeys):
                arbCountryTime.keys = _arbCountryTime_allKeys[-1].name  # just the last key pressed
                arbCountryTime.rt = _arbCountryTime_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *spaceContinue_2* updates
        if spaceContinue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spaceContinue_2.frameNStart = frameN  # exact frame index
            spaceContinue_2.tStart = t  # local t and not account for scr refresh
            spaceContinue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spaceContinue_2, 'tStartRefresh')  # time at next scr refresh
            spaceContinue_2.setAutoDraw(True)
        
        # *key_space_3* updates
        waitOnFlip = False
        if key_space_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_space_3.frameNStart = frameN  # exact frame index
            key_space_3.tStart = t  # local t and not account for scr refresh
            key_space_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_space_3, 'tStartRefresh')  # time at next scr refresh
            key_space_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_space_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_space_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_space_3.status == STARTED and not waitOnFlip:
            theseKeys = key_space_3.getKeys(keyList=['space'], waitRelease=False)
            _key_space_3_allKeys.extend(theseKeys)
            if len(_key_space_3_allKeys):
                key_space_3.keys = _key_space_3_allKeys[-1].name  # just the last key pressed
                key_space_3.rt = _key_space_3_allKeys[-1].rt
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
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
HandednessComponents = [textHandedness, writeHand, throwHand, toothHand, spoonHand, writeHandLabel, throwHandLabel, toothHandLabel, spoonHandLabel, textSpaceHand, keySpaceHand]
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
    if writeHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        writeHand.frameNStart = frameN  # exact frame index
        writeHand.tStart = t  # local t and not account for scr refresh
        writeHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(writeHand, 'tStartRefresh')  # time at next scr refresh
        writeHand.setAutoDraw(True)
    
    # *throwHand* updates
    if throwHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        throwHand.frameNStart = frameN  # exact frame index
        throwHand.tStart = t  # local t and not account for scr refresh
        throwHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(throwHand, 'tStartRefresh')  # time at next scr refresh
        throwHand.setAutoDraw(True)
    
    # *toothHand* updates
    if toothHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        toothHand.frameNStart = frameN  # exact frame index
        toothHand.tStart = t  # local t and not account for scr refresh
        toothHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(toothHand, 'tStartRefresh')  # time at next scr refresh
        toothHand.setAutoDraw(True)
    
    # *spoonHand* updates
    if spoonHand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spoonHand.frameNStart = frameN  # exact frame index
        spoonHand.tStart = t  # local t and not account for scr refresh
        spoonHand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spoonHand, 'tStartRefresh')  # time at next scr refresh
        spoonHand.setAutoDraw(True)
    
    # *writeHandLabel* updates
    if writeHandLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        writeHandLabel.frameNStart = frameN  # exact frame index
        writeHandLabel.tStart = t  # local t and not account for scr refresh
        writeHandLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(writeHandLabel, 'tStartRefresh')  # time at next scr refresh
        writeHandLabel.setAutoDraw(True)
    
    # *throwHandLabel* updates
    if throwHandLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        throwHandLabel.frameNStart = frameN  # exact frame index
        throwHandLabel.tStart = t  # local t and not account for scr refresh
        throwHandLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(throwHandLabel, 'tStartRefresh')  # time at next scr refresh
        throwHandLabel.setAutoDraw(True)
    
    # *toothHandLabel* updates
    if toothHandLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        toothHandLabel.frameNStart = frameN  # exact frame index
        toothHandLabel.tStart = t  # local t and not account for scr refresh
        toothHandLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(toothHandLabel, 'tStartRefresh')  # time at next scr refresh
        toothHandLabel.setAutoDraw(True)
    
    # *spoonHandLabel* updates
    if spoonHandLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spoonHandLabel.frameNStart = frameN  # exact frame index
        spoonHandLabel.tStart = t  # local t and not account for scr refresh
        spoonHandLabel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spoonHandLabel, 'tStartRefresh')  # time at next scr refresh
        spoonHandLabel.setAutoDraw(True)
    
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
        theseKeys = keySpaceHand.getKeys(keyList=['space'], waitRelease=False)
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
thisExp.addData('writeHand.response', writeHand.getRating())
thisExp.addData('throwHand.response', throwHand.getRating())
thisExp.addData('toothHand.response', toothHand.getRating())
thisExp.addData('spoonHand.response', spoonHand.getRating())
thisExp.addData('spoonHandLabel.started', spoonHandLabel.tStartRefresh)
thisExp.addData('spoonHandLabel.stopped', spoonHandLabel.tStopRefresh)
# the Routine "Handedness" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
        theseKeys = finishQKey.getKeys(keyList=['space'], waitRelease=False)
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

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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

# ------Prepare to start Routine "PracticeInstr"-------
continueRoutine = True
# update component parameters for each repeat
SpacePracticInst.keys = []
SpacePracticInst.rt = []
_SpacePracticInst_allKeys = []
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
PracticeInstrComponents = [practiceInstr, textSpacePractInstr, SpacePracticInst, mouse]
for thisComponent in PracticeInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeInstr"-------
while continueRoutine:
    # get current time
    t = PracticeInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceInstr* updates
    if practiceInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceInstr.frameNStart = frameN  # exact frame index
        practiceInstr.tStart = t  # local t and not account for scr refresh
        practiceInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceInstr, 'tStartRefresh')  # time at next scr refresh
        practiceInstr.setAutoDraw(True)
    
    # *textSpacePractInstr* updates
    if textSpacePractInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpacePractInstr.frameNStart = frameN  # exact frame index
        textSpacePractInstr.tStart = t  # local t and not account for scr refresh
        textSpacePractInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpacePractInstr, 'tStartRefresh')  # time at next scr refresh
        textSpacePractInstr.setAutoDraw(True)
    
    # *SpacePracticInst* updates
    waitOnFlip = False
    if SpacePracticInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SpacePracticInst.frameNStart = frameN  # exact frame index
        SpacePracticInst.tStart = t  # local t and not account for scr refresh
        SpacePracticInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SpacePracticInst, 'tStartRefresh')  # time at next scr refresh
        SpacePracticInst.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SpacePracticInst.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SpacePracticInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SpacePracticInst.status == STARTED and not waitOnFlip:
        theseKeys = SpacePracticInst.getKeys(keyList=['space'], waitRelease=False)
        _SpacePracticInst_allKeys.extend(theseKeys)
        if len(_SpacePracticInst_allKeys):
            SpacePracticInst.keys = _SpacePracticInst_allKeys[-1].name  # just the last key pressed
            SpacePracticInst.rt = _SpacePracticInst_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeInstr"-------
for thisComponent in PracticeInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "PracticeInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
trialsPractice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticeStimuliPavlovia.xlsx'),
    seed=None, name='trialsPractice')
thisExp.addLoop(trialsPractice)  # add the loop to the experiment
thisTrialsPractice = trialsPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
if thisTrialsPractice != None:
    for paramName in thisTrialsPractice:
        exec('{} = thisTrialsPractice[paramName]'.format(paramName))

for thisTrialsPractice in trialsPractice:
    currentLoop = trialsPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
    if thisTrialsPractice != None:
        for paramName in thisTrialsPractice:
            exec('{} = thisTrialsPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeTrials"-------
    continueRoutine = True
    # update component parameters for each repeat
    imageCenterPract.setPos((0, 0))
    imageCenterPract.setImage(Image)
    imageLVFPract.setPos((-0.45, 0))
    imageLVFPract.setImage(LVF)
    imageRVFPract.setPos((0.45, 0))
    imageRVFPract.setImage(RVF)
    keyChimericPract.keys = []
    keyChimericPract.rt = []
    _keyChimericPract_allKeys = []
    imageCentLabel.setText('TARGET FACE')
    # keep track of which components have finished
    PracticeTrialsComponents = [imageCenterPract, imageLVFPract, imageRVFPract, keyChimericPract, imageCentLabel, imageLVFLabel, imageRVFLabel]
    for thisComponent in PracticeTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeTrials"-------
    while continueRoutine:
        # get current time
        t = PracticeTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageCenterPract* updates
        if imageCenterPract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageCenterPract.frameNStart = frameN  # exact frame index
            imageCenterPract.tStart = t  # local t and not account for scr refresh
            imageCenterPract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageCenterPract, 'tStartRefresh')  # time at next scr refresh
            imageCenterPract.setAutoDraw(True)
        
        # *imageLVFPract* updates
        if imageLVFPract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageLVFPract.frameNStart = frameN  # exact frame index
            imageLVFPract.tStart = t  # local t and not account for scr refresh
            imageLVFPract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageLVFPract, 'tStartRefresh')  # time at next scr refresh
            imageLVFPract.setAutoDraw(True)
        
        # *imageRVFPract* updates
        if imageRVFPract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageRVFPract.frameNStart = frameN  # exact frame index
            imageRVFPract.tStart = t  # local t and not account for scr refresh
            imageRVFPract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRVFPract, 'tStartRefresh')  # time at next scr refresh
            imageRVFPract.setAutoDraw(True)
        
        # *keyChimericPract* updates
        waitOnFlip = False
        if keyChimericPract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyChimericPract.frameNStart = frameN  # exact frame index
            keyChimericPract.tStart = t  # local t and not account for scr refresh
            keyChimericPract.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyChimericPract, 'tStartRefresh')  # time at next scr refresh
            keyChimericPract.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyChimericPract.clock.reset)  # t=0 on next screen flip
        if keyChimericPract.status == STARTED and not waitOnFlip:
            theseKeys = keyChimericPract.getKeys(keyList=['left', 'right', 'escape'], waitRelease=False)
            _keyChimericPract_allKeys.extend(theseKeys)
            if len(_keyChimericPract_allKeys):
                keyChimericPract.keys = _keyChimericPract_allKeys[-1].name  # just the last key pressed
                keyChimericPract.rt = _keyChimericPract_allKeys[-1].rt
                # was this correct?
                if (keyChimericPract.keys == str(correct)) or (keyChimericPract.keys == correct):
                    keyChimericPract.corr = 1
                else:
                    keyChimericPract.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *imageCentLabel* updates
        if imageCentLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageCentLabel.frameNStart = frameN  # exact frame index
            imageCentLabel.tStart = t  # local t and not account for scr refresh
            imageCentLabel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageCentLabel, 'tStartRefresh')  # time at next scr refresh
            imageCentLabel.setAutoDraw(True)
        
        # *imageLVFLabel* updates
        if imageLVFLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageLVFLabel.frameNStart = frameN  # exact frame index
            imageLVFLabel.tStart = t  # local t and not account for scr refresh
            imageLVFLabel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageLVFLabel, 'tStartRefresh')  # time at next scr refresh
            imageLVFLabel.setAutoDraw(True)
        
        # *imageRVFLabel* updates
        if imageRVFLabel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageRVFLabel.frameNStart = frameN  # exact frame index
            imageRVFLabel.tStart = t  # local t and not account for scr refresh
            imageRVFLabel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRVFLabel, 'tStartRefresh')  # time at next scr refresh
            imageRVFLabel.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeTrials"-------
    for thisComponent in PracticeTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyChimericPract.keys in ['', [], None]:  # No response was made
        keyChimericPract.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           keyChimericPract.corr = 1;  # correct non-response
        else:
           keyChimericPract.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsPractice (TrialHandler)
    trialsPractice.addData('keyChimericPract.keys',keyChimericPract.keys)
    trialsPractice.addData('keyChimericPract.corr', keyChimericPract.corr)
    if keyChimericPract.keys != None:  # we had a response
        trialsPractice.addData('keyChimericPract.rt', keyChimericPract.rt)
    trialsPractice.addData('imageRVFLabel.started', imageRVFLabel.tStartRefresh)
    trialsPractice.addData('imageRVFLabel.stopped', imageRVFLabel.tStopRefresh)
    # the Routine "PracticeTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.200000)
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
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsPractice'


# ------Prepare to start Routine "TrialsInstr"-------
continueRoutine = True
# update component parameters for each repeat
keySpaceTrialsInstr.keys = []
keySpaceTrialsInstr.rt = []
_keySpaceTrialsInstr_allKeys = []
# keep track of which components have finished
TrialsInstrComponents = [trialsInstr, textSpaceTrials, keySpaceTrialsInstr]
for thisComponent in TrialsInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrialsInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TrialsInstr"-------
while continueRoutine:
    # get current time
    t = TrialsInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrialsInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trialsInstr* updates
    if trialsInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialsInstr.frameNStart = frameN  # exact frame index
        trialsInstr.tStart = t  # local t and not account for scr refresh
        trialsInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialsInstr, 'tStartRefresh')  # time at next scr refresh
        trialsInstr.setAutoDraw(True)
    
    # *textSpaceTrials* updates
    if textSpaceTrials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpaceTrials.frameNStart = frameN  # exact frame index
        textSpaceTrials.tStart = t  # local t and not account for scr refresh
        textSpaceTrials.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpaceTrials, 'tStartRefresh')  # time at next scr refresh
        textSpaceTrials.setAutoDraw(True)
    
    # *keySpaceTrialsInstr* updates
    waitOnFlip = False
    if keySpaceTrialsInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keySpaceTrialsInstr.frameNStart = frameN  # exact frame index
        keySpaceTrialsInstr.tStart = t  # local t and not account for scr refresh
        keySpaceTrialsInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keySpaceTrialsInstr, 'tStartRefresh')  # time at next scr refresh
        keySpaceTrialsInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keySpaceTrialsInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keySpaceTrialsInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keySpaceTrialsInstr.status == STARTED and not waitOnFlip:
        theseKeys = keySpaceTrialsInstr.getKeys(keyList=['space'], waitRelease=False)
        _keySpaceTrialsInstr_allKeys.extend(theseKeys)
        if len(_keySpaceTrialsInstr_allKeys):
            keySpaceTrialsInstr.keys = _keySpaceTrialsInstr_allKeys[-1].name  # just the last key pressed
            keySpaceTrialsInstr.rt = _keySpaceTrialsInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrialsInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TrialsInstr"-------
for thisComponent in TrialsInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "TrialsInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.200000)
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
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
trialsChimeric = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageStimuliPavlovia.xlsx'),
    seed=None, name='trialsChimeric')
thisExp.addLoop(trialsChimeric)  # add the loop to the experiment
thisTrialsChimeric = trialsChimeric.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsChimeric.rgb)
if thisTrialsChimeric != None:
    for paramName in thisTrialsChimeric:
        exec('{} = thisTrialsChimeric[paramName]'.format(paramName))

for thisTrialsChimeric in trialsChimeric:
    currentLoop = trialsChimeric
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsChimeric.rgb)
    if thisTrialsChimeric != None:
        for paramName in thisTrialsChimeric:
            exec('{} = thisTrialsChimeric[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ChimericTrials"-------
    continueRoutine = True
    # update component parameters for each repeat
    imageCenter.setPos((0, 0))
    imageCenter.setImage(Image)
    imageLVF.setPos((-0.45, 0))
    imageLVF.setImage(LVF)
    imageRVF.setPos((0.45, 0))
    imageRVF.setImage(RVF)
    keyChimeric.keys = []
    keyChimeric.rt = []
    _keyChimeric_allKeys = []
    # keep track of which components have finished
    ChimericTrialsComponents = [imageCenter, imageLVF, imageRVF, keyChimeric]
    for thisComponent in ChimericTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChimericTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ChimericTrials"-------
    while continueRoutine:
        # get current time
        t = ChimericTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChimericTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageCenter* updates
        if imageCenter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageCenter.frameNStart = frameN  # exact frame index
            imageCenter.tStart = t  # local t and not account for scr refresh
            imageCenter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageCenter, 'tStartRefresh')  # time at next scr refresh
            imageCenter.setAutoDraw(True)
        
        # *imageLVF* updates
        if imageLVF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageLVF.frameNStart = frameN  # exact frame index
            imageLVF.tStart = t  # local t and not account for scr refresh
            imageLVF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageLVF, 'tStartRefresh')  # time at next scr refresh
            imageLVF.setAutoDraw(True)
        
        # *imageRVF* updates
        if imageRVF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageRVF.frameNStart = frameN  # exact frame index
            imageRVF.tStart = t  # local t and not account for scr refresh
            imageRVF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageRVF, 'tStartRefresh')  # time at next scr refresh
            imageRVF.setAutoDraw(True)
        
        # *keyChimeric* updates
        waitOnFlip = False
        if keyChimeric.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyChimeric.frameNStart = frameN  # exact frame index
            keyChimeric.tStart = t  # local t and not account for scr refresh
            keyChimeric.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyChimeric, 'tStartRefresh')  # time at next scr refresh
            keyChimeric.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyChimeric.clock.reset)  # t=0 on next screen flip
        if keyChimeric.status == STARTED and not waitOnFlip:
            theseKeys = keyChimeric.getKeys(keyList=['left', 'right', 'escape'], waitRelease=False)
            _keyChimeric_allKeys.extend(theseKeys)
            if len(_keyChimeric_allKeys):
                keyChimeric.keys = _keyChimeric_allKeys[-1].name  # just the last key pressed
                keyChimeric.rt = _keyChimeric_allKeys[-1].rt
                # was this correct?
                if (keyChimeric.keys == str(correct)) or (keyChimeric.keys == correct):
                    keyChimeric.corr = 1
                else:
                    keyChimeric.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChimericTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ChimericTrials"-------
    for thisComponent in ChimericTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyChimeric.keys in ['', [], None]:  # No response was made
        keyChimeric.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           keyChimeric.corr = 1;  # correct non-response
        else:
           keyChimeric.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsChimeric (TrialHandler)
    trialsChimeric.addData('keyChimeric.keys',keyChimeric.keys)
    trialsChimeric.addData('keyChimeric.corr', keyChimeric.corr)
    if keyChimeric.keys != None:  # we had a response
        trialsChimeric.addData('keyChimeric.rt', keyChimeric.rt)
    # the Routine "ChimericTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.200000)
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
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.2-frameTolerance:
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsChimeric'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
EndScreenComponents = [textEnd, keyEnd]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.tStart = t  # local t and not account for scr refresh
        textEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
        textEnd.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['escape'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
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
