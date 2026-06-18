/******************************* 
 * Fullexperiment_Builder Test *
 *******************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'FullExperiment_Builder';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(PracticeInstrRoutineBegin());
flowScheduler.add(PracticeInstrRoutineEachFrame());
flowScheduler.add(PracticeInstrRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeLoopBegin, trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopEnd);
flowScheduler.add(TrialsInstrRoutineBegin());
flowScheduler.add(TrialsInstrRoutineEachFrame());
flowScheduler.add(TrialsInstrRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsChimericLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsChimericLoopBegin, trialsChimericLoopScheduler);
flowScheduler.add(trialsChimericLoopScheduler);
flowScheduler.add(trialsChimericLoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var PracticeInstrClock;
var practiceInstr;
var textSpacePractInstr;
var SpacePracticInst;
var mouse;
var Blank500Clock;
var textBlank;
var PracticeTrialsClock;
var imageCenterPract;
var imageLVFPract;
var imageRVFPract;
var keyChimericPract;
var imageCentLabel;
var imageLVFLabel;
var imageRVFLabel;
var TrialsInstrClock;
var trialsInstr;
var textSpaceTrials;
var keySpaceTrialsInstr;
var ChimericTrialsClock;
var imageCenter;
var imageLVF;
var imageRVF;
var keyChimeric;
var EndScreenClock;
var textEnd;
var keyEnd;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "PracticeInstr"
  PracticeInstrClock = new util.Clock();
  practiceInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInstr',
    text: 'In this task, you will judge facial resemblance.\n\nYou will be presented with 3 faces on the screen on each trial.\n\nThe center face is the target face.\n\nPress the LEFT arrow key if the face on the left looks more like the target. \nPress the RIGHT key if the face on the right looks more like the target. \n\nThere is no right or wrong answer. Sometimes it will be hard to decide - this is perfectly normal. \n\nThere will be a few practice trials followed by the main experiment.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.03,  wrapWidth: 1, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpacePractInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpacePractInstr',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -1.0 
  });
  
  SpacePracticInst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  mouse.setVisible(false);
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeTrials"
  PracticeTrialsClock = new util.Clock();
  imageCenterPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageCenterPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageLVFPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageLVFPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  imageRVFPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageRVFPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  keyChimericPract = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageCentLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageCentLabel',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -4.0 
  });
  
  imageLVFLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageLVFLabel',
    text: 'Press the LEFT arrow key \nif you think this face \nlooks more like the target ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.45), (- 0.2)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -5.0 
  });
  
  imageRVFLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageRVFLabel',
    text: 'Press the RIGHT arrow key \nif you think this face \nlooks more like the target ',
    font: 'Arial',
    units: undefined, 
    pos: [0.45, (- 0.2)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TrialsInstr"
  TrialsInstrClock = new util.Clock();
  trialsInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr',
    text: 'You will now begin the actual experiment\n\nThe face in the center is the target face.\n\nPress the LEFT key if the face on the left looks more like the target. \n\nPress the RIGHT key if the face on the right looks more like the target. \n\nThere is no right or wrong answer. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.03,  wrapWidth: 1, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpaceTrials = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceTrials',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  keySpaceTrialsInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ChimericTrials"
  ChimericTrialsClock = new util.Clock();
  imageCenter = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageCenter', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageLVF = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageLVF', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  imageRVF = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageRVF', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  keyChimeric = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thank you for participating in the study!\n\nThe purpose of this study is to examine whether habitual reading direction affects the way faces are perceived. \n\nPrevious studies have found that humans judge the left side of the face more similar to the whole face than the right side of the face.\n\nHumans also look at the left side of the face more than the right side of the face when identifying faces. \n\nThis study will compare these face perception biases in readers of English (and other languages with right-to-left script) with readers of Arabic (and other languages with left-to-right script).\n\nPress escape to exit. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: 0.0 
  });
  
  keyEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _SpacePracticInst_allKeys;
var gotValidClick;
var PracticeInstrComponents;
function PracticeInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'PracticeInstr'-------
    t = 0;
    PracticeInstrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    SpacePracticInst.keys = undefined;
    SpacePracticInst.rt = undefined;
    _SpacePracticInst_allKeys = [];
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PracticeInstrComponents = [];
    PracticeInstrComponents.push(practiceInstr);
    PracticeInstrComponents.push(textSpacePractInstr);
    PracticeInstrComponents.push(SpacePracticInst);
    PracticeInstrComponents.push(mouse);
    
    for (const thisComponent of PracticeInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function PracticeInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'PracticeInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practiceInstr* updates
    if (t >= 0.0 && practiceInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstr.tStart = t;  // (not accounting for frame time here)
      practiceInstr.frameNStart = frameN;  // exact frame index
      
      practiceInstr.setAutoDraw(true);
    }

    
    // *textSpacePractInstr* updates
    if (t >= 0.0 && textSpacePractInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpacePractInstr.tStart = t;  // (not accounting for frame time here)
      textSpacePractInstr.frameNStart = frameN;  // exact frame index
      
      textSpacePractInstr.setAutoDraw(true);
    }

    
    // *SpacePracticInst* updates
    if (t >= 0.0 && SpacePracticInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SpacePracticInst.tStart = t;  // (not accounting for frame time here)
      SpacePracticInst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SpacePracticInst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SpacePracticInst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SpacePracticInst.clearEvents(); });
    }

    if (SpacePracticInst.status === PsychoJS.Status.STARTED) {
      let theseKeys = SpacePracticInst.getKeys({keyList: ['space'], waitRelease: false});
      _SpacePracticInst_allKeys = _SpacePracticInst_allKeys.concat(theseKeys);
      if (_SpacePracticInst_allKeys.length > 0) {
        SpacePracticInst.keys = _SpacePracticInst_allKeys[_SpacePracticInst_allKeys.length - 1].name;  // just the last key pressed
        SpacePracticInst.rt = _SpacePracticInst_allKeys[_SpacePracticInst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'PracticeInstr'-------
    for (const thisComponent of PracticeInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracticeInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Blank500Components;
function Blank500RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(textBlank);
    
    for (const thisComponent of Blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function Blank500RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Blank500'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textBlank* updates
    if (t >= 0.0 && textBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlank.tStart = t;  // (not accounting for frame time here)
      textBlank.frameNStart = frameN;  // exact frame index
      
      textBlank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textBlank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank500RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Blank500'-------
    for (const thisComponent of Blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var trialsPractice;
var currentLoop;
function trialsPracticeLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsPractice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'PracticeStimuliPavlovia.xlsx',
    seed: undefined, name: 'trialsPractice'
  });
  psychoJS.experiment.addLoop(trialsPractice); // add the loop to the experiment
  currentLoop = trialsPractice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsPractice of trialsPractice) {
    const snapshot = trialsPractice.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(PracticeTrialsRoutineBegin(snapshot));
    thisScheduler.add(PracticeTrialsRoutineEachFrame(snapshot));
    thisScheduler.add(PracticeTrialsRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsPracticeLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPractice);

  return Scheduler.Event.NEXT;
}


var trialsChimeric;
function trialsChimericLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsChimeric = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ImageStimuliPavlovia.xlsx',
    seed: undefined, name: 'trialsChimeric'
  });
  psychoJS.experiment.addLoop(trialsChimeric); // add the loop to the experiment
  currentLoop = trialsChimeric;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsChimeric of trialsChimeric) {
    const snapshot = trialsChimeric.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ChimericTrialsRoutineBegin(snapshot));
    thisScheduler.add(ChimericTrialsRoutineEachFrame(snapshot));
    thisScheduler.add(ChimericTrialsRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsChimericLoopEnd() {
  psychoJS.experiment.removeLoop(trialsChimeric);

  return Scheduler.Event.NEXT;
}


var _keyChimericPract_allKeys;
var PracticeTrialsComponents;
function PracticeTrialsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'PracticeTrials'-------
    t = 0;
    PracticeTrialsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imageCenterPract.setPos([0, 0]);
    imageCenterPract.setImage(Image);
    imageLVFPract.setPos([(- 0.45), 0]);
    imageLVFPract.setImage(LVF);
    imageRVFPract.setPos([0.45, 0]);
    imageRVFPract.setImage(RVF);
    keyChimericPract.keys = undefined;
    keyChimericPract.rt = undefined;
    _keyChimericPract_allKeys = [];
    imageCentLabel.setText('TARGET FACE');
    // keep track of which components have finished
    PracticeTrialsComponents = [];
    PracticeTrialsComponents.push(imageCenterPract);
    PracticeTrialsComponents.push(imageLVFPract);
    PracticeTrialsComponents.push(imageRVFPract);
    PracticeTrialsComponents.push(keyChimericPract);
    PracticeTrialsComponents.push(imageCentLabel);
    PracticeTrialsComponents.push(imageLVFLabel);
    PracticeTrialsComponents.push(imageRVFLabel);
    
    for (const thisComponent of PracticeTrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function PracticeTrialsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'PracticeTrials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeTrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageCenterPract* updates
    if (t >= 0.0 && imageCenterPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCenterPract.tStart = t;  // (not accounting for frame time here)
      imageCenterPract.frameNStart = frameN;  // exact frame index
      
      imageCenterPract.setAutoDraw(true);
    }

    
    // *imageLVFPract* updates
    if (t >= 0.0 && imageLVFPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVFPract.tStart = t;  // (not accounting for frame time here)
      imageLVFPract.frameNStart = frameN;  // exact frame index
      
      imageLVFPract.setAutoDraw(true);
    }

    
    // *imageRVFPract* updates
    if (t >= 0.0 && imageRVFPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVFPract.tStart = t;  // (not accounting for frame time here)
      imageRVFPract.frameNStart = frameN;  // exact frame index
      
      imageRVFPract.setAutoDraw(true);
    }

    
    // *keyChimericPract* updates
    if (t >= 0.0 && keyChimericPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyChimericPract.tStart = t;  // (not accounting for frame time here)
      keyChimericPract.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyChimericPract.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyChimericPract.start(); }); // start on screen flip
    }

    if (keyChimericPract.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyChimericPract.getKeys({keyList: ['left', 'right', 'escape'], waitRelease: false});
      _keyChimericPract_allKeys = _keyChimericPract_allKeys.concat(theseKeys);
      if (_keyChimericPract_allKeys.length > 0) {
        keyChimericPract.keys = _keyChimericPract_allKeys[_keyChimericPract_allKeys.length - 1].name;  // just the last key pressed
        keyChimericPract.rt = _keyChimericPract_allKeys[_keyChimericPract_allKeys.length - 1].rt;
        // was this correct?
        if (keyChimericPract.keys == correct) {
            keyChimericPract.corr = 1;
        } else {
            keyChimericPract.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *imageCentLabel* updates
    if (t >= 0.0 && imageCentLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCentLabel.tStart = t;  // (not accounting for frame time here)
      imageCentLabel.frameNStart = frameN;  // exact frame index
      
      imageCentLabel.setAutoDraw(true);
    }

    
    // *imageLVFLabel* updates
    if (t >= 0.0 && imageLVFLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVFLabel.tStart = t;  // (not accounting for frame time here)
      imageLVFLabel.frameNStart = frameN;  // exact frame index
      
      imageLVFLabel.setAutoDraw(true);
    }

    
    // *imageRVFLabel* updates
    if (t >= 0.0 && imageRVFLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVFLabel.tStart = t;  // (not accounting for frame time here)
      imageRVFLabel.frameNStart = frameN;  // exact frame index
      
      imageRVFLabel.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeTrialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeTrialsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'PracticeTrials'-------
    for (const thisComponent of PracticeTrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (keyChimericPract.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         keyChimericPract.corr = 1;  // correct non-response
      } else {
         keyChimericPract.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyChimericPract.keys', keyChimericPract.keys);
    psychoJS.experiment.addData('keyChimericPract.corr', keyChimericPract.corr);
    if (typeof keyChimericPract.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyChimericPract.rt', keyChimericPract.rt);
        routineTimer.reset();
        }
    
    keyChimericPract.stop();
    // the Routine "PracticeTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keySpaceTrialsInstr_allKeys;
var TrialsInstrComponents;
function TrialsInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'TrialsInstr'-------
    t = 0;
    TrialsInstrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keySpaceTrialsInstr.keys = undefined;
    keySpaceTrialsInstr.rt = undefined;
    _keySpaceTrialsInstr_allKeys = [];
    // keep track of which components have finished
    TrialsInstrComponents = [];
    TrialsInstrComponents.push(trialsInstr);
    TrialsInstrComponents.push(textSpaceTrials);
    TrialsInstrComponents.push(keySpaceTrialsInstr);
    
    for (const thisComponent of TrialsInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function TrialsInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'TrialsInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TrialsInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trialsInstr* updates
    if (t >= 0.0 && trialsInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr.tStart = t;  // (not accounting for frame time here)
      trialsInstr.frameNStart = frameN;  // exact frame index
      
      trialsInstr.setAutoDraw(true);
    }

    
    // *textSpaceTrials* updates
    if (t >= 0.0 && textSpaceTrials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceTrials.tStart = t;  // (not accounting for frame time here)
      textSpaceTrials.frameNStart = frameN;  // exact frame index
      
      textSpaceTrials.setAutoDraw(true);
    }

    
    // *keySpaceTrialsInstr* updates
    if (t >= 0.0 && keySpaceTrialsInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpaceTrialsInstr.tStart = t;  // (not accounting for frame time here)
      keySpaceTrialsInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.clearEvents(); });
    }

    if (keySpaceTrialsInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpaceTrialsInstr.getKeys({keyList: ['space'], waitRelease: false});
      _keySpaceTrialsInstr_allKeys = _keySpaceTrialsInstr_allKeys.concat(theseKeys);
      if (_keySpaceTrialsInstr_allKeys.length > 0) {
        keySpaceTrialsInstr.keys = _keySpaceTrialsInstr_allKeys[_keySpaceTrialsInstr_allKeys.length - 1].name;  // just the last key pressed
        keySpaceTrialsInstr.rt = _keySpaceTrialsInstr_allKeys[_keySpaceTrialsInstr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrialsInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialsInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'TrialsInstr'-------
    for (const thisComponent of TrialsInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "TrialsInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyChimeric_allKeys;
var ChimericTrialsComponents;
function ChimericTrialsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ChimericTrials'-------
    t = 0;
    ChimericTrialsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imageCenter.setPos([0, 0]);
    imageCenter.setImage(Image);
    imageLVF.setPos([(- 0.45), 0]);
    imageLVF.setImage(LVF);
    imageRVF.setPos([0.45, 0]);
    imageRVF.setImage(RVF);
    keyChimeric.keys = undefined;
    keyChimeric.rt = undefined;
    _keyChimeric_allKeys = [];
    // keep track of which components have finished
    ChimericTrialsComponents = [];
    ChimericTrialsComponents.push(imageCenter);
    ChimericTrialsComponents.push(imageLVF);
    ChimericTrialsComponents.push(imageRVF);
    ChimericTrialsComponents.push(keyChimeric);
    
    for (const thisComponent of ChimericTrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function ChimericTrialsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ChimericTrials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ChimericTrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageCenter* updates
    if (t >= 0.0 && imageCenter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCenter.tStart = t;  // (not accounting for frame time here)
      imageCenter.frameNStart = frameN;  // exact frame index
      
      imageCenter.setAutoDraw(true);
    }

    
    // *imageLVF* updates
    if (t >= 0.0 && imageLVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVF.tStart = t;  // (not accounting for frame time here)
      imageLVF.frameNStart = frameN;  // exact frame index
      
      imageLVF.setAutoDraw(true);
    }

    
    // *imageRVF* updates
    if (t >= 0.0 && imageRVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVF.tStart = t;  // (not accounting for frame time here)
      imageRVF.frameNStart = frameN;  // exact frame index
      
      imageRVF.setAutoDraw(true);
    }

    
    // *keyChimeric* updates
    if (t >= 0.0 && keyChimeric.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyChimeric.tStart = t;  // (not accounting for frame time here)
      keyChimeric.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyChimeric.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyChimeric.start(); }); // start on screen flip
    }

    if (keyChimeric.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyChimeric.getKeys({keyList: ['left', 'right', 'escape'], waitRelease: false});
      _keyChimeric_allKeys = _keyChimeric_allKeys.concat(theseKeys);
      if (_keyChimeric_allKeys.length > 0) {
        keyChimeric.keys = _keyChimeric_allKeys[_keyChimeric_allKeys.length - 1].name;  // just the last key pressed
        keyChimeric.rt = _keyChimeric_allKeys[_keyChimeric_allKeys.length - 1].rt;
        // was this correct?
        if (keyChimeric.keys == correct) {
            keyChimeric.corr = 1;
        } else {
            keyChimeric.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ChimericTrialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ChimericTrialsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ChimericTrials'-------
    for (const thisComponent of ChimericTrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (keyChimeric.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         keyChimeric.corr = 1;  // correct non-response
      } else {
         keyChimeric.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyChimeric.keys', keyChimeric.keys);
    psychoJS.experiment.addData('keyChimeric.corr', keyChimeric.corr);
    if (typeof keyChimeric.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyChimeric.rt', keyChimeric.rt);
        routineTimer.reset();
        }
    
    keyChimeric.stop();
    // the Routine "ChimericTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyEnd_allKeys;
var EndScreenComponents;
function EndScreenRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyEnd.keys = undefined;
    keyEnd.rt = undefined;
    _keyEnd_allKeys = [];
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(textEnd);
    EndScreenComponents.push(keyEnd);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EndScreenRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }

    
    // *keyEnd* updates
    if (t >= 0.0 && keyEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyEnd.tStart = t;  // (not accounting for frame time here)
      keyEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.clearEvents(); });
    }

    if (keyEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyEnd.getKeys({keyList: ['escape'], waitRelease: false});
      _keyEnd_allKeys = _keyEnd_allKeys.concat(theseKeys);
      if (_keyEnd_allKeys.length > 0) {
        keyEnd.keys = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].name;  // just the last key pressed
        keyEnd.rt = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
