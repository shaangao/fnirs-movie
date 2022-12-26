# from psychopy import locale_setup
# from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import psychopy.iohub as io
from psychopy.hardware import keyboard

import numpy as np
# from numpy import (sin, cos, tan, log, log10, pi, average,
                #    sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
# import sys  # to get file system encoding



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'exp'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
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
    originPath='/Users/apple/Documents/GitHub/fnirs-movie-watching/exp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 960], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "checkApparatus" ---
instrApparatus = visual.TextStim(win=win, name='instrApparatus',
    text="Check fNIRS trigger \n\n\n\n\n Please wait for the experimenter",
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyRespGo = keyboard.Keyboard()

# --- Initialize components for Routine "taskIntro" ---
instrTaskIntro = visual.TextStim(win=win, name='instrTaskIntro',
    text="In this study, you will be watching the British television crime drama series Sherlock. \nPlease watch it as you would normally watch a television show that you are interested in. \n\n\n\n\n\nPress ENTER to continue",
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=100.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyRespReturn = keyboard.Keyboard()

# --- Initialize components for Routine "ready" ---
instrReady = visual.TextStim(win=win, name='instrReady',
    text="Are you ready for the movie? \n\n\n\n\n\nPress ENTER to start watching",
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyRespReturn_2 = keyboard.Keyboard()

# --- Initialize components for Routine "countdown" ---
textCountdown = visual.TextStim(win=win, name='textCountdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "movie1" ---
sherlock1 = visual.MovieStim(
    win, name='sherlock1',
    filename='media/sherlock/sherlock_part1.m4v', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.6, 0.9], units='height',
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
keyRespGoDebug = keyboard.Keyboard()

# --- Initialize components for Routine "movie2" ---
sherlock2 = visual.MovieStim(
    win, name='sherlock2',
    filename='media/sherlock/sherlock_part2.m4v', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.6, 0.9], units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
keyRespGoDebug2 = keyboard.Keyboard()

# --- Initialize components for Routine "finish" ---
instrFinish = visual.TextStim(win=win, name='instrFinish',
    text="Thank you for your participation! \n\n\n\n\n Please wait for the experimenter",
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyRespGo_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "checkApparatus" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespGo.keys = []
keyRespGo.rt = []
_keyRespGo_allKeys = []
# keep track of which components have finished
checkApparatusComponents = [instrApparatus, keyRespGo]
for thisComponent in checkApparatusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "checkApparatus" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrApparatus* updates
    if instrApparatus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrApparatus.frameNStart = frameN  # exact frame index
        instrApparatus.tStart = t  # local t and not account for scr refresh
        instrApparatus.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrApparatus, 'tStartRefresh')  # time at next scr refresh
        instrApparatus.setAutoDraw(True)
    
    # *keyRespGo* updates
    if keyRespGo.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespGo.frameNStart = frameN  # exact frame index
        keyRespGo.tStart = t  # local t and not account for scr refresh
        keyRespGo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespGo, 'tStartRefresh')  # time at next scr refresh
        keyRespGo.status = STARTED
        # keyboard checking is just starting
        keyRespGo.clock.reset()  # now t=0
    if keyRespGo.status == STARTED:
        theseKeys = keyRespGo.getKeys(keyList=['g'], waitRelease=False)
        _keyRespGo_allKeys.extend(theseKeys)
        if len(_keyRespGo_allKeys):
            keyRespGo.keys = _keyRespGo_allKeys[-1].name  # just the last key pressed
            keyRespGo.rt = _keyRespGo_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in checkApparatusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "checkApparatus" ---
for thisComponent in checkApparatusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyRespGo.keys in ['', [], None]:  # No response was made
    keyRespGo.keys = None
thisExp.addData('keyRespGo.keys',keyRespGo.keys)
if keyRespGo.keys != None:  # we had a response
    thisExp.addData('keyRespGo.rt', keyRespGo.rt)
thisExp.nextEntry()
# the Routine "checkApparatus" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "taskIntro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespReturn.keys = []
keyRespReturn.rt = []
_keyRespReturn_allKeys = []
# keep track of which components have finished
taskIntroComponents = [instrTaskIntro, keyRespReturn]
for thisComponent in taskIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "taskIntro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrTaskIntro* updates
    if instrTaskIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrTaskIntro.frameNStart = frameN  # exact frame index
        instrTaskIntro.tStart = t  # local t and not account for scr refresh
        instrTaskIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrTaskIntro, 'tStartRefresh')  # time at next scr refresh
        instrTaskIntro.setAutoDraw(True)
    
    # *keyRespReturn* updates
    if keyRespReturn.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespReturn.frameNStart = frameN  # exact frame index
        keyRespReturn.tStart = t  # local t and not account for scr refresh
        keyRespReturn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespReturn, 'tStartRefresh')  # time at next scr refresh
        keyRespReturn.status = STARTED
        # keyboard checking is just starting
        keyRespReturn.clock.reset()  # now t=0
    if keyRespReturn.status == STARTED:
        theseKeys = keyRespReturn.getKeys(keyList=['return'], waitRelease=False)
        _keyRespReturn_allKeys.extend(theseKeys)
        if len(_keyRespReturn_allKeys):
            keyRespReturn.keys = _keyRespReturn_allKeys[-1].name  # just the last key pressed
            keyRespReturn.rt = _keyRespReturn_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in taskIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "taskIntro" ---
for thisComponent in taskIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyRespReturn.keys in ['', [], None]:  # No response was made
    keyRespReturn.keys = None
thisExp.addData('keyRespReturn.keys',keyRespReturn.keys)
if keyRespReturn.keys != None:  # we had a response
    thisExp.addData('keyRespReturn.rt', keyRespReturn.rt)
thisExp.nextEntry()
# the Routine "taskIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ready" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespReturn_2.keys = []
keyRespReturn_2.rt = []
_keyRespReturn_2_allKeys = []
# keep track of which components have finished
readyComponents = [instrReady, keyRespReturn_2]
for thisComponent in readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ready" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrReady* updates
    if instrReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrReady.frameNStart = frameN  # exact frame index
        instrReady.tStart = t  # local t and not account for scr refresh
        instrReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrReady, 'tStartRefresh')  # time at next scr refresh
        instrReady.setAutoDraw(True)
    
    # *keyRespReturn_2* updates
    if keyRespReturn_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespReturn_2.frameNStart = frameN  # exact frame index
        keyRespReturn_2.tStart = t  # local t and not account for scr refresh
        keyRespReturn_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespReturn_2, 'tStartRefresh')  # time at next scr refresh
        keyRespReturn_2.status = STARTED
        # keyboard checking is just starting
        keyRespReturn_2.clock.reset()  # now t=0
    if keyRespReturn_2.status == STARTED:
        theseKeys = keyRespReturn_2.getKeys(keyList=['return'], waitRelease=False)
        _keyRespReturn_2_allKeys.extend(theseKeys)
        if len(_keyRespReturn_2_allKeys):
            keyRespReturn_2.keys = _keyRespReturn_2_allKeys[-1].name  # just the last key pressed
            keyRespReturn_2.rt = _keyRespReturn_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ready" ---
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyRespReturn_2.keys in ['', [], None]:  # No response was made
    keyRespReturn_2.keys = None
thisExp.addData('keyRespReturn_2.keys',keyRespReturn_2.keys)
if keyRespReturn_2.keys != None:  # we had a response
    thisExp.addData('keyRespReturn_2.rt', keyRespReturn_2.rt)
thisExp.nextEntry()
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "countdown" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
countdownComponents = [textCountdown]
for thisComponent in countdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "countdown" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textCountdown* updates
    if textCountdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textCountdown.frameNStart = frameN  # exact frame index
        textCountdown.tStart = t  # local t and not account for scr refresh
        textCountdown.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textCountdown, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textCountdown.started')
        textCountdown.setAutoDraw(True)
    if textCountdown.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textCountdown.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            textCountdown.tStop = t  # not accounting for scr refresh
            textCountdown.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textCountdown.stopped')
            textCountdown.setAutoDraw(False)
    if textCountdown.status == STARTED:  # only update if drawing
        textCountdown.setText(str(10-int(t)), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "countdown" ---
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- Prepare to start Routine "movie1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespGoDebug.keys = []
keyRespGoDebug.rt = []
_keyRespGoDebug_allKeys = []
# keep track of which components have finished
movie1Components = [sherlock1, keyRespGoDebug]
for thisComponent in movie1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movie1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock1* updates
    if sherlock1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock1.frameNStart = frameN  # exact frame index
        sherlock1.tStart = t  # local t and not account for scr refresh
        sherlock1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sherlock1.started')
        sherlock1.setAutoDraw(True)
        sherlock1.play()
    if sherlock1.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *keyRespGoDebug* updates
    if keyRespGoDebug.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespGoDebug.frameNStart = frameN  # exact frame index
        keyRespGoDebug.tStart = t  # local t and not account for scr refresh
        keyRespGoDebug.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespGoDebug, 'tStartRefresh')  # time at next scr refresh
        keyRespGoDebug.status = STARTED
        # keyboard checking is just starting
        keyRespGoDebug.clock.reset()  # now t=0
    if keyRespGoDebug.status == STARTED:
        theseKeys = keyRespGoDebug.getKeys(keyList=['g'], waitRelease=False)
        _keyRespGoDebug_allKeys.extend(theseKeys)
        if len(_keyRespGoDebug_allKeys):
            keyRespGoDebug.keys = _keyRespGoDebug_allKeys[-1].name  # just the last key pressed
            keyRespGoDebug.rt = _keyRespGoDebug_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movie1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movie1" ---
for thisComponent in movie1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sherlock1.stop()
# check responses
if keyRespGoDebug.keys in ['', [], None]:  # No response was made
    keyRespGoDebug.keys = None
thisExp.addData('keyRespGoDebug.keys',keyRespGoDebug.keys)
if keyRespGoDebug.keys != None:  # we had a response
    thisExp.addData('keyRespGoDebug.rt', keyRespGoDebug.rt)
thisExp.nextEntry()
# the Routine "movie1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "movie2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespGoDebug2.keys = []
keyRespGoDebug2.rt = []
_keyRespGoDebug2_allKeys = []
# keep track of which components have finished
movie2Components = [sherlock2, keyRespGoDebug2]
for thisComponent in movie2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movie2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock2* updates
    if sherlock2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock2.frameNStart = frameN  # exact frame index
        sherlock2.tStart = t  # local t and not account for scr refresh
        sherlock2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sherlock2.started')
        sherlock2.setAutoDraw(True)
        sherlock2.play()
    if sherlock2.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *keyRespGoDebug2* updates
    if keyRespGoDebug2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespGoDebug2.frameNStart = frameN  # exact frame index
        keyRespGoDebug2.tStart = t  # local t and not account for scr refresh
        keyRespGoDebug2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespGoDebug2, 'tStartRefresh')  # time at next scr refresh
        keyRespGoDebug2.status = STARTED
        # keyboard checking is just starting
        keyRespGoDebug2.clock.reset()  # now t=0
    if keyRespGoDebug2.status == STARTED:
        theseKeys = keyRespGoDebug2.getKeys(keyList=['g'], waitRelease=False)
        _keyRespGoDebug2_allKeys.extend(theseKeys)
        if len(_keyRespGoDebug2_allKeys):
            keyRespGoDebug2.keys = _keyRespGoDebug2_allKeys[-1].name  # just the last key pressed
            keyRespGoDebug2.rt = _keyRespGoDebug2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movie2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movie2" ---
for thisComponent in movie2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sherlock2.stop()
# check responses
if keyRespGoDebug2.keys in ['', [], None]:  # No response was made
    keyRespGoDebug2.keys = None
thisExp.addData('keyRespGoDebug2.keys',keyRespGoDebug2.keys)
if keyRespGoDebug2.keys != None:  # we had a response
    thisExp.addData('keyRespGoDebug2.rt', keyRespGoDebug2.rt)
thisExp.nextEntry()
# the Routine "movie2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyRespGo_2.keys = []
keyRespGo_2.rt = []
_keyRespGo_2_allKeys = []
# keep track of which components have finished
finishComponents = [instrFinish, keyRespGo_2]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrFinish* updates
    if instrFinish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrFinish.frameNStart = frameN  # exact frame index
        instrFinish.tStart = t  # local t and not account for scr refresh
        instrFinish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrFinish, 'tStartRefresh')  # time at next scr refresh
        instrFinish.setAutoDraw(True)
    
    # *keyRespGo_2* updates
    if keyRespGo_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyRespGo_2.frameNStart = frameN  # exact frame index
        keyRespGo_2.tStart = t  # local t and not account for scr refresh
        keyRespGo_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyRespGo_2, 'tStartRefresh')  # time at next scr refresh
        keyRespGo_2.status = STARTED
        # keyboard checking is just starting
        keyRespGo_2.clock.reset()  # now t=0
    if keyRespGo_2.status == STARTED:
        theseKeys = keyRespGo_2.getKeys(keyList=['g'], waitRelease=False)
        _keyRespGo_2_allKeys.extend(theseKeys)
        if len(_keyRespGo_2_allKeys):
            keyRespGo_2.keys = _keyRespGo_2_allKeys[-1].name  # just the last key pressed
            keyRespGo_2.rt = _keyRespGo_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyRespGo_2.keys in ['', [], None]:  # No response was made
    keyRespGo_2.keys = None
thisExp.addData('keyRespGo_2.keys',keyRespGo_2.keys)
if keyRespGo_2.keys != None:  # we had a response
    thisExp.addData('keyRespGo_2.rt', keyRespGo_2.rt)
thisExp.nextEntry()
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
