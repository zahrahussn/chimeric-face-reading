/******************************* 
 * Fullexperiment_Builder Test *
 *******************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'FullExperiment_Builder';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'age': '', 'sex': '', 'country of residence': '', 'native language': ''};

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
flowScheduler.add(StepQuestScreenRoutineBegin);
flowScheduler.add(StepQuestScreenRoutineEachFrame);
flowScheduler.add(StepQuestScreenRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(LanguagesRoutineBegin);
flowScheduler.add(LanguagesRoutineEachFrame);
flowScheduler.add(LanguagesRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ProficiencyEngRoutineBegin);
flowScheduler.add(ProficiencyEngRoutineEachFrame);
flowScheduler.add(ProficiencyEngRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ActivitiesEngRoutineBegin);
flowScheduler.add(ActivitiesEngRoutineEachFrame);
flowScheduler.add(ActivitiesEngRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ReadingEngRoutineBegin);
flowScheduler.add(ReadingEngRoutineEachFrame);
flowScheduler.add(ReadingEngRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ProficiencyArRoutineBegin);
flowScheduler.add(ProficiencyArRoutineEachFrame);
flowScheduler.add(ProficiencyArRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ActivitiesArRoutineBegin);
flowScheduler.add(ActivitiesArRoutineEachFrame);
flowScheduler.add(ActivitiesArRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(ReadingArRoutineBegin);
flowScheduler.add(ReadingArRoutineEachFrame);
flowScheduler.add(ReadingArRoutineEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
const loopTimeArLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loopTimeArLoopBegin, loopTimeArLoopScheduler);
flowScheduler.add(loopTimeArLoopScheduler);
flowScheduler.add(loopTimeArLoopEnd);
flowScheduler.add(Blank500RoutineBegin);
flowScheduler.add(Blank500RoutineEachFrame);
flowScheduler.add(Blank500RoutineEnd);
flowScheduler.add(HandednessRoutineBegin);
flowScheduler.add(HandednessRoutineEachFrame);
flowScheduler.add(HandednessRoutineEnd);
flowScheduler.add(Q_FinishRoutineBegin);
flowScheduler.add(Q_FinishRoutineEachFrame);
flowScheduler.add(Q_FinishRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.5';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var StepQuestScreenClock;
var mouseWelcome;
var textStepQuest;
var Blank500Clock;
var textBlank;
var LanguagesClock;
var InstrLanguages;
var ProficiencyEngClock;
var mouse;
var mouseInstructions;
var textProficiencyEng;
var text;
var ActivitiesEngClock;
var textActivitiesEng;
var textSpaceActivitiesEng;
var ReadingEngClock;
var hoursReading;
var space;
var ProficiencyArClock;
var textProficiencyAr;
var textSpaceAr;
var ActivitiesArClock;
var textActivitiesAr;
var textSpaceActivitiesAr;
var ReadingArClock;
var readingAr;
var spaceContinue;
var CountryArClock;
var textCountAr;
var TimeArClock;
var textLongCountAr;
var HandednessClock;
var textHandedness;
var textScale;
var textSpaceHand;
var Q_FinishClock;
var QDone;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "StepQuestScreen"
  StepQuestScreenClock = new util.Clock();
  mouseWelcome = new core.Mouse({
    win: psychoJS.window,
  });
  mouseWelcome.mouseClock = new util.Clock();
  textStepQuest = new visual.TextStim({
    win: psychoJS.window,
    name: 'textStepQuest',
    text: '       Please answer the following questions before we begin the experiment. \n\n\n                                            Press SPACE to continue.',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: 30, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Languages"
  LanguagesClock = new util.Clock();
  InstrLanguages = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLanguages',
    text: '            Which language are you most fluent in?\n\n\n    1.   English, French or other European language \n\n    2.   Arabic, Hebrew, Urdu, Farsi, Aramaic, Azeri or Kurdish\n\n    3.   Hindi, Malay or other South Asian or South East Asian language\n\n    4.   Chinese, Japanese or Korean\n\n    5.   Amharic, Berber or other African language\n\n    6.   Other\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.1], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ProficiencyEng"
  ProficiencyEngClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  mouseInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'mouseInstructions',
    text: 'Use the mouse to respond below. ',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.45], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -2.0 
  });
  
  textProficiencyEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textProficiencyEng',
    text: 'How fluent are you in English or any language written from LEFT to RIGHT:',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Press SPACE to continue \n',
    font: 'Arial',
    units : 'height', 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ActivitiesEng"
  ActivitiesEngClock = new util.Clock();
  textActivitiesEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textActivitiesEng',
    text: 'How OFTEN do you use English or a language with a script written from LEFT to RIGHT for:',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpaceActivitiesEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceActivitiesEng',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ReadingEng"
  ReadingEngClock = new util.Clock();
  hoursReading = new visual.TextStim({
    win: psychoJS.window,
    name: 'hoursReading',
    text: 'How many hours/day do you read printed or online material in English or a language written from LEFT to RIGHT:',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  space = new visual.TextStim({
    win: psychoJS.window,
    name: 'space',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : 'height', 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ProficiencyAr"
  ProficiencyArClock = new util.Clock();
  textProficiencyAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textProficiencyAr',
    text: 'How fluent are you in Arabic, Hebrew, Urdu, or any language written from RIGHT to LEFT:',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpaceAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceAr',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ActivitiesAr"
  ActivitiesArClock = new util.Clock();
  textActivitiesAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textActivitiesAr',
    text: 'How OFTEN do you use Arabic, Hebrew or a language with a script written from RIGHT to LEFT for:',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpaceActivitiesAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceActivitiesAr',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ReadingAr"
  ReadingArClock = new util.Clock();
  readingAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'readingAr',
    text: 'How many hours/day do you read printed or online material in Arabic or a language written from LEFT to RIGHT:',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  spaceContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceContinue',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : 'height', 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "CountryAr"
  CountryArClock = new util.Clock();
  textCountAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textCountAr',
    text: 'Have you ever lived in a country where Arabic, Hebrew, Urdu, Farsi or Aramaic is the dominant communicating language?\n\n\n                                                                        1. Yes\n\n                                                                        2. No',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TimeAr"
  TimeArClock = new util.Clock();
  textLongCountAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textLongCountAr',
    text: 'For how long have you lived in this country / countries?\n\n        1.  Less than 1 year\n\n        2.  1-3 years\n\n        3.  4-7 years\n\n        4.  More than 7 years',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.05], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Handedness"
  HandednessClock = new util.Clock();
  textHandedness = new visual.TextStim({
    win: psychoJS.window,
    name: 'textHandedness',
    text: 'Which hand do you use for the following activities:',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  textScale = new visual.TextStim({
    win: psychoJS.window,
    name: 'textScale',
    text: '1: Always left 2: Usually left 3: Both equally 4: Usually right 5: Always right',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('gray'),  opacity: 1,
    depth: -5.0 
  });
  
  textSpaceHand = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceHand',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "Q_Finish"
  Q_FinishClock = new util.Clock();
  QDone = new visual.TextStim({
    win: psychoJS.window,
    name: 'QDone',
    text: '                Questionnaire complete!\n \nPress SPACE to continue with the experiment',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var gotValidClick;
var keySpaceStepQuest;
var StepQuestScreenComponents;
function StepQuestScreenRoutineBegin() {
  //------Prepare to start Routine 'StepQuestScreen'-------
  t = 0;
  StepQuestScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouseWelcome
  gotValidClick = false; // until a click is received
  keySpaceStepQuest = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  StepQuestScreenComponents = [];
  StepQuestScreenComponents.push(mouseWelcome);
  StepQuestScreenComponents.push(textStepQuest);
  StepQuestScreenComponents.push(keySpaceStepQuest);
  
  StepQuestScreenComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function StepQuestScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'StepQuestScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = StepQuestScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textStepQuest* updates
  if (t >= 0.0 && textStepQuest.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textStepQuest.tStart = t;  // (not accounting for frame time here)
    textStepQuest.frameNStart = frameN;  // exact frame index
    textStepQuest.setAutoDraw(true);
  }

  
  // *keySpaceStepQuest* updates
  if (t >= 0.0 && keySpaceStepQuest.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySpaceStepQuest.tStart = t;  // (not accounting for frame time here)
    keySpaceStepQuest.frameNStart = frameN;  // exact frame index
    keySpaceStepQuest.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keySpaceStepQuest.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  StepQuestScreenComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function StepQuestScreenRoutineEnd() {
  //------Ending Routine 'StepQuestScreen'-------
  StepQuestScreenComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  // the Routine "StepQuestScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Blank500Components;
function Blank500RoutineBegin() {
  //------Prepare to start Routine 'Blank500'-------
  t = 0;
  Blank500Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  Blank500Components = [];
  Blank500Components.push(textBlank);
  
  Blank500Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function Blank500RoutineEachFrame() {
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

  frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textBlank.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  Blank500Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Blank500RoutineEnd() {
  //------Ending Routine 'Blank500'-------
  Blank500Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var fluentLang;
var LanguagesComponents;
function LanguagesRoutineBegin() {
  //------Prepare to start Routine 'Languages'-------
  t = 0;
  LanguagesClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  fluentLang = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  LanguagesComponents = [];
  LanguagesComponents.push(InstrLanguages);
  LanguagesComponents.push(fluentLang);
  
  LanguagesComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function LanguagesRoutineEachFrame() {
  //------Loop for each frame of Routine 'Languages'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = LanguagesClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *InstrLanguages* updates
  if (t >= 0.0 && InstrLanguages.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    InstrLanguages.tStart = t;  // (not accounting for frame time here)
    InstrLanguages.frameNStart = frameN;  // exact frame index
    InstrLanguages.setAutoDraw(true);
  }

  
  // *fluentLang* updates
  if (t >= 0.0 && fluentLang.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fluentLang.tStart = t;  // (not accounting for frame time here)
    fluentLang.frameNStart = frameN;  // exact frame index
    fluentLang.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { fluentLang.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (fluentLang.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['1', '2', '3', '4', '5', '6', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      fluentLang.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      fluentLang.rt = fluentLang.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  LanguagesComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function LanguagesRoutineEnd() {
  //------Ending Routine 'Languages'-------
  LanguagesComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  
  // check responses
  if (fluentLang.keys === undefined || fluentLang.keys.length === 0) {    // No response was made
      fluentLang.keys = undefined;
  }
  
  psychoJS.experiment.addData('fluentLang.keys', fluentLang.keys);
  if (typeof fluentLang.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('fluentLang.rt', fluentLang.rt);
      routineTimer.reset();
      }
  
  // the Routine "Languages" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var spaceKey;
var ProficiencyEngComponents;
function ProficiencyEngRoutineBegin() {
  //------Prepare to start Routine 'ProficiencyEng'-------
  t = 0;
  ProficiencyEngClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse
  gotValidClick = false; // until a click is received
  spaceKey = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ProficiencyEngComponents = [];
  ProficiencyEngComponents.push(mouse);
  ProficiencyEngComponents.push(mouseInstructions);
  ProficiencyEngComponents.push(textProficiencyEng);
  ProficiencyEngComponents.push(text);
  ProficiencyEngComponents.push(spaceKey);
  
  ProficiencyEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ProficiencyEngRoutineEachFrame() {
  //------Loop for each frame of Routine 'ProficiencyEng'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ProficiencyEngClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *mouseInstructions* updates
  if (t >= 0.0 && mouseInstructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouseInstructions.tStart = t;  // (not accounting for frame time here)
    mouseInstructions.frameNStart = frameN;  // exact frame index
    mouseInstructions.setAutoDraw(true);
  }

  
  // *textProficiencyEng* updates
  if (t >= 0.0 && textProficiencyEng.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textProficiencyEng.tStart = t;  // (not accounting for frame time here)
    textProficiencyEng.frameNStart = frameN;  // exact frame index
    textProficiencyEng.setAutoDraw(true);
  }

  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *spaceKey* updates
  if (t >= 0.0 && spaceKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    spaceKey.tStart = t;  // (not accounting for frame time here)
    spaceKey.frameNStart = frameN;  // exact frame index
    spaceKey.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (spaceKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['escape', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ProficiencyEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ProficiencyEngRoutineEnd() {
  //------Ending Routine 'ProficiencyEng'-------
  ProficiencyEngComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  // the Routine "ProficiencyEng" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var keyActivitiesEng;
var ActivitiesEngComponents;
function ActivitiesEngRoutineBegin() {
  //------Prepare to start Routine 'ActivitiesEng'-------
  t = 0;
  ActivitiesEngClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keyActivitiesEng = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ActivitiesEngComponents = [];
  ActivitiesEngComponents.push(textActivitiesEng);
  ActivitiesEngComponents.push(textSpaceActivitiesEng);
  ActivitiesEngComponents.push(keyActivitiesEng);
  
  ActivitiesEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ActivitiesEngRoutineEachFrame() {
  //------Loop for each frame of Routine 'ActivitiesEng'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ActivitiesEngClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textActivitiesEng* updates
  if (t >= 0.0 && textActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textActivitiesEng.tStart = t;  // (not accounting for frame time here)
    textActivitiesEng.frameNStart = frameN;  // exact frame index
    textActivitiesEng.setAutoDraw(true);
  }

  
  // *textSpaceActivitiesEng* updates
  if (t >= 0.0 && textSpaceActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textSpaceActivitiesEng.tStart = t;  // (not accounting for frame time here)
    textSpaceActivitiesEng.frameNStart = frameN;  // exact frame index
    textSpaceActivitiesEng.setAutoDraw(true);
  }

  
  // *keyActivitiesEng* updates
  if (t >= 0.0 && keyActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyActivitiesEng.tStart = t;  // (not accounting for frame time here)
    keyActivitiesEng.frameNStart = frameN;  // exact frame index
    keyActivitiesEng.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keyActivitiesEng.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ActivitiesEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ActivitiesEngRoutineEnd() {
  //------Ending Routine 'ActivitiesEng'-------
  ActivitiesEngComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "ActivitiesEng" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_reading;
var ReadingEngComponents;
function ReadingEngRoutineBegin() {
  //------Prepare to start Routine 'ReadingEng'-------
  t = 0;
  ReadingEngClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_reading = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ReadingEngComponents = [];
  ReadingEngComponents.push(hoursReading);
  ReadingEngComponents.push(space);
  ReadingEngComponents.push(key_reading);
  
  ReadingEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ReadingEngRoutineEachFrame() {
  //------Loop for each frame of Routine 'ReadingEng'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ReadingEngClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *hoursReading* updates
  if (t >= 0.0 && hoursReading.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    hoursReading.tStart = t;  // (not accounting for frame time here)
    hoursReading.frameNStart = frameN;  // exact frame index
    hoursReading.setAutoDraw(true);
  }

  
  // *space* updates
  if (t >= 0.0 && space.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    space.tStart = t;  // (not accounting for frame time here)
    space.frameNStart = frameN;  // exact frame index
    space.setAutoDraw(true);
  }

  
  // *key_reading* updates
  if (t >= 0.0 && key_reading.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reading.tStart = t;  // (not accounting for frame time here)
    key_reading.frameNStart = frameN;  // exact frame index
    key_reading.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_reading.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ReadingEngComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ReadingEngRoutineEnd() {
  //------Ending Routine 'ReadingEng'-------
  ReadingEngComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "ReadingEng" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var keySpaceAr;
var ProficiencyArComponents;
function ProficiencyArRoutineBegin() {
  //------Prepare to start Routine 'ProficiencyAr'-------
  t = 0;
  ProficiencyArClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keySpaceAr = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ProficiencyArComponents = [];
  ProficiencyArComponents.push(textProficiencyAr);
  ProficiencyArComponents.push(textSpaceAr);
  ProficiencyArComponents.push(keySpaceAr);
  
  ProficiencyArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ProficiencyArRoutineEachFrame() {
  //------Loop for each frame of Routine 'ProficiencyAr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ProficiencyArClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textProficiencyAr* updates
  if (t >= 0.0 && textProficiencyAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textProficiencyAr.tStart = t;  // (not accounting for frame time here)
    textProficiencyAr.frameNStart = frameN;  // exact frame index
    textProficiencyAr.setAutoDraw(true);
  }

  
  // *textSpaceAr* updates
  if (t >= 0.0 && textSpaceAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textSpaceAr.tStart = t;  // (not accounting for frame time here)
    textSpaceAr.frameNStart = frameN;  // exact frame index
    textSpaceAr.setAutoDraw(true);
  }

  
  // *keySpaceAr* updates
  if (t >= 0.0 && keySpaceAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySpaceAr.tStart = t;  // (not accounting for frame time here)
    keySpaceAr.frameNStart = frameN;  // exact frame index
    keySpaceAr.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keySpaceAr.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['escape', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ProficiencyArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ProficiencyArRoutineEnd() {
  //------Ending Routine 'ProficiencyAr'-------
  ProficiencyArComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "ProficiencyAr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var keySpaceActivitiesAr;
var ActivitiesArComponents;
function ActivitiesArRoutineBegin() {
  //------Prepare to start Routine 'ActivitiesAr'-------
  t = 0;
  ActivitiesArClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keySpaceActivitiesAr = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ActivitiesArComponents = [];
  ActivitiesArComponents.push(textActivitiesAr);
  ActivitiesArComponents.push(textSpaceActivitiesAr);
  ActivitiesArComponents.push(keySpaceActivitiesAr);
  
  ActivitiesArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ActivitiesArRoutineEachFrame() {
  //------Loop for each frame of Routine 'ActivitiesAr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ActivitiesArClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textActivitiesAr* updates
  if (t >= 0.0 && textActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textActivitiesAr.tStart = t;  // (not accounting for frame time here)
    textActivitiesAr.frameNStart = frameN;  // exact frame index
    textActivitiesAr.setAutoDraw(true);
  }

  
  // *textSpaceActivitiesAr* updates
  if (t >= 0.0 && textSpaceActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textSpaceActivitiesAr.tStart = t;  // (not accounting for frame time here)
    textSpaceActivitiesAr.frameNStart = frameN;  // exact frame index
    textSpaceActivitiesAr.setAutoDraw(true);
  }

  
  // *keySpaceActivitiesAr* updates
  if (t >= 0.0 && keySpaceActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySpaceActivitiesAr.tStart = t;  // (not accounting for frame time here)
    keySpaceActivitiesAr.frameNStart = frameN;  // exact frame index
    keySpaceActivitiesAr.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keySpaceActivitiesAr.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ActivitiesArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ActivitiesArRoutineEnd() {
  //------Ending Routine 'ActivitiesAr'-------
  ActivitiesArComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "ActivitiesAr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_space;
var ReadingArComponents;
function ReadingArRoutineBegin() {
  //------Prepare to start Routine 'ReadingAr'-------
  t = 0;
  ReadingArClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_space = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  ReadingArComponents = [];
  ReadingArComponents.push(readingAr);
  ReadingArComponents.push(spaceContinue);
  ReadingArComponents.push(key_space);
  
  ReadingArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function ReadingArRoutineEachFrame() {
  //------Loop for each frame of Routine 'ReadingAr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ReadingArClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *readingAr* updates
  if (t >= 0.0 && readingAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    readingAr.tStart = t;  // (not accounting for frame time here)
    readingAr.frameNStart = frameN;  // exact frame index
    readingAr.setAutoDraw(true);
  }

  
  // *spaceContinue* updates
  if (t >= 0.0 && spaceContinue.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    spaceContinue.tStart = t;  // (not accounting for frame time here)
    spaceContinue.frameNStart = frameN;  // exact frame index
    spaceContinue.setAutoDraw(true);
  }

  
  // *key_space* updates
  if (t >= 0.0 && key_space.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_space.tStart = t;  // (not accounting for frame time here)
    key_space.frameNStart = frameN;  // exact frame index
    key_space.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_space.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  ReadingArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ReadingArRoutineEnd() {
  //------Ending Routine 'ReadingAr'-------
  ReadingArComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "ReadingAr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var loopTimeAr;
var currentLoop;
var trialIterator;
function loopTimeArLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  loopTimeAr = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'loopTimeAr'});
  psychoJS.experiment.addLoop(loopTimeAr); // add the loop to the experiment
  currentLoop = loopTimeAr;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = loopTimeAr[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisLoopTimeAr = result.value;
    thisScheduler.add(importConditions(loopTimeAr));
    thisScheduler.add(CountryArRoutineBegin);
    thisScheduler.add(CountryArRoutineEachFrame);
    thisScheduler.add(CountryArRoutineEnd);
    thisScheduler.add(Blank500RoutineBegin);
    thisScheduler.add(Blank500RoutineEachFrame);
    thisScheduler.add(Blank500RoutineEnd);
    thisScheduler.add(TimeArRoutineBegin);
    thisScheduler.add(TimeArRoutineEachFrame);
    thisScheduler.add(TimeArRoutineEnd);
  }

  return Scheduler.Event.NEXT;
}


function loopTimeArLoopEnd() {
  psychoJS.experiment.removeLoop(loopTimeAr);

  return Scheduler.Event.NEXT;
}

var arbCountryYN;
var CountryArComponents;
function CountryArRoutineBegin() {
  //------Prepare to start Routine 'CountryAr'-------
  t = 0;
  CountryArClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  arbCountryYN = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  CountryArComponents = [];
  CountryArComponents.push(textCountAr);
  CountryArComponents.push(arbCountryYN);
  
  CountryArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function CountryArRoutineEachFrame() {
  //------Loop for each frame of Routine 'CountryAr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = CountryArClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textCountAr* updates
  if (t >= 0.0 && textCountAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textCountAr.tStart = t;  // (not accounting for frame time here)
    textCountAr.frameNStart = frameN;  // exact frame index
    textCountAr.setAutoDraw(true);
  }

  
  // *arbCountryYN* updates
  if (t >= 0.0 && arbCountryYN.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    arbCountryYN.tStart = t;  // (not accounting for frame time here)
    arbCountryYN.frameNStart = frameN;  // exact frame index
    arbCountryYN.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { arbCountryYN.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (arbCountryYN.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['1', '2', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      arbCountryYN.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      arbCountryYN.rt = arbCountryYN.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  CountryArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function CountryArRoutineEnd() {
  //------Ending Routine 'CountryAr'-------
  CountryArComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  
  // check responses
  if (arbCountryYN.keys === undefined || arbCountryYN.keys.length === 0) {    // No response was made
      arbCountryYN.keys = undefined;
  }
  
  psychoJS.experiment.addData('arbCountryYN.keys', arbCountryYN.keys);
  if (typeof arbCountryYN.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('arbCountryYN.rt', arbCountryYN.rt);
      routineTimer.reset();
      }
  
  // the Routine "CountryAr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var arbCountryTime;
var TimeArComponents;
function TimeArRoutineBegin() {
  //------Prepare to start Routine 'TimeAr'-------
  t = 0;
  TimeArClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  arbCountryTime = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  TimeArComponents = [];
  TimeArComponents.push(textLongCountAr);
  TimeArComponents.push(arbCountryTime);
  
  TimeArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function TimeArRoutineEachFrame() {
  //------Loop for each frame of Routine 'TimeAr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = TimeArClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textLongCountAr* updates
  if (t >= 0.0 && textLongCountAr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textLongCountAr.tStart = t;  // (not accounting for frame time here)
    textLongCountAr.frameNStart = frameN;  // exact frame index
    textLongCountAr.setAutoDraw(true);
  }

  
  // *arbCountryTime* updates
  if (t >= 0.0 && arbCountryTime.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    arbCountryTime.tStart = t;  // (not accounting for frame time here)
    arbCountryTime.frameNStart = frameN;  // exact frame index
    arbCountryTime.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { arbCountryTime.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (arbCountryTime.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['1', '2', '3', '4', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      arbCountryTime.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      arbCountryTime.rt = arbCountryTime.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  TimeArComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function TimeArRoutineEnd() {
  //------Ending Routine 'TimeAr'-------
  TimeArComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  
  // check responses
  if (arbCountryTime.keys === undefined || arbCountryTime.keys.length === 0) {    // No response was made
      arbCountryTime.keys = undefined;
  }
  
  psychoJS.experiment.addData('arbCountryTime.keys', arbCountryTime.keys);
  if (typeof arbCountryTime.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('arbCountryTime.rt', arbCountryTime.rt);
      routineTimer.reset();
      }
  
  // the Routine "TimeAr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var keySpaceHand;
var HandednessComponents;
function HandednessRoutineBegin() {
  //------Prepare to start Routine 'Handedness'-------
  t = 0;
  HandednessClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keySpaceHand = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  HandednessComponents = [];
  HandednessComponents.push(textHandedness);
  HandednessComponents.push(textScale);
  HandednessComponents.push(textSpaceHand);
  HandednessComponents.push(keySpaceHand);
  
  HandednessComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function HandednessRoutineEachFrame() {
  //------Loop for each frame of Routine 'Handedness'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = HandednessClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textHandedness* updates
  if (t >= 0.0 && textHandedness.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textHandedness.tStart = t;  // (not accounting for frame time here)
    textHandedness.frameNStart = frameN;  // exact frame index
    textHandedness.setAutoDraw(true);
  }

  
  // *textScale* updates
  if (t >= 0.0 && textScale.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textScale.tStart = t;  // (not accounting for frame time here)
    textScale.frameNStart = frameN;  // exact frame index
    textScale.setAutoDraw(true);
  }

  
  // *textSpaceHand* updates
  if (t >= 0.0 && textSpaceHand.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textSpaceHand.tStart = t;  // (not accounting for frame time here)
    textSpaceHand.frameNStart = frameN;  // exact frame index
    textSpaceHand.setAutoDraw(true);
  }

  
  // *keySpaceHand* updates
  if (t >= 0.0 && keySpaceHand.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keySpaceHand.tStart = t;  // (not accounting for frame time here)
    keySpaceHand.frameNStart = frameN;  // exact frame index
    keySpaceHand.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keySpaceHand.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  HandednessComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function HandednessRoutineEnd() {
  //------Ending Routine 'Handedness'-------
  HandednessComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "Handedness" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var finishQKey;
var Q_FinishComponents;
function Q_FinishRoutineBegin() {
  //------Prepare to start Routine 'Q_Finish'-------
  t = 0;
  Q_FinishClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  finishQKey = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Q_FinishComponents = [];
  Q_FinishComponents.push(QDone);
  Q_FinishComponents.push(finishQKey);
  
  Q_FinishComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function Q_FinishRoutineEachFrame() {
  //------Loop for each frame of Routine 'Q_Finish'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q_FinishClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *QDone* updates
  if (t >= 0.0 && QDone.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    QDone.tStart = t;  // (not accounting for frame time here)
    QDone.frameNStart = frameN;  // exact frame index
    QDone.setAutoDraw(true);
  }

  
  // *finishQKey* updates
  if (t >= 0.0 && finishQKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    finishQKey.tStart = t;  // (not accounting for frame time here)
    finishQKey.frameNStart = frameN;  // exact frame index
    finishQKey.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (finishQKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  Q_FinishComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q_FinishRoutineEnd() {
  //------Ending Routine 'Q_Finish'-------
  Q_FinishComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "Q_Finish" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
