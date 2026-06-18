## This file is part of the Chimeric Face script
DUMMYMODE = True # False for connected eye tracker, True for dummy mode (using mouse or joystick)

# DISPLAY
# used in libscreen; the values may be adjusted, but not the constant's names
SCREENNR = 0 # number of the screen used for displaying experiment
DISPTYPE = 'psychopy' # either 'psychopy' or 'pygame'
DISPSIZE = (1280,1024) # canvas size
SCREENSIZE = (33.8,27.1) # physical screen size
MOUSEVISIBLE = False # mouse visibility
BGC = (127,127,127,255) # backgroundcolour
FGC = (0,0,0,255) # foregroundcolour

# INPUT
KEYLIST = ['left', 'escape', 'right','space'] # None for all keys; list of keynames for keys of choice (e.g. ['space','9',':'] for space, 9 and ; keys)

#
# EYETRACKER
# general
TRACKERTYPE = 'tobii' # either 'smi', 'eyelink' or 'dummy' (NB: if DUMMYMODE is True, trackertype will be set to dummy automatically)
SACCVELTHRESH = 35 # degrees per second, saccade velocity threshold
SACCACCTHRESH = 9500 # degrees per second, saccade acceleration threshold
