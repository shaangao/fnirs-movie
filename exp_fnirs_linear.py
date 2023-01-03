# from __future__ import absolute_import, division, print_function
import psychopy
psychopy.useVersion('2021.2.2')
from psychopy import visual, core, event, iohub, data, gui
from psychopy.iohub import launchHubServer
from psychopy.iohub.util import hideWindow, showWindow
import pandas as pd
import os
import time
from psychopy.sound import Microphone
from psychopy.hardware.keyboard import Keyboard



####################################
########## MODE SWITCHES ###########
####################################

fnirs = 0   # 0: no fnirs; 1: with fnirs



####################################
############ INITIALIZE ############
####################################

# Store info about the experiment session
expInfo = {'participant': ''}
dfTimeStamps = pd.read_csv('data_template.csv')    # store ppt ID and time stamps. will be exported to csv.



####################################
############# TIMELINE #############
####################################


############# PREP #############

# get participant ID via dialog
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title='Enter Participant ID')
if not dlg.OK: core.quit()  # if user pressed cancel

# data file name stem = absolute path/data/participant_date (later add file extensions)
expInfo['date'] = data.getDateStr()
filename = os.path.dirname(os.path.abspath(__file__))\
            + os.sep + u'data/%s_%s' % (expInfo['participant'], expInfo['date'])

# export partial data to csv as a safe measure
dfTimeStamps.loc[0,'id'] = expInfo['participant']
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  

# set up window
win = visual.Window((1920, 1080),
    units='pix',
    fullscr=True,
    allowGUI=False,
    monitor='55w_60dist',
    #screen=1,
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
)
win.mouseVisible = False

# set up io devices: keyboard, fnirs, microphone
devicesConfig = {}
io = launchHubServer(window=win, **devicesConfig)
# keyboard
keyboard = io.getDevice('keyboard')
kb = Keyboard(waitForStart=True)
# microphone
recordingDevicesList = Microphone.getDevices()
device=recordingDevicesList[0]
mic = Microphone(streamBufferSecs=1000.0,
                    sampleRateHz=48000,
                    device=recordingDevicesList[0],
                    channels=1,
                    maxRecordingSize=240000,
                    audioRunMode=0
)
# fnirs
if fnirs:
    from pylsl import StreamInfo, StreamOutlet
    lslInfo = StreamInfo(name='Trigger', type='Markers', channel_count=1, channel_format='int32')
    NIRx_trigger = StreamOutlet(lslInfo)    # initialize stream
    print('You should be able to connect NIRx.')


############# COMPONENTS #############

# instruction: check apparatus
instrApparatus = visual.TextStim(win=win, name='instrApparatus',
    text="Check fNIRS trigger \n\n\n\n\n Please wait for the experimenter",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.9
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)

# instruction: video intro
instrVideoIntro = visual.TextStim(win=win, name='instrVideoIntro',
    text="In this study, you will be watching the British television crime drama series Sherlock. \nPlease watch it as you would normally watch a television show that you are interested in. \n\n\n\n\n\nPress ENTER to continue",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.9
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=100.0, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)

# instruction: video ready
instrVideoReady = visual.TextStim(win=win, name='instrVideoReady',
    text="The show is comprised of 2 parts; there will be a short cartoon at the beginning of each part. \nAre you ready for the movie? \n\n\n\n\n\nPress ENTER to start watching",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.9
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=100.0, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)

# video: sherlock 1
sherlock1 = visual.MovieStim3(
    win, name='sherlock1',
    filename='media/sherlock/sherlock_cartoon_part1.m4v',
    # movieLib='ffpyplayer',    # movieLib not available in earlier version of psychopy
    # loop=False, volume=1.0,
    size = (800,500), units = 'pix',
    # pos=(0, 0), size=[1.6, 0.9], units='height',
    # ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# video: sherlock 2
sherlock2 = visual.MovieStim3(
    win, name='sherlock2',
    filename='media/sherlock/sherlock_cartoon_part2.m4v', 
    # movieLib='ffpyplayer',    # movieLib not available in earlier version of psychopy
    # loop=False, volume=1.0,
    size = (800,500), units = 'pix',
    # pos=(0, 0), size=[1.6, 0.9], units=None,
    # ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# instruction: record intro
instrRecordIntro = visual.TextStim(win=win, name='instrRecordIntro',
    text="You just watched the Sherlock show. \n\nNow, we would like you to recount, in your own words, the events in the show in the original order they were viewed in, in as much detail as possible. \n\nSpeak for at least 10 min if possible -- but the longer the better. (You are allowed to speak for as long as you wish.) \nPlease verbally indicate when you are finished by saying, for example, \"I'm done.\" \n\nCompleteness and detail are more important than temporal order. \nIf at any point you realized that you missed something, feel free to return to it. \n\n\n\nPress ENTER when you are ready to begin audio recording",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.5
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=100.0, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)

# instruction: recording
instrRecording = visual.TextStim(win=win, name='instrRecording',
    text="RECORDING... \n\n\n\nVerbally indicate when you are finished and then press ENTER to stop recording",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.9
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=100.0, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)

# instruction: finish
instrFinish = visual.TextStim(win=win, name='instrFinish',
    text="Thank you for your participation! \n\n\n\n\n Please use the pager to call the experimenter back in",
    font='Arial',
    pos=[0, 0], height=24,color='white', units='pix', colorSpace='rgb',
    wrapWidth=win.size[0] * 0.9
    # units='norm', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    # color='white', colorSpace='rgb', opacity=None, 
    # languageStyle='LTR',
    # depth=0.0
)



############# START MAIN #############

# show instruction: check apparatus
instrApparatus.draw()
win.flip()
keys = event.waitKeys(keyList=["g"])

# this marks the start of the main exp
# timer for tracking time stamps
mainExpClock = core.Clock()
# push fnirs sample: start of experiment
if fnirs:
    NIRx_trigger.push_sample([0])

# show instruction: video intro
instrVideoIntro.draw()
win.flip()
keys = event.waitKeys(keyList=["return"])

# show instruction: video ready
instrVideoReady.draw()
win.flip()
keys = event.waitKeys(keyList=["return"])

# video 1
# record start time
dfTimeStamps.loc[0,'video1Start'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save partial data
# push fnirs sample: start of video 1
if fnirs:
    NIRx_trigger.push_sample([1])
# show video: sherlock 1
while sherlock1.status != visual.FINISHED:
    sherlock1.draw()
    win.flip()
# record end time
dfTimeStamps.loc[0,'video1End'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save partial data

# video 2
# record start time
dfTimeStamps.loc[0,'video2Start'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save partial data
# push fnirs sample: start of video 2
if fnirs:
    NIRx_trigger.push_sample([2])
# show video: sherlock 2
while sherlock2.status != visual.FINISHED:
    sherlock1.draw()
    win.flip()
# record end time
dfTimeStamps.loc[0,'video2End'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save partial data
# push fnirs sample: end of video 2
if fnirs:
    NIRx_trigger.push_sample([3])

# show instruction: record intro
instrRecordIntro.draw()
win.flip()
keys = event.waitKeys(keyList=["return"])

# start recording
mic.start()
# record start time
dfTimeStamps.loc[0,'recordStart'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save partial data
# push fnirs sample: start of recording
if fnirs:
    NIRx_trigger.push_sample([4])

# show instruction: recording
instrRecording.draw()
win.flip()
keys = event.waitKeys(keyList=["return"])

# stop recording
mic.stop()
# record end time
dfTimeStamps.loc[0,'recordEnd'] = mainExpClock.getTime()
dfTimeStamps.to_csv(filename + '_timestamps.csv', index=False)  # save data
# push fnirs sample: end of recording
if fnirs:
    NIRx_trigger.push_sample([5])
# save audio
audioClip = mic.getRecording()
audioClip.save(filename + '.wav')

# show instruction: finish
instrFinish.draw()
win.flip()
# push fnirs sample: end of experiment
if fnirs:
    NIRx_trigger.push_sample([6])
# proceed to end
keys = event.waitKeys(keyList=["g"])


############# END #############

# closes experiment
win.close()
io.quit()
core.quit()
